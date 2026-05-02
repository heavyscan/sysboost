"""Overview frame for SysBoost."""
import customtkinter as ctk
from src.core.detector import SystemDetector
from src.core.optimizer import ScoreEngine
from src.i18n import t

class OverviewFrame(ctk.CTkFrame):
    """Frame displaying health score and hardware summary."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._setup_score_section()
        self._setup_hardware_section()
        self._update_data()

    def _setup_score_section(self):
        """Displays the health score prominently."""
        self.score_container = ctk.CTkFrame(self, fg_color="transparent")
        self.score_container.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.score_label = ctk.CTkLabel(
            self.score_container,
            text=t("overview.health_score"),
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.score_label.pack(pady=(0, 5))

        self.score_value = ctk.CTkLabel(
            self.score_container,
            text="--",
            font=ctk.CTkFont(size=64, weight="bold"),
            text_color="#3b8ed0"
        )
        self.score_value.pack()

    def _setup_hardware_section(self):
        """Displays hardware information in cards."""
        self.hardware_label = ctk.CTkLabel(
            self,
            text=t("overview.hardware"),
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.hardware_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")

        # Scrollable frame for cards
        self.cards_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.cards_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.cards_frame.grid_columnconfigure((0, 1), weight=1)

        self.cards = {}
        hardware_items = [
            ("os", t("overview.os")),
            ("cpu", t("overview.cpu")),
            ("ram", t("overview.ram")),
            ("disk", t("overview.disk"))
        ]

        for i, (key, label) in enumerate(hardware_items):
            card = ctk.CTkFrame(self.cards_frame, corner_radius=10)
            card.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
            
            title = ctk.CTkLabel(card, text=label, font=ctk.CTkFont(size=12, weight="bold"), text_color="gray")
            title.pack(padx=15, pady=(10, 0), anchor="w")
            
            value = ctk.CTkLabel(card, text="...", font=ctk.CTkFont(size=14), wraplength=350, justify="left")
            value.pack(padx=15, pady=(5, 15), anchor="w")
            
            self.cards[key] = value

    def _update_data(self):
        """Fetches real hardware data and updates the UI."""
        try:
            profile = SystemDetector.get_profile()
            score = ScoreEngine.calculate_score(profile)

            # Update Score
            self.score_value.configure(text=str(score.overall))
            
            # Update Cards
            self.cards["os"].configure(text=f"{profile.os_name.name} {profile.os_version}")
            self.cards["cpu"].configure(text=f"{profile.cpu.model}\n{profile.cpu.physical_cores} Cores / {profile.cpu.logical_cores} Threads")
            self.cards["ram"].configure(text=f"{profile.ram.total_gb} GB Total\n{profile.ram.available_gb} GB Available")
            
            if profile.disks:
                main_disk = profile.disks[0]
                self.cards["disk"].configure(text=f"{main_disk.device} ({main_disk.disk_type.value})\n{main_disk.free_gb} GB Free of {main_disk.total_gb} GB")
        except Exception as e:
            # Em produção, usaremos o logger e mostraremos erro amigável na UI
            print(f"Error updating overview data: {e}")
