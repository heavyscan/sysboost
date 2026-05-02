#!/usr/bin/env python3
"""SysBoost entry point."""
import sys
import os

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    from src.core.logger import setup_logging
    import logging

    logger = setup_logging(level=logging.INFO)
    logger.info("Starting SysBoost v0.1.0")

    try:
        from src.ui.app import App
        app = App()
        app.mainloop()
    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        logger.error("Run: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Fatal error on startup: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
