"""SysBoost main application window."""
import customtkinter as ctk
from src.core.logger import get_logger
from src.i18n import init as i18n_init, t
from src.ui.frames.overview import OverviewFrame
from src.ui.frames.monitor import MonitorFrame
from src.ui.frames.optimize import OptimizeFrame
from src.ui.frames.history import HistoryFrame
from src.ui.frames.benchmark import BenchmarkFrame
from src.ui.frames.plugins import PluginsFrame
from src.ui.frames.settings import SettingsFrame
from src.core.worker import MetricsWorker

import sys
import traceback
from src.ui.components.toast import ToastManager

logger = get_logger("ui.app")

# Default visual configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    """SysBoost main window — Dashboard Layout."""

    def __init__(self):
        super().__init__()
        i18n_init()

        self.title(t("app.title"))
        self.geometry("1100x700")
        self.minsize(950, 650)

        # Configuração do grid (1x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._setup_navigation()
        self._setup_frames()
        
        # Inicializar Worker de métricas
        self.worker = MetricsWorker(callback=self._on_metrics_received)
        self.worker.start()
        
        # Iniciar no frame de overview
        self.select_frame_by_name("overview")
        
        logger.info("SysBoost Dashboard Layout initialized")

    def _setup_navigation(self):
        """Configura a sidebar lateral de navegação."""
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        # Logo / Título
        self.navigation_frame_label = ctk.CTkLabel(
            self.navigation_frame, 
            text="⚡ SysBoost",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Botões de Navegação
        self.overview_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=t("nav.overview"),
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("overview")
        )
        self.overview_button.grid(row=1, column=0, sticky="ew")

        self.monitor_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=t("nav.monitor"),
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("monitor")
        )
        self.monitor_button.grid(row=2, column=0, sticky="ew")

        self.optimize_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=t("nav.optimize"),
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("optimize")
        )
        self.optimize_button.grid(row=3, column=0, sticky="ew")
        
        self.benchmark_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=t("nav.benchmark"),
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("benchmark")
        )
        self.benchmark_button.grid(row=4, column=0, sticky="ew")

        self.history_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=t("nav.history"),
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("history")
        )
        self.history_button.grid(row=5, column=0, sticky="ew")

        # Configurações na parte inferior
        self.settings_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=t("nav.settings"),
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("settings")
        )
        self.settings_button.grid(row=9, column=0, sticky="ew")

    def _setup_frames(self):
        """Inicializa os frames de conteúdo."""
        # Frame de Overview Real
        self.overview_frame = OverviewFrame(self, corner_radius=0, fg_color="transparent")

        # Frame de Monitor Real
        self.monitor_frame = MonitorFrame(self, corner_radius=0, fg_color="transparent")

        # Frame de Otimização Real
        self.optimize_frame = OptimizeFrame(self, corner_radius=0, fg_color="transparent")

        # Frame de Histórico Real
        self.history_frame = HistoryFrame(self, corner_radius=0, fg_color="transparent")
        # Frame de Benchmark Real
        self.benchmark_frame = BenchmarkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Frame de Plugins Real
        self.plugins_frame = PluginsFrame(self, corner_radius=0, fg_color="transparent")
        
        # Frame de Configurações Real
        self.settings_frame = SettingsFrame(self, corner_radius=0, fg_color="transparent")

    def report_callback_exception(self, exc, val, tb):
        """Global exception handler for Tkinter callbacks."""
        error_msg = "".join(traceback.format_exception(exc, val, tb))
        logger.error(f"UI Exception: {error_msg}")
        ToastManager.show(self, "An unexpected error occurred. Check logs.", type="error")

    def select_frame_by_name(self, name):
        """Alterna entre os frames de conteúdo."""
        # Resetar cores dos botões
        self.overview_button.configure(fg_color=("gray75", "gray25") if name == "overview" else "transparent")
        self.monitor_button.configure(fg_color=("gray75", "gray25") if name == "monitor" else "transparent")
        self.optimize_button.configure(fg_color=("gray75", "gray25") if name == "optimize" else "transparent")
        self.benchmark_button.configure(fg_color=("gray75", "gray25") if name == "benchmark" else "transparent")
        self.history_button.configure(fg_color=("gray75", "gray25") if name == "history" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # Esconder todos os frames
        if name == "overview":
            self.overview_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.overview_frame.grid_forget()
        
        if name == "monitor":
            self.monitor_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.monitor_frame.grid_forget()

        if name == "optimize":
            self.optimize_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.optimize_frame.grid_forget()

        if name == "benchmark":
            self.benchmark_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.benchmark_frame.grid_forget()

        if name == "history":
            self.history_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.history_frame.grid_forget()

        if name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()

    def _on_metrics_received(self, snapshot):
        """Callback executado pelo worker (thread separada)."""
        # Agendar atualização na thread principal do CustomTkinter
        self.after(0, lambda: self.monitor_frame.update_metrics(snapshot))



def main():
    """Entry point registered in pyproject.toml [project.scripts]."""
    app = App()
    app.mainloop()
