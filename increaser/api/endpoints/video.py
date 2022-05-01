from fastapi import APIRouter

from dtypes import IncreaseAlgorithm
from video import VideoReader, VideoWriter
from processors import double_frame_rate
from schemas import Video
from utils import write_bytes, read_bytes


router = APIRouter()


@router.post("/double_fps", response_model=Video, status_code=200)
def double_fps(video: Video, algorithm: IncreaseAlgorithm):
    filepath = write_bytes(video.content, video.filename)

    reader = VideoReader(filepath)
    writer = VideoWriter(filepath, *reader.frame_size, reader.fps * 2, reader.codec)

    frame_generator = double_frame_rate(reader, algorithm)
    writer.write_from_generator(frame_generator)

    del reader
    del writer

    return {"filename": video.filename, "content": read_bytes(video.filename)}
