"""Monitor frame for SysBoost."""
import customtkinter as ctk
from src.i18n import t

class MonitorFrame(ctk.CTkFrame):
    """Frame displaying real-time system metrics."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._setup_ui()

    def _setup_ui(self):
        """Builds the monitoring interface."""
        # CPU Section
        self.cpu_label = ctk.CTkLabel(self, text=t("monitor.cpu_usage"), font=ctk.CTkFont(size=14, weight="bold"))
        self.cpu_label.pack(padx=20, pady=(20, 5), anchor="w")

        self.cpu_container = ctk.CTkFrame(self, fg_color="transparent")
        self.cpu_container.pack(fill="x", padx=20, pady=10)
        
        self.cpu_progress = ctk.CTkProgressBar(self.cpu_container, height=20)
        self.cpu_progress.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.cpu_progress.set(0)
        
        self.cpu_value_label = ctk.CTkLabel(self.cpu_container, text="0%", width=50)
        self.cpu_value_label.pack(side="right")

        # RAM Section
        self.ram_label = ctk.CTkLabel(self, text=t("monitor.ram_usage"), font=ctk.CTkFont(size=14, weight="bold"))
        self.ram_label.pack(padx=20, pady=(10, 5), anchor="w")

        self.ram_container = ctk.CTkFrame(self, fg_color="transparent")
        self.ram_container.pack(fill="x", padx=20, pady=10)
        
        self.ram_progress = ctk.CTkProgressBar(self.ram_container, height=20)
        self.ram_progress.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.ram_progress.set(0)
        
        self.ram_value_label = ctk.CTkLabel(self.ram_container, text="0%", width=50)
        self.ram_value_label.pack(side="right")

        # Disk & Network Section
        self.stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.stats_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.stats_frame.grid_columnconfigure((0, 1), weight=1)

        # Disk Card
        self.disk_card = ctk.CTkFrame(self.stats_frame)
        self.disk_card.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(self.disk_card, text=t("monitor.disk_io"), font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
        self.disk_io_label = ctk.CTkLabel(self.disk_card, text="R: 0.0 MB/s | W: 0.0 MB/s")
        self.disk_io_label.pack(pady=10)

        # Network Card
        self.net_card = ctk.CTkFrame(self.stats_frame)
        self.net_card.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        ctk.CTkLabel(self.net_card, text=t("monitor.network"), font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
        self.net_io_label = ctk.CTkLabel(self.net_card, text="D: 0.0 KB/s | U: 0.0 KB/s")
        self.net_io_label.pack(pady=10)

    def update_metrics(self, snapshot):
        """Updates the UI elements with snapshot data."""
        # Update CPU
        self.cpu_progress.set(snapshot.cpu_percent / 100)
        self.cpu_value_label.configure(text=f"{int(snapshot.cpu_percent)}%")

        # Update RAM
        self.ram_progress.set(snapshot.ram_percent / 100)
        self.ram_value_label.configure(text=f"{int(snapshot.ram_percent)}%")

        # Update Disk
        self.disk_io_label.configure(text=f"R: {snapshot.disk_read_mbs} MB/s | W: {snapshot.disk_write_mbs} MB/s")

        # Update Network
        self.net_io_label.configure(text=f"D: {snapshot.net_download_kbs} KB/s | U: {snapshot.net_upload_kbs} KB/s")
