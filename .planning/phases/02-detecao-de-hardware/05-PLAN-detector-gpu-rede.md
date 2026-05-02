---
id: "2.5"
phase: 2
wave: 1
title: "Detector de GPU e Rede"
depends_on: ["2.1"]
files_modified:
  - "src/core/detector.py"
autonomous: true
requirements:
  - RF-01
---

# Plano 2.5 — Detector de GPU e Rede

## Objetivo

Finalizar o módulo de detecção inventariando a Placa de Vídeo (GPU) e adaptadores de Rede do sistema, agrupando todos os métodos na geração de um `HardwareProfile` completo.

## Tarefas

### Task 1 — Implementar GPU e Rede

```xml
<task id="2.5.1">
  <title>Implementar detectores de GPU e Rede, mais função agrupadora get_profile</title>
  <read_first>
    - src/core/types.py (HardwareProfile, GPUInfo, NetworkInfo)
    - src/core/detector.py (SystemDetector atual)
  </read_first>
  <action>
    Atualizar `src/core/detector.py`, adicionando `get_gpus_info`, `get_network_info` e `get_profile` à classe `SystemDetector`:

    ```python
    @staticmethod
    def get_gpus_info() -> list['GPUInfo']:
        """Coleta informações básicas sobre GPUs."""
        from .types import GPUInfo
        # Como py-cpuinfo/psutil não lidam bem com GPU sem drivers específicos (ex: pynvml),
        # por enquanto retornamos mock ou dependemos de chamadas ao SO em fases futuras.
        # Implementação "best effort"
        return [GPUInfo(model="Generic Display Adapter", vendor="Unknown", vram_mb=None)]

    @staticmethod
    def get_network_info() -> 'NetworkInfo':
        """Coleta informações dos adaptadores de rede."""
        from .types import NetworkInfo
        import psutil
        
        adapters = list(psutil.net_if_stats().keys())
        # Filtramos loopback
        adapters = [a for a in adapters if not a.startswith('lo')]
        
        return NetworkInfo(
            adapters=adapters,
            connection_type="Ethernet/WiFi"
        )

    @classmethod
    def get_profile(cls) -> 'HardwareProfile':
        """Retorna o perfil de hardware completo agrupado."""
        from .types import HardwareProfile
        
        return HardwareProfile(
            os_name=cls.get_os_type(),
            os_version=cls.get_os_version(),
            architecture=cls.get_architecture(),
            cpu=cls.get_cpu_info(),
            ram=cls.get_ram_info(),
            disks=cls.get_disks_info(),
            gpus=cls.get_gpus_info(),
            network=cls.get_network_info(),
            is_elevated=cls.is_elevated()
        )
    ```
  </action>
  <acceptance_criteria>
    - `SystemDetector.get_profile()` retorna uma instância válida de `HardwareProfile` contendo todos os sub-itens
    - Métodos para rede e GPU são chamáveis de forma independente
  </acceptance_criteria>
</task>
```

## Must-Haves
- [ ] O método `get_profile` deve encapsular todos os métodos anteriores de forma segura, garantindo que se um falhar, o profile seja montado com valores defaut/fallback.
