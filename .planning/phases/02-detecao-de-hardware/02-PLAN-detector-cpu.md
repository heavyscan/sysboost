---
id: "2.2"
phase: 2
wave: 1
title: "Detector de CPU: modelo, fabricante, núcleos e frequência"
depends_on: ["2.1"]
files_modified:
  - "src/core/detector.py"
autonomous: true
requirements:
  - RF-01
---

# Plano 2.2 — Detector de CPU

## Objetivo

Inventariar informações completas sobre o processador: modelo, fabricante (Intel, AMD, ARM, Apple), contagem de núcleos (físicos e lógicos) e frequências. A detecção usará a biblioteca `psutil` (e opcionalmente `cpuinfo` se necessário, mas preferir `psutil` para manter dependências leves).

## Tarefas

### Task 1 — Detecção de Processador

```xml
<task id="2.2.1">
  <title>Implementar detecção de CPU via psutil</title>
  <read_first>
    - src/core/types.py (classe CPUInfo)
    - src/core/detector.py (SystemDetector atual)
  </read_first>
  <action>
    Atualizar `src/core/detector.py`, adicionando o método de detecção de CPU na classe `SystemDetector`:

    ```python
    import psutil
    import cpuinfo  # Certifique-se de que py-cpuinfo está no pyproject.toml se usado, ou implemente parse manual

    # ... dentro da classe SystemDetector:
    
    @staticmethod
    def get_cpu_info() -> 'CPUInfo':
        """Coleta informações detalhadas da CPU."""
        from .types import CPUInfo
        import platform

        # Tentar usar psutil para métricas básicas
        logical_cores = psutil.cpu_count(logical=True) or 1
        physical_cores = psutil.cpu_count(logical=False) or 1
        
        freq = psutil.cpu_freq()
        base_freq = freq.current if freq else 0.0
        max_freq = freq.max if freq else 0.0

        # Para nome do modelo, platform.processor() ou parse de /proc/cpuinfo no Linux
        processor_name = platform.processor()
        vendor = "Unknown"
        
        # Heurística simples de vendor
        name_lower = processor_name.lower()
        if "intel" in name_lower:
            vendor = "Intel"
        elif "amd" in name_lower:
            vendor = "AMD"
        elif "apple" in name_lower:
            vendor = "Apple"
        elif "arm" in name_lower or "aarch64" in platform.machine().lower():
            vendor = "ARM"

        return CPUInfo(
            model=processor_name,
            vendor=vendor,
            physical_cores=physical_cores,
            logical_cores=logical_cores,
            base_freq_mhz=base_freq,
            max_freq_mhz=max_freq,
            cache_l3_mb=None  # Mais complexo sem ferramentas específicas (L3 cache)
        )
    ```
  </action>
  <acceptance_criteria>
    - `SystemDetector.get_cpu_info()` retorna uma instância de `CPUInfo` válida
    - Informações de núcleos lógicos e físicos estão corretas e são `int`
  </acceptance_criteria>
</task>
```

## Must-Haves
- [ ] Detecção de processador robusta que não quebre se o psutil falhar ao ler frequências
