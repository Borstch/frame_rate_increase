from typing import Sequence

import numpy as np
from scipy.spatial.distance import jaccard


def msjd(interpolated: Sequence[np.ndarray], real: np.ndarray) -> float:
	distances = [jaccard(y_hat.flatten(), y.flatten()) for y_hat, y in zip(interpolated, real)]
	return np.mean(distances)
