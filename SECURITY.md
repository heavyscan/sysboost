# Security Policy

## Reporting Vulnerabilities

**Do not open public issues for security vulnerabilities.**

Report security issues by email or via GitHub's private security advisory feature.

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact

We will respond within 48 hours.

## Security Notes

- SysBoost requires elevated privileges for some operations (system-level tuning)
- All optimizations are documented and fully reversible via the built-in revert system
- SysBoost never collects or transmits user data
- All changes are logged locally in `~/.sysboost/history.json`
