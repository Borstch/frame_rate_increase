from typing import Optional

from pydantic import BaseModel

from dtypes import IncreaseAlgorithm


class InterpolationData(BaseModel):
    frame_before: str
    frame_after: str
    algorithm: Optional[IncreaseAlgorithm] = IncreaseAlgorithm.Mean
