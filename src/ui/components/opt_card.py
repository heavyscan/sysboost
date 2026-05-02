"""Optimization card component for SysBoost UI."""
import customtkinter as ctk

class OptimizationCard(ctk.CTkFrame):
    """A card representing a single optimization action."""

    def __init__(self, master, opt_id, name, description, category, status="pending", on_apply=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.opt_id = opt_id
        self.on_apply = on_apply
        self.status = status

        self.grid_columnconfigure(0, weight=1)
        
        # Header: Name and Category Badge
        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.pack(fill="x", padx=15, pady=(15, 5))
        
        self.name_label = ctk.CTkLabel(self.header, text=name, font=ctk.CTkFont(size=14, weight="bold"))
        self.name_label.pack(side="left")
        
        self.category_badge = ctk.CTkLabel(
            self.header, 
            text=category.upper(), 
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="#333333",
            corner_radius=5,
            padx=10
        )
        self.category_badge.pack(side="right")

        # Description
        self.desc_label = ctk.CTkLabel(
            self, 
            text=description, 
            font=ctk.CTkFont(size=12), 
            text_color="gray",
            wraplength=400,
            justify="left"
        )
        self.desc_label.pack(fill="x", padx=15, pady=(0, 15), anchor="w")

        # Footer: Status and Button
        self.footer = ctk.CTkFrame(self, fg_color="transparent")
        self.footer.pack(fill="x", padx=15, pady=(0, 15))
        
        self.status_indicator = ctk.CTkLabel(
            self.footer, 
            text="● " + status.capitalize(),
            font=ctk.CTkFont(size=12),
            text_color=self._get_status_color(status)
        )
        self.status_indicator.pack(side="left")
        
        self.action_btn = ctk.CTkButton(
            self.footer, 
            text="Apply" if status == "pending" else "Applied",
            width=100,
            height=28,
            command=self._handle_click,
            state="normal" if status == "pending" else "disabled"
        )
        self.action_btn.pack(side="right")

    def _get_status_color(self, status):
        if status == "applied": return "#2ecc71" # Green
        if status == "error": return "#e74c3c"   # Red
        return "#95a5a6" # Gray/Pending

    def _handle_click(self):
        if self.on_apply:
            self.action_btn.configure(state="disabled", text="Applying...")
            self.on_apply(self.opt_id, self)

    def update_status(self, new_status, new_btn_text=None):
        """Updates the visual status of the card."""
        self.status = new_status
        self.status_indicator.configure(
            text="● " + new_status.capitalize(),
            text_color=self._get_status_color(new_status)
        )
        if new_btn_text:
            self.action_btn.configure(text=new_btn_text)
        
        if new_status == "applied":
            self.action_btn.configure(state="disabled", text="Applied")
        elif new_status == "pending":
            self.action_btn.configure(state="normal", text="Apply")
