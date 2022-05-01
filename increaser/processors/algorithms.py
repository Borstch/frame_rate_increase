import numpy as np


def mean_interpolation(first_frame: np.ndarray, second_frame: np.ndarray) -> np.ndarray:
    buffer = first_frame.astype(float) + second_frame.astype(float)
    return (buffer / 2).astype(np.uint8)
