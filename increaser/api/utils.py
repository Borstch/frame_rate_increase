import base64

import numpy as np
import cv2


def encode_frame(frame: np.ndarray) -> str:
    return base64.b64encode(cv2.imencode(".jpg", frame)[1]).decode()


def decode_frame(frame_bytestring: str) -> np.ndarray:
    frame_bytes = base64.decodebytes(bytes(frame_bytestring, "utf-8"))
    return cv2.imdecode(np.frombuffer(frame_bytes, np.uint8), -1)
