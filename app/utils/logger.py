"""
Centralized application logger.
"""

import logging
from pathlib import Path

from app.config.settings import get_settings


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger instance.
    """

    settings = get_settings()

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # File Handler
    log_dir = Path(settings.LOG_DIR)
    log_dir.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(
        log_dir / "app.log",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.propagate = False

    return logger