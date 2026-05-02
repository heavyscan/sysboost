"""Optimization history and revert frame for SysBoost."""
import customtkinter as ctk
from src.core.revert import HistoryManager
from src.i18n import t

class HistoryFrame(ctk.CTkFrame):
    """Frame displaying a log of applied optimizations with revert options."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.history_manager = HistoryManager()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        
        self.title_label = ctk.CTkLabel(
            self.header, 
            text=t("history.title"), 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(side="left")
        
        self.refresh_btn = ctk.CTkButton(
            self.header, 
            text="Refresh", 
            width=80, 
            command=self._load_history
        )
        self.refresh_btn.pack(side="right")

        # History List
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self._load_history()

    def _load_history(self):
        """Loads and displays history items."""
        # Clear existing items
        for child in self.scroll_frame.winfo_children():
            child.destroy()
            
        history = self.history_manager.get_history()
        
        if not history:
            ctk.CTkLabel(self.scroll_frame, text="No optimizations applied yet.", text_color="gray").pack(pady=20)
            return

        # Show in reverse order (newest first)
        for item in reversed(history):
            self._create_history_item(item)

    def _create_history_item(self, item):
        """Creates a single history row."""
        row = ctk.CTkFrame(self.scroll_frame)
        row.pack(fill="x", padx=5, pady=5)
        
        # Details
        details = ctk.CTkFrame(row, fg_color="transparent")
        details.pack(side="left", fill="both", expand=True, padx=15, pady=10)
        
        name = ctk.CTkLabel(details, text=item["name"], font=ctk.CTkFont(size=13, weight="bold"))
        name.pack(anchor="w")
        
        info = f"{item['applied_at'].split('T')[0]} | {item['category']} | Status: {item['status']}"
        subtext = ctk.CTkLabel(details, text=info, font=ctk.CTkFont(size=11), text_color="gray")
        subtext.pack(anchor="w")

        # Revert Button (only if applied)
        if item["status"] == "applied":
            revert_btn = ctk.CTkButton(
                row, 
                text="Rollback", 
                width=80, 
                fg_color="#c0392b", 
                hover_color="#e74c3c",
                command=lambda id=item["id"]: self._revert(id)
            )
            revert_btn.pack(side="right", padx=15)
        else:
            ctk.CTkLabel(row, text="Reverted", text_color="#e67e22", width=80).pack(side="right", padx=15)

    def _revert(self, record_id):
        """Calls the revert logic."""
        if self.history_manager.revert_optimization(record_id):
            self._load_history()
