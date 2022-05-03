from typing import List, Optional

import numpy as np
from skimage.transform import radon, iradon


class Interpolator:
    @staticmethod
    def linear(
        im0: np.ndarray, im1: np.ndarray, alpha: Optional[float] = 0.5
    ) -> np.ndarray:
        return (alpha * im1.astype(float) + (1 - alpha) * im0.astype(float)).astype(
            np.uint8
        )

    @classmethod
    def radon(
        cls, im0: np.ndarray, im1: np.ndarray, alpha: Optional[float] = 0.5
    ) -> np.ndarray:
        im0_channels = cls.__split_channels(im0)
        im1_channels = cls.__split_channels(im1)

        average_channels = [
            cls.__radon_transform(im0, im1, alpha)
            for im0, im1 in zip(im0_channels, im1_channels)
        ]
        return np.dstack(average_channels).astype(np.uint8)

    @staticmethod
    def __split_channels(image: np.ndarray) -> List[np.ndarray]:
        if len(image.shape) == 2:
            image = image[:, :, None]

        _, _, n_channels = image.shape
        return [image[:, :, channel] for channel in range(n_channels)]

    @staticmethod
    def __radon_transform(im0: np.ndarray, im1: np.ndarray, alpha: float) -> np.ndarray:
        theta = np.linspace(0, 180, max(im1.shape), endpoint=False)

        im0_hat = radon(im0.astype(float), theta=theta, circle=False)
        im1_hat = radon(im1.astype(float), theta=theta, circle=False)

        average = alpha * im1_hat + (1 - alpha) * im0_hat
        return iradon(average, theta=theta, circle=False, filter_name="ramp")
