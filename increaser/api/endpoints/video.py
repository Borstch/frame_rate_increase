from fastapi import APIRouter

from dtypes import IncreaseAlgorithm
from video import VideoReader, VideoWriter
from processors import double_frame_rate
from schemas import Video
from utils import write_bytes, read_bytes
from api.utils import encode_video, decode_video


router = APIRouter()


@router.post("/double_fps", response_model=Video, status_code=200)
def double_fps(video: Video, algorithm: IncreaseAlgorithm):
    video_bytes = decode_video(video.content)
    filepath = write_bytes(video_bytes, video.filename)

    reader = VideoReader(filepath)
    writer = VideoWriter(filepath, *reader.frame_size, reader.fps * 2)

    frame_generator = double_frame_rate(reader, algorithm)
    writer.write_from_generator(frame_generator)
    new_filename = writer.filename

    del reader
    del writer

    return {"filename": new_filename, "content": encode_video(read_bytes(new_filename))}
