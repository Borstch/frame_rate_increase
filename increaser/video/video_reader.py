from pathlib import Path

import cv2

from increaser.dtypes import FrameGenerator


class VideoReader:
    def __init__(self, filepath: Path):
        self.__reader = self.__init_reader(filepath)

    def __del__(self):
        self.__reader.release()

    def __iter__(self) -> FrameGenerator:
        while True:
            ret, frame = self.__reader.read()
            if not ret:
                break

            yield frame

    @property
    def fps(self) -> int:
        return int(self.__reader.get(cv2.CAP_PROP_FPS))

    @property
    def codec(self) -> int:
        return self.__reader.get(cv2.CAP_PROP_FOURCC)

    @property
    def frame_size(self) -> tuple[int, int]:
        width = int(self.__reader.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.__reader.get(cv2.cv.CAP_PROP_FRAME_HEIGHT))
        return width, height

    @staticmethod
    def __init_reader(filepath: Path) -> cv2.VideoCapture:
        try:
            return cv2.VideoCapture(filepath)
        except:
            raise RuntimeError(f"Unable to read frames from file {filepath}")
