"""Benchmark frame for SysBoost UI."""
import customtkinter as ctk
import threading
from src.core.benchmark import CPUBenchmark, DiskBenchmark, BenchmarkManager
from src.i18n import t

class BenchmarkFrame(ctk.CTkFrame):
    """Frame for running and viewing system benchmarks."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.manager = BenchmarkManager()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._setup_ui()
        self._load_last_results()

    def _setup_ui(self):
        """Builds the benchmark interface."""
        # Header
        self.title_label = ctk.CTkLabel(
            self, 
            text=t("benchmark.title"), 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Controls
        self.controls = ctk.CTkFrame(self, fg_color="transparent")
        self.controls.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.start_btn = ctk.CTkButton(
            self.controls, 
            text="Start Full Benchmark", 
            command=self._run_benchmark_async
        )
        self.start_btn.pack(side="left", padx=(0, 10))
        
        self.progress_bar = ctk.CTkProgressBar(self.controls, width=300)
        self.progress_bar.pack(side="left", padx=10)
        self.progress_bar.set(0)

        # Results Display
        self.results_frame = ctk.CTkFrame(self)
        self.results_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.results_frame.grid_columnconfigure((0, 1), weight=1)

        # CPU Results
        self.cpu_res_card = ctk.CTkFrame(self.results_frame, corner_radius=10)
        self.cpu_res_card.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.cpu_res_card, text="CPU Score", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
        self.cpu_score_val = ctk.CTkLabel(self.cpu_res_card, text="--", font=ctk.CTkFont(size=36, weight="bold"))
        self.cpu_score_val.pack(pady=10)

        # Disk Results
        self.disk_res_card = ctk.CTkFrame(self.results_frame, corner_radius=10)
        self.disk_res_card.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.disk_res_card, text="Disk Speed (R/W)", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 0))
        self.disk_speed_val = ctk.CTkLabel(self.disk_res_card, text="-- / -- MB/s", font=ctk.CTkFont(size=24, weight="bold"))
        self.disk_speed_val.pack(pady=20)

    def _load_last_results(self):
        """Displays the most recent results from history."""
        history = self.manager.get_history()
        if history:
            last = history[-1]
            self.cpu_score_val.configure(text=str(last["cpu_score"]))
            self.disk_speed_val.configure(text=f"{last['disk_read_mbs']} / {last['disk_write_mbs']} MB/s")

    def _run_benchmark_async(self):
        """Runs the benchmark in a background thread."""
        self.start_btn.configure(state="disabled")
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()
        
        threading.Thread(target=self._execute_benchmark, daemon=True).start()

    def _execute_benchmark(self):
        """The actual benchmark execution logic."""
        try:
            # CPU
            cpu_bench = CPUBenchmark(duration=5)
            cpu_score = cpu_bench.run()
            
            # Disk
            disk_bench = DiskBenchmark(file_size_mb=100)
            write_speed, read_speed = disk_bench.run()
            
            # Save
            self.manager.save_result(cpu_score, write_speed, read_speed)
            
            # Update UI (thread-safe)
            self.after(0, lambda: self._on_benchmark_complete(cpu_score, write_speed, read_speed))
            
        except Exception as e:
            print(f"Benchmark error: {e}")
            self.after(0, lambda: self.start_btn.configure(state="normal"))

    def _on_benchmark_complete(self, cpu_score, write_speed, read_speed):
        """Updates the UI when tests are done."""
        self.progress_bar.stop()
        self.progress_bar.configure(mode="determinate")
        self.progress_bar.set(1)
        self.start_btn.configure(state="normal")
        
        self.cpu_score_val.configure(text=str(cpu_score))
        self.disk_speed_val.configure(text=f"{read_speed} / {write_speed} MB/s")
