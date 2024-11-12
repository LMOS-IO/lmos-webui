from fastapi import APIRouter

from lmos_database.actions.rate_limit import (
    # record_ratelimit_usage as record_ratelimit_usage_action,
    get_current_limits as get_current_limits_action,
)

router = APIRouter(tags=["Rate Limit"])


@router.get("/ratelimit/get")
async def get_current_limits(api_key: str, ip: str, model: str):
    return await get_current_limits_action(api_key, ip, model)
