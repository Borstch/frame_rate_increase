from pathlib import Path


root = Path("./tmp")


def write_bytes(content: bytes, filename: str) -> None:
    with open(root / filename, "wb") as f:
        f.write(content)


def read_bytes(filename: str) -> bytes:
    with open(root / filename, "rb") as f:
        return f.read()
