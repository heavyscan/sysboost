"""Toast notification system for SysBoost UI."""
import customtkinter as ctk

class Toast(ctk.CTkFrame):
    """A floating notification message."""

    def __init__(self, master, message, type="success", duration=3000, **kwargs):
        super().__init__(master, corner_radius=10, **kwargs)
        
        self.duration = duration
        
        # Style based on type
        bg_color = "#2ecc71" if type == "success" else "#e74c3c" if type == "error" else "#333333"
        self.configure(fg_color=bg_color)

        self.label = ctk.CTkLabel(
            self, 
            text=message, 
            text_color="white",
            font=ctk.CTkFont(size=13, weight="bold"),
            padx=20,
            pady=10
        )
        self.label.pack()

        # Position (top-center of the parent window)
        self.place(relx=0.5, rely=0.1, anchor="n")
        
        # Auto-destroy
        self.after(duration, self.destroy)

class ToastManager:
    """Helper to show toasts from anywhere in the UI."""
    
    @staticmethod
    def show(master, message, type="success"):
        return Toast(master, message, type)
