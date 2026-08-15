from pathlib import Path

import logging

logger = logging.getLogger(__name__)


BASE_DIR = Path(__file__).resolve().parent.parent

DOWNLOAD_DIR = BASE_DIR / "downloads"

CLEAR_DOWNLOAD_DIR = True

DOWNLOAD_DIR.mkdir(exist_ok=True)

if CLEAR_DOWNLOAD_DIR:

    logger.info(f'Limpando a pasta downloads: {DOWNLOAD_DIR}')
    
    for item in DOWNLOAD_DIR.iterdir():
        if item.is_file():
            item.unlink()