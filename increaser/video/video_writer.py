import logging

from pathlib import Path
from uuid import uuid4

import numpy as np
import cv2

from dtypes import FrameGenerator


class VideoWriter:
    def __init__(self, filepath: Path, width: int, height: int, fps: int):
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.__filename = str(uuid4()) + ".mp4"
        self.__writer = cv2.VideoWriter(
            self.__get_new_path(filepath), fourcc, fps, (width, height)
        )

    def __del__(self):
        self.__writer.release()
        self._logger.info(f"Video {self.__filename} was saved on disk")

    @property
    def filename(self):
        return self.__filename

    def write_from_generator(self, frames: FrameGenerator) -> None:
        for frame in frames:
            self.write_frame(frame)

    def write_frame(self, frame: np.ndarray) -> None:
        self.__writer.write(frame)

    def __get_new_path(self, old_path: Path) -> str:
        dir = old_path.parent
        return str(Path(dir, self.__filename))

    _logger = logging.getLogger("video_writer")
