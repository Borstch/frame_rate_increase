from pathlib import Path

import numpy as np
import cv2

from dtypes import FrameGenerator


class VideoWriter:
    def __init__(self, filepath: Path, width: int, height: int, fps: int, codec: int):
        self.__writer = cv2.VideoWriter(filepath, codec, fps, (width, height))

    def __del__(self):
        self.__writer.release()

    def write_from_generator(self, frames: FrameGenerator) -> None:
        for frame in frames:
            self.write_frame(frame)

    def write_frame(self, frame: np.ndarray) -> None:
        self.__writer.write(frame)
