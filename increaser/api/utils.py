import base64

import numpy as np
import cv2


def encode_frame(frame: np.ndarray) -> str:
    return base64.b64encode(cv2.imencode(".jpg", frame)[1]).decode()


def decode_frame(frame_bytestring: str) -> np.ndarray:
    frame_bytes = base64.decodebytes(bytes(frame_bytestring, "utf-8"))
    return cv2.imdecode(np.frombuffer(frame_bytes, np.uint8), -1)


def encode_video(video: bytes) -> str:
    return base64.b64encode(video).decode()


def decode_video(video_string: str) -> bytes:
    return base64.decodebytes(bytes(video_string, "utf-8"))
