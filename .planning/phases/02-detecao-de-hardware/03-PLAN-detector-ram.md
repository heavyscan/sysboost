---
id: "2.3"
phase: 2
wave: 1
title: "Detector de RAM: capacidade e estado atual"
depends_on: ["2.1"]
files_modified:
  - "src/core/detector.py"
autonomous: true
requirements:
  - RF-01
---

# Plano 2.3 — Detector de RAM

## Objetivo

Inventariar a quantidade total de memória RAM, a quantidade disponível no momento e informações adicionais (frequência e tipo, caso seja possível sem elevação excessiva, o que varia muito de sistema operacional para sistema operacional).

## Tarefas

### Task 1 — Detecção de Memória RAM

```xml
<task id="2.3.1">
  <title>Implementar detecção de RAM via psutil</title>
  <read_first>
    - src/core/types.py (classe RAMInfo)
    - src/core/detector.py (SystemDetector atual)
  </read_first>
  <action>
    Atualizar `src/core/detector.py`, adicionando `get_ram_info` à classe `SystemDetector`:

    ```python
    @staticmethod
    def get_ram_info() -> 'RAMInfo':
        """Coleta informações sobre a memória RAM do sistema."""
        from .types import RAMInfo
        import psutil

        mem = psutil.virtual_memory()
        
        # Conversão de bytes para gigabytes
        total_gb = mem.total / (1024 ** 3)
        available_gb = mem.available / (1024 ** 3)
        used_percent = mem.percent

        # Frequência e tipo (DDR4, etc) não são expostos pelo psutil e requerem
        # dmidecode (Linux), WMI (Windows) ou system_profiler (macOS).
        # Vamos usar valores genéricos para não falhar sem privilégios ou bibliotecas pesadas.
        
        return RAMInfo(
            total_gb=round(total_gb, 2),
            available_gb=round(available_gb, 2),
            used_percent=used_percent,
            ram_type="Unknown",
            freq_mhz=None
        )
    ```
  </action>
  <acceptance_criteria>
    - `SystemDetector.get_ram_info()` retorna uma instância de `RAMInfo`
    - Valores de `total_gb` e `available_gb` estão corretos (arredondados para 2 casas)
  </acceptance_criteria>
</task>
```

## Must-Haves
- [ ] O cálculo de bytes para GB deve ser preciso (`1024 ** 3`).
