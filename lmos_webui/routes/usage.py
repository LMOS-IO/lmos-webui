from fastapi import APIRouter

from lmos_database.actions.usage import (
    # create_llm_usage as create_llm_usage_action,
    get_usage_by_api_key as get_usage_by_api_key_action,
    # create_stt_usage as create_stt_usage_action,
    # create_bulk_usage as create_bulk_usage_action,
    get_usage_by_model_and_api_key as get_usage_by_model_and_api_key_action,
    get_usage_by_model as get_usage_by_model_action,
    # create_reranker_usage as create_reranker_usage_action,
    # create_tts_usage as create_tts_usage_action,
)

router = APIRouter(tags=["usage"])


@router.get("/usage/get/llm")
async def get_usage_by_api_key(api_key: str):
    return await get_usage_by_api_key_action(api_key)


@router.get("/usage/get/stt")
async def get_usage_by_model_and_api_key(model: str, api_key: str):
    return await get_usage_by_model_and_api_key_action(model, api_key)


@router.get("/usage/get/bulk")
async def get_usage_by_model(model: str):
    return await get_usage_by_model_action(model)
