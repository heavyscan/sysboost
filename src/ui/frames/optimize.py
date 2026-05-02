"""Optimization management frame for SysBoost."""
import customtkinter as ctk
import platform
from src.ui.components.opt_card import OptimizationCard
from src.core.optimizer import WindowsOptimizer, LinuxOptimizer, MacOSOptimizer
from src.core.detector import SystemDetector
from src.i18n import t

class OptimizeFrame(ctk.CTkFrame):
    """Frame where users can apply system optimizations."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.os_type = platform.system()
        self._init_optimizer()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.title_label = ctk.CTkLabel(
            self, 
            text=t("optimize.title"), 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Scrollable area for cards
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self._load_optimizations()

    def _init_optimizer(self):
        """Initializes the correct optimizer engine."""
        if self.os_type == "Windows":
            self.optimizer = WindowsOptimizer()
        elif self.os_type == "Linux":
            self.optimizer = LinuxOptimizer()
        elif self.os_type == "Darwin":
            self.optimizer = MacOSOptimizer()
        else:
            self.optimizer = None

    def _load_optimizations(self):
        """Loads available optimizations based on OS."""
        if self.os_type == "Windows":
            opts = [
                ("win_power_plan", "High Performance Power Plan", "Sets CPU to maximum performance mode.", "Power"),
                ("win_svc_sysmain", "Disable SysMain", "Reduces disk usage by disabling Superfetch.", "Services"),
                ("win_visual_fx", "Performance Visual Effects", "Disables UI animations for faster response.", "UI/UX"),
                ("win_game_mode", "Enable Game Mode", "Prioritizes games for better FPS.", "System")
            ]
        elif self.os_type == "Linux":
            opts = [
                ("lin_cpu_governor", "Performance Governor", "Sets CPU to maximum frequency.", "CPU"),
                ("lin_sysctl_mem", "Memory Tuning", "Optimizes swappiness and cache usage.", "Memory"),
                ("lin_net_bbr", "TCP BBR", "Speeds up network using Google's BBR algorithm.", "Network")
            ]
        elif self.os_type == "Darwin":
            opts = [
                ("mac_spotlight", "Disable Spotlight", "Stops mds process from indexing files.", "System"),
                ("mac_app_nap", "Disable App Nap", "Prevents background app latency.", "Performance")
            ]
        else:
            opts = []

        for i, (opt_id, name, desc, cat) in enumerate(opts):
            card = OptimizationCard(
                self.scroll_frame,
                opt_id=opt_id,
                name=name,
                description=desc,
                category=cat,
                on_apply=self._apply_opt
            )
            card.pack(fill="x", padx=10, pady=5)

    def _apply_opt(self, opt_id, card):
        """Calls the core optimizer for the given ID."""
        success = False
        try:
            if opt_id == "win_power_plan":
                success = self.optimizer.optimize_power_plan()
            elif "win_svc_" in opt_id:
                # Specific service or all
                results = self.optimizer.disable_unused_services()
                success = any(results.values())
            elif opt_id == "win_visual_fx":
                success = self.optimizer.optimize_visual_effects()
            elif opt_id == "win_game_mode":
                results = self.optimizer.apply_registry_tuning()
                success = results.get("win_game_mode", False)
            
            # Linux & Mac... (to be expanded as needed)
            elif opt_id == "lin_cpu_governor":
                success = self.optimizer.optimize_governor()
            elif opt_id == "mac_spotlight":
                success = self.optimizer.optimize_spotlight()
                
            if success:
                card.update_status("applied")
            else:
                card.update_status("error", "Retry")
                
        except Exception as e:
            print(f"Error applying optimization {opt_id}: {e}")
            card.update_status("error", "Error")
