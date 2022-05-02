import logging
from pathlib import Path

logger = logging.getLogger("io")


root = Path("./tmp")
root.mkdir(parents=True, exist_ok=True)
logger.debug("Root directory for storing videos initialized")


def write_bytes(content: bytes, filename: str) -> Path:
    filepath = root / filename
    with open(filepath, "wb") as f:
        f.write(content)

    logger.info(f"{len(content)} bytes was written into {filepath}")
    return filepath


def read_bytes(filename: str) -> bytes:
    with open(root / filename, "rb") as f:
        return f.read()
