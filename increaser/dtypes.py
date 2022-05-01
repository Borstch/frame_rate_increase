from enum import Enum
from typing import Generator, Callable

import numpy as np


FrameGenerator = Generator[np.ndarray, None, None]
Increaser = Callable[[np.ndarray, np.ndarray], np.ndarray]


class IncreaseAlgorithm(str, Enum):
    Mean = "mean"
