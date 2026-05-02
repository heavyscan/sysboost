---
id: "2.6"
phase: 2
wave: 2
title: "Motor de Score: cálculo de saúde e otimização"
depends_on: ["2.5"]
files_modified:
  - "src/core/optimizer.py"
  - "src/core/detector.py"
autonomous: true
requirements:
  - RF-02
---

# Plano 2.6 — Motor de Score

## Objetivo

Implementar a base do cálculo do "Health Score" da máquina (0-100) com sub-categorias. Como as otimizações reais virão nas fases 4 a 6, o motor será um esqueleto que avalia condições base do hardware (ex: SSD vs HDD, RAM disponível) para pontuação inicial, projetado para ser estendido mais tarde.

## Tarefas

### Task 1 — Implementar Engine de Score Base

```xml
<task id="2.6.1">
  <title>Criar motor de avaliação de saúde no optimizer.py</title>
  <read_first>
    - src/core/types.py (HealthScore, HardwareProfile)
    - src/core/detector.py (SystemDetector.get_profile)
    - src/core/optimizer.py (stub)
  </read_first>
  <action>
    Atualizar/Criar `src/core/optimizer.py`:

    ```python
    """Motor central de otimizações e cálculo de score."""
    from .types import HardwareProfile, HealthScore, DiskType
    from .logger import get_logger

    logger = get_logger("optimizer.score")

    class ScoreEngine:
        """Calcula o Health Score do sistema baseado no Hardware e Estado."""

        @staticmethod
        def calculate_score(profile: 'HardwareProfile') -> 'HealthScore':
            """Calcula a pontuação atual baseada no profile."""
            cpu_score = ScoreEngine._score_cpu(profile)
            ram_score = ScoreEngine._score_ram(profile)
            disk_score = ScoreEngine._score_disk(profile)
            net_score = 50  # Base fixa, requer testes reais para melhorar
            services_score = 50  # Base fixa até termos o módulo de serviços
            
            # Média ponderada simplificada
            overall = int((cpu_score * 0.3) + (ram_score * 0.3) + (disk_score * 0.2) + (net_score * 0.1) + (services_score * 0.1))
            
            return HealthScore(
                overall=min(max(overall, 0), 100),
                cpu=cpu_score,
                ram=ram_score,
                disk=disk_score,
                network=net_score,
                services=services_score
            )

        @staticmethod
        def _score_cpu(profile: 'HardwareProfile') -> int:
            score = 50
            if profile.cpu.physical_cores >= 8:
                score += 30
            elif profile.cpu.physical_cores >= 4:
                score += 15
            if profile.cpu.base_freq_mhz > 3000:
                score += 20
            return min(score, 100)

        @staticmethod
        def _score_ram(profile: 'HardwareProfile') -> int:
            score = 40
            if profile.ram.total_gb >= 16:
                score += 40
            elif profile.ram.total_gb >= 8:
                score += 20
            
            if profile.ram.used_percent < 50:
                score += 20
            elif profile.ram.used_percent > 85:
                score -= 20
                
            return min(max(score, 0), 100)

        @staticmethod
        def _score_disk(profile: 'HardwareProfile') -> int:
            if not profile.disks:
                return 50
                
            # Pontua baseado no disco do sistema (assumindo o primeiro)
            main_disk = profile.disks[0]
            if main_disk.disk_type == DiskType.NVME:
                return 95
            elif main_disk.disk_type == DiskType.SSD:
                return 80
            else:
                return 40
    ```
  </action>
  <acceptance_criteria>
    - `src/core/optimizer.py` contém classe `ScoreEngine`
    - Método `calculate_score` retorna um `HealthScore` com valores 0-100
  </acceptance_criteria>
</task>
```

## Must-Haves
- [ ] Pontuações devem sempre ser fixadas no limite seguro de `0` a `100`.
