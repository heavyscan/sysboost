# Contributing to SysBoost

Thank you for wanting to contribute! 🎉

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR-USER/sysboost.git`
3. Set up the environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   # .venv\Scripts\activate    # Windows
   pip install -r requirements-dev.txt
   pip install -e .
   ```
4. Create a branch: `git checkout -b feature/my-feature`
5. Make changes and add tests
6. Verify: `ruff check src/ tests/ && pytest tests/unit/`
7. Commit: `git commit -m "feat: clear description of change"`
8. Push and open a Pull Request

## Contribution Types

- 🐛 **Bug fixes** — always welcome!
- ✨ **New optimizations** — use the plugin system or contribute to core
- 🌍 **Translations** — add files to `src/i18n/`
- 📚 **Documentation** — improve README or add wiki pages
- 🧪 **Tests** — increase coverage of core modules

## Adding a New Optimization (Plugin)

1. Create `plugins/my-optimization/__init__.py`
2. Extend `SysBoostPlugin` from `src/plugins/base.py`
3. Implement `apply()` with a full revert strategy
4. Add tests in `tests/unit/test_my_optimization.py`
5. Document the optimization in your PR description

## Commit Convention

We use [Conventional Commits](https://conventionalcommits.org):
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation only
- `test:` tests only
- `refactor:` code restructuring without behavior change
- `chore:` maintenance (deps, CI, etc.)

## Code Style

We use `ruff` for linting and formatting:

```bash
ruff check src/ tests/    # check
ruff format src/ tests/   # auto-fix formatting
```

## Reporting Bugs

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template.
Always include: OS, SysBoost version, steps to reproduce.
