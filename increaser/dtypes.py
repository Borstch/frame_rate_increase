from enum import Enum
from typing import Generator

import numpy as np


FrameGenerator = Generator[np.ndarray, None, None]


class IncreaseAlgorithm(Enum, int):
    mean = 0
