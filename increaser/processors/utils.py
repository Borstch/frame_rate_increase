from increaser.dtypes import FrameGenerator, IncreaseAlgorithm
from increaser.video import VideoReader
from algorithms import mean_interpolation


_ALGORITHMS = {IncreaseAlgorithm.mean: mean_interpolation}


def double_frame_rate(
    reader: VideoReader, algorithm: IncreaseAlgorithm
) -> FrameGenerator:
    prev_frame = None
    for frame in reader:
        if prev_frame is not None:
            yield _ALGORITHMS[algorithm](prev_frame, frame)

        prev_frame = frame
        yield frame
