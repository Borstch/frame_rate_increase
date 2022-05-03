from dtypes import FrameGenerator, Increaser, IncreaseAlgorithm
from video import VideoReader
from .algorithms import Interpolator


_ALGORITHMS = {
    IncreaseAlgorithm.Linear: Interpolator.linear,
    IncreaseAlgorithm.Radon: Interpolator.radon,
}


def get_algorithm(algorithm: IncreaseAlgorithm) -> Increaser:
    return _ALGORITHMS[algorithm]


def double_frame_rate(
    reader: VideoReader, algorithm: IncreaseAlgorithm
) -> FrameGenerator:
    prev_frame = None
    for frame in reader:
        if prev_frame is not None:
            yield get_algorithm(algorithm)(prev_frame, frame)

        prev_frame = frame
        yield frame
