from fastapi import APIRouter

from .apikey import router as apikey_router
from .model import router as model_router
from .perms import router as perms_router
from .rate_limit import router as rate_limit_router
from .usage import router as usage_router
from .user import router as user_router

router = APIRouter(prefix="/api")

router.include_router(apikey_router)
router.include_router(model_router)
router.include_router(perms_router)
router.include_router(rate_limit_router)
router.include_router(usage_router)
router.include_router(user_router)
