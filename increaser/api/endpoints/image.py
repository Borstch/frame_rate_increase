import logging

from fastapi import APIRouter, HTTPException

from dtypes import IncreaseAlgorithm
from processors import get_algorithm
from schemas import InterpolationData
from api.utils import encode_frame, decode_frame


router = APIRouter()
logger = logging.getLogger("image_processor")


@router.post("/between", response_model=str, status_code=200)
def interpolate_frame_in_between(data: InterpolationData):
    frame_before = decode_frame(data.frame_before)
    frame_after = decode_frame(data.frame_after)

    logger.info(f"Image interpolation started with algorithm {data.algorithm}")
    try:
        interpolated = get_algorithm(data.algorithm)(frame_before, frame_after)
        return encode_frame(interpolated)
    except KeyError:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid interpolation algorithm given: {data.algorithm}",
        )
    logger.info("Done interpolationg.")
