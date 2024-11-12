from fastapi import APIRouter

from lmos_database.actions.apikey import (
    create_api_key as create_api_key_action,
    get_api_keys_by_user as get_api_keys_by_user_action,
    delete_api_key_by_hash as delete_api_key_by_hash_action,
    disable_api_key_by_hash as disable_api_key_by_hash_action,
)

router = APIRouter(tags=["Router"])

@router.put("/apikey/create")
async def create_api_key(api_key: str, user_id: int):
    return await create_api_key_action(api_key, user_id)

@router.get("/apikey/get")
async def get_api_keys_by_user(user_id: int):
    return await get_api_keys_by_user_action(user_id)

@router.delete("/apikey/delete")
async def delete_api_key_by_hash(api_key_hash: str):
    return await delete_api_key_by_hash_action(api_key_hash)

@router.delete("/apikey/disable")
async def disable_api_key_by_hash(api_key_hash: str):
    return await disable_api_key_by_hash_action(api_key_hash)