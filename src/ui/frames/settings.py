"""Settings frame for SysBoost UI."""
import customtkinter as ctk
import json
from pathlib import Path
import platformdirs
from src.i18n import t

class SettingsFrame(ctk.CTkFrame):
    """Frame for managing application settings like language and theme."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config_dir = Path(platformdirs.user_config_dir("SysBoost", "SysBoost"))
        self.config_file = self.config_dir / "settings.json"
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._setup_ui()

    def _setup_ui(self):
        """Builds the settings interface."""
        # Header
        self.title_label = ctk.CTkLabel(
            self, 
            text=t("settings.title"), 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Settings Container
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        # Language Selection
        ctk.CTkLabel(self.container, text=t("settings.language"), font=ctk.CTkFont(size=14)).grid(row=0, column=0, padx=20, pady=20, sticky="w")
        
        current_lang = self._get_current_lang()
        self.lang_menu = ctk.CTkOptionMenu(
            self.container, 
            values=["English", "Português"],
            command=self._change_language
        )
        self.lang_menu.set("Português" if current_lang == "pt" else "English")
        self.lang_menu.grid(row=0, column=1, padx=20, pady=20, sticky="e")

        # Info Message
        self.info_label = ctk.CTkLabel(
            self, 
            text=t("settings.restart_msg"), 
            font=ctk.CTkFont(size=12), 
            text_color="gray"
        )
        self.info_label.grid(row=2, column=0, padx=20, pady=10, sticky="n")

    def _get_current_lang(self) -> str:
        """Loads the current language from settings file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    return json.load(f).get("language", "en")
            except:
                pass
        return "en"

    def _change_language(self, lang_name):
        """Saves the new language setting."""
        from src.ui.components.toast import ToastManager
        lang_code = "pt" if lang_name == "Português" else "en"
        
        config = {"language": lang_code}
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_file, "w") as f:
            json.dump(config, f)
            
        ToastManager.show(self.winfo_toplevel(), t("settings.restart_msg"), type="success")
