from pathlib import Path


root = Path("./tmp")
root.mkdir(parents=True, exist_ok=True)


def write_bytes(content: bytes, filename: str) -> Path:
    filepath = root / filename
    with open(filepath, "wb") as f:
        f.write(content)

    return filepath


def read_bytes(filename: str) -> bytes:
    with open(root / filename, "rb") as f:
        return f.read()
