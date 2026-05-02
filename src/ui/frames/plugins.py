"""Plugin management frame for SysBoost UI."""
import customtkinter as ctk
from src.plugins.manager import PluginManager
from src.i18n import t

class PluginsFrame(ctk.CTkFrame):
    """Frame for managing system extensions (plugins)."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.manager = PluginManager()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._setup_ui()
        self._load_plugins()

    def _setup_ui(self):
        """Builds the plugin management interface."""
        # Header
        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        
        self.title_label = ctk.CTkLabel(
            self.header, 
            text=t("plugins.title"), 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(side="left")
        
        self.refresh_btn = ctk.CTkButton(
            self.header, 
            text="Scan Plugins", 
            width=100, 
            command=self._load_plugins
        )
        self.refresh_btn.pack(side="right")

        # Plugin List
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

    def _load_plugins(self):
        """Discovers and displays plugins."""
        # Clear current list
        for child in self.scroll_frame.winfo_children():
            child.destroy()
            
        self.manager.load_all_plugins()
        
        if not self.manager.loaded_plugins:
            ctk.CTkLabel(
                self.scroll_frame, 
                text="No plugins found. Place plugins in the app data folder.", 
                text_color="gray",
                wraplength=400
            ).pack(pady=40)
            return

        for p_id, plugin in self.manager.loaded_plugins.items():
            self._create_plugin_card(plugin)

    def _create_plugin_card(self, plugin):
        """Creates a card for a single plugin."""
        card = ctk.CTkFrame(self.scroll_frame)
        card.pack(fill="x", padx=10, pady=5)
        
        # Details
        details = ctk.CTkFrame(card, fg_color="transparent")
        details.pack(side="left", fill="both", expand=True, padx=15, pady=10)
        
        title_box = ctk.CTkFrame(details, fg_color="transparent")
        title_box.pack(fill="x")
        
        ctk.CTkLabel(title_box, text=plugin.name, font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        ctk.CTkLabel(title_box, text=f"v{plugin.version}", font=ctk.CTkFont(size=11), text_color="gray").pack(side="left", padx=10)
        
        ctk.CTkLabel(details, text=plugin.description, font=ctk.CTkFont(size=12), text_color="gray", wraplength=350, justify="left").pack(anchor="w")

        # Toggle Switch (placeholder for actual enable/disable logic)
        switch = ctk.CTkSwitch(card, text="Enabled")
        switch.select() # Loaded = Enabled for now
        switch.pack(side="right", padx=15)
