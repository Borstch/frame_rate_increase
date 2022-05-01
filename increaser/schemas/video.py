from pydantic import BaseModel


class Video(BaseModel):
    filename: str
    content: bytes
