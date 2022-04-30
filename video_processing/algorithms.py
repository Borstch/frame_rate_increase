import numpy as np


def mean_interpolation(first_frame: np.ndarray, second_frame: np.ndarray) -> np.ndarray:
    return np.mean([first_frame, second_frame])
