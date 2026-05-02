"""SysBoost i18n — internationalization support."""
import json
import locale
from pathlib import Path

_TRANSLATIONS: dict[str, dict] = {}
_current_lang: str = "en_US"


def _load_lang(lang: str) -> dict:
    """Load a JSON translation file for the given language code."""
    lang_file = Path(__file__).parent / f"{lang}.json"
    if lang_file.exists():
        with open(lang_file, encoding="utf-8") as f:
            return json.load(f)
    return {}


def init(lang: str | None = None) -> None:
    """Initialize i18n. Auto-detects system locale if lang is None.

    Args:
        lang: Language code, e.g. 'pt_BR' or 'en_US'. Auto-detected if None.
    """
    global _current_lang
    if lang is None:
        try:
            system_locale = locale.getdefaultlocale()[0] or "en_US"
        except Exception:
            system_locale = "en_US"
        lang = system_locale if system_locale in ["pt_BR", "en_US"] else "en_US"
    _current_lang = lang
    for lang_code in ["en_US", "pt_BR"]:
        _TRANSLATIONS[lang_code] = _load_lang(lang_code)


def t(key: str, lang: str | None = None) -> str:
    """Translate a key to the current or specified language.

    Falls back to en_US if the key is not found in the target language.
    Returns the key itself if not found in any language.

    Args:
        key: Translation key, e.g. 'nav.overview'
        lang: Override language for this call only.

    Returns:
        Translated string, or the key if no translation found.
    """
    target = lang or _current_lang
    translation = _TRANSLATIONS.get(target, {}).get(key)
    if translation is None:
        translation = _TRANSLATIONS.get("en_US", {}).get(key, key)
    return translation


def current_lang() -> str:
    """Return the currently active language code."""
    return _current_lang
