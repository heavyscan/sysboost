"""SysBoost main application window."""
import customtkinter as ctk
from src.core.logger import get_logger
from src.i18n import init as i18n_init, t

logger = get_logger("ui.app")

# Default visual configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    """SysBoost main window — full UI implemented in Phase 3."""

    def __init__(self):
        super().__init__()
        i18n_init()

        self.title(t("app.title"))
        self.geometry("1100x700")
        self.minsize(900, 600)
        self._setup_placeholder_ui()
        logger.info("SysBoost App initialized")

    def _setup_placeholder_ui(self):
        """Placeholder UI — replaced by full dashboard in Phase 3."""
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=40, pady=40)

        title = ctk.CTkLabel(
            frame,
            text="⚡ SysBoost",
            font=ctk.CTkFont(size=48, weight="bold"),
        )
        title.pack(expand=True, pady=(60, 10))

        subtitle = ctk.CTkLabel(
            frame,
            text=t("app.detecting"),
            font=ctk.CTkFont(size=18),
            text_color="gray",
        )
        subtitle.pack(pady=(0, 60))


def main():
    """Entry point registered in pyproject.toml [project.scripts]."""
    app = App()
    app.mainloop()
