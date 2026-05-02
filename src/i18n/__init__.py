"""SysBoost i18n — internationalization support."""
import json
import locale
from pathlib import Path
import platformdirs

_TRANSLATIONS: dict[str, dict] = {}
_current_lang: str = "en"

def _load_lang(lang: str) -> dict:
    """Load a JSON translation file for the given language code."""
    # Look into src/i18n/locales/
    lang_file = Path(__file__).parent / "locales" / f"{lang}.json"
    if lang_file.exists():
        with open(lang_file, encoding="utf-8") as f:
            return json.load(f)
    return {}

def init(lang: str | None = None) -> None:
    """Initialize i18n. Checks settings.json first, then auto-detects."""
    global _current_lang
    
    # 1. Try to load from settings.json
    config_dir = Path(platformdirs.user_config_dir("SysBoost", "SysBoost"))
    config_file = config_dir / "settings.json"
    
    if lang is None and config_file.exists():
        try:
            with open(config_file, "r") as f:
                lang = json.load(f).get("language")
        except:
            pass

    # 2. Auto-detect if still None
    if lang is None:
        try:
            # Simple check for pt_BR or similar
            sys_loc = locale.getdefaultlocale()[0] or "en"
            lang = "pt" if sys_loc.startswith("pt") else "en"
        except:
            lang = "en"

    _current_lang = lang if lang in ["pt", "en"] else "en"
    
    # Load all available languages
    for lang_code in ["en", "pt"]:
        _TRANSLATIONS[lang_code] = _load_lang(lang_code)

def t(key: str, lang: str | None = None) -> str:
    """Translate a key to the current or specified language."""
    target = lang or _current_lang
    translation = _TRANSLATIONS.get(target, {}).get(key)
    if translation is None:
        # Fallback to English, then to key itself
        translation = _TRANSLATIONS.get("en", {}).get(key, key)
    return translation

def current_lang() -> str:
    """Return the currently active language code."""
    return _current_lang
