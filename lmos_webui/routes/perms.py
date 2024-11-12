from fastapi import APIRouter

from lmos_database.actions.permissions import (
    grant_model_access as grant_model_access_action,
    revoke_model_access as revoke_model_access_action,
    get_api_permissions as get_api_permissions_action,
)

router = APIRouter(tags=["Permissions"])


@router.put("/perms/grant")
async def grant_model_access(model_name: str, user_id: int):
    """
    this endpoint will grant access to a model to a user
    """
    return await grant_model_access_action(model_name, user_id)


@router.put("/perms/revoke")
async def revoke_model_access(model_name: str, user_id: int):
    """
    this endpoint will revoke access to a model from a user
    """
    return await revoke_model_access_action(model_name, user_id)


@router.get("/perms/get")
async def get_api_permissions(api_key: str):
    """
    this endpoint will return the permissions for a given api key
    """
    return await get_api_permissions_action(api_key)
