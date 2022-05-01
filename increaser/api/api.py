from fastapi import APIRouter

from api.endpoints import image, video

router = APIRouter()

router.include_router(image.router, prefix="/image", tags=["image"])
router.include_router(video.router, prefix="/video", tags=["video"])
