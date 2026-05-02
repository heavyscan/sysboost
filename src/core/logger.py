"""SysBoost centralized logging system."""
import logging
import sys
from pathlib import Path
from datetime import datetime

try:
    import platformdirs
    def get_log_dir() -> Path:
        log_dir = Path(platformdirs.user_log_dir("SysBoost", "SysBoost"))
        log_dir.mkdir(parents=True, exist_ok=True)
        return log_dir
except ImportError:
    def get_log_dir() -> Path:
        log_dir = Path.home() / ".sysboost" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        return log_dir


def setup_logging(level: int = logging.INFO, log_to_file: bool = True) -> logging.Logger:
    """Configure SysBoost logging.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR).
        log_to_file: If True, also writes to a daily log file.

    Returns:
        Configured root SysBoost logger.
    """
    root_logger = logging.getLogger("sysboost")
    root_logger.setLevel(level)

    if root_logger.handlers:
        return root_logger  # already configured

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    root_logger.addHandler(console)

    # File handler
    if log_to_file:
        try:
            log_file = get_log_dir() / f"sysboost_{datetime.now().strftime('%Y%m%d')}.log"
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)
        except Exception:
            pass  # never crash because of logging

    return root_logger


def get_logger(name: str) -> logging.Logger:
    """Get a child logger under the sysboost namespace.

    Args:
        name: Logger name (e.g. 'ui.app', 'core.detector').

    Returns:
        Logger instance.
    """
    return logging.getLogger(f"sysboost.{name}")
