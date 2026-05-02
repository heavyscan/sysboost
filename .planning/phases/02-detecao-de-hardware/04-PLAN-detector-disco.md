---
id: "2.4"
phase: 2
wave: 1
title: "Detector de Disco: partições, tipo e espaço"
depends_on: ["2.1"]
files_modified:
  - "src/core/detector.py"
autonomous: true
requirements:
  - RF-01
---

# Plano 2.4 — Detector de Disco

## Objetivo

Inventariar os discos e partições do sistema. Precisamos detectar o dispositivo, ponto de montagem, espaço total e espaço livre. Embora o tipo do disco (NVME, SSD, HDD) seja um requisito ideal, detectá-lo muitas vezes requer ferramentas que exigem privilégios elevados. Faremos o melhor esforço com APIs multiplataforma e fallbacks seguros.

## Tarefas

### Task 1 — Detecção de Discos via psutil

```xml
<task id="2.4.1">
  <title>Implementar detecção de partições e discos</title>
  <read_first>
    - src/core/types.py (classes DiskInfo, DiskType)
    - src/core/detector.py (SystemDetector atual)
  </read_first>
  <action>
    Atualizar `src/core/detector.py`, adicionando `get_disks_info` à classe `SystemDetector`:

    ```python
    @staticmethod
    def get_disks_info() -> list['DiskInfo']:
        """Coleta informações sobre os discos do sistema."""
        from .types import DiskInfo, DiskType
        import psutil

        disks = []
        try:
            partitions = psutil.disk_partitions(all=False)
        except Exception as e:
            logger.error(f"Falha ao ler partições: {e}")
            partitions = []

        for partition in partitions:
            # Pula partições virtuais, de loopback ou inacessíveis (como cdrom, snapfs)
            if partition.fstype == "" or "loop" in partition.device.lower():
                continue

            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # Partições de sistema ou protegidas
                continue
            except FileNotFoundError:
                # Pode acontecer no Windows se o driver sumir
                continue

            total_gb = usage.total / (1024 ** 3)
            free_gb = usage.free / (1024 ** 3)
            
            # Heurística basica para tipo de disco, olhando o nome do device (Linux focado)
            # Para Windows, WMI seria necessário para veracidade total
            disk_type = DiskType.UNKNOWN
            dev_lower = partition.device.lower()
            if "nvme" in dev_lower:
                disk_type = DiskType.NVME
            elif "sd" in dev_lower:  # /dev/sda, etc. Costuma ser SSD SATA ou HDD
                disk_type = DiskType.SSD  # Assumimos SSD como padrão moderno

            disks.append(DiskInfo(
                device=partition.device,
                mountpoint=partition.mountpoint,
                disk_type=disk_type,
                total_gb=round(total_gb, 2),
                free_gb=round(free_gb, 2),
                model="Unknown"
            ))

        return disks
    ```
  </action>
  <acceptance_criteria>
    - `SystemDetector.get_disks_info()` retorna uma lista de `DiskInfo` válida
    - Partições ignoram unidades inacessíveis (evitando crashes)
  </acceptance_criteria>
</task>
```

## Must-Haves
- [ ] Tratamento adequado de erros de `PermissionError` ao ler `disk_usage` de drives restritos.
