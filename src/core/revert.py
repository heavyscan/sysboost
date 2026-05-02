"""RevertManager — manages the optimization history and revert operations."""
import json
from pathlib import Path
from datetime import datetime
from .logger import get_logger
from .types import OptimizationRecord, OptimizationStatus

logger = get_logger("core.revert")

HISTORY_FILE = Path.home() / ".sysboost" / "history.json"


class RevertManager:
    """Persists optimization history and enables reverting changes.

    History is saved to ~/.sysboost/history.json as a JSON list.
    Each entry contains the before value, after value, and all data
    needed to undo the optimization.
    """

    def __init__(self, history_path: Path | None = None):
        self._path = history_path or HISTORY_FILE
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._records: list[OptimizationRecord] = []
        self._load()

    def _load(self) -> None:
        """Load history from disk."""
        if self._path.exists():
            try:
                with open(self._path, encoding="utf-8") as f:
                    data = json.load(f)
                self._records = [self._from_dict(r) for r in data]
            except Exception as e:
                logger.warning(f"Could not load history: {e}")

    def _save(self) -> None:
        """Persist history to disk."""
        try:
            with open(self._path, "w", encoding="utf-8") as f:
                json.dump([self._to_dict(r) for r in self._records], f, indent=2)
        except Exception as e:
            logger.error(f"Could not save history: {e}")

    def record(self, record: OptimizationRecord) -> None:
        """Add a new optimization record to history."""
        self._records.append(record)
        self._save()
        logger.info(f"Recorded optimization: {record.name}")

    def get_all(self) -> list[OptimizationRecord]:
        """Return all optimization records, newest first."""
        return list(reversed(self._records))

    def get_applied(self) -> list[OptimizationRecord]:
        """Return only currently applied (not yet reverted) optimizations."""
        return [r for r in self._records if r.status == OptimizationStatus.APPLIED]

    def mark_reverted(self, record_id: str) -> bool:
        """Mark a record as reverted by its ID."""
        for record in self._records:
            if record.id == record_id:
                record.status = OptimizationStatus.REVERTED
                self._save()
                return True
        return False

    def clear(self) -> None:
        """Clear all history records."""
        self._records = []
        self._save()

    @staticmethod
    def _to_dict(r: OptimizationRecord) -> dict:
        return {
            "id": r.id,
            "name": r.name,
            "category": r.category,
            "applied_at": r.applied_at.isoformat(),
            "before_value": r.before_value,
            "after_value": r.after_value,
            "revert_data": r.revert_data,
            "status": r.status.value,
        }

    @staticmethod
    def _from_dict(d: dict) -> OptimizationRecord:
        return OptimizationRecord(
            id=d["id"],
            name=d["name"],
            category=d["category"],
            applied_at=datetime.fromisoformat(d["applied_at"]),
            before_value=d["before_value"],
            after_value=d["after_value"],
            revert_data=d["revert_data"],
            status=OptimizationStatus(d.get("status", "applied")),
        )
