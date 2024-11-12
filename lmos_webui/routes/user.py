from fastapi import APIRouter

from lmos_database.actions.user import (
    create_user as create_user_action,
    get_user_by_username as get_user_by_username_action,
    get_user_by_email as get_user_by_email_action,
    get_user_by_id as get_user_by_id_action,
    get_all_users as get_all_users_action,
    delete_user_by_id as delete_user_by_id_action,
    delete_user_by_username as delete_user_by_username_action,
)

router = APIRouter(tags=["User"])

@router.post("/create", response_model=dict)
async def create_user(user: dict):
    return await create_user_action(user)

@router.get("/get/by/username", response_model=dict)
async def get_user_by_username(username: str):
    return await get_user_by_username_action(username)

@router.get("/get/by/email", response_model=dict)
async def get_user_by_email(email: str):
    return await get_user_by_email_action(email)

@router.get("/get/by/id", response_model=dict)
async def get_user_by_id(user_id: int):
    return await get_user_by_id_action(user_id)

@router.get("/get/all", response_model=dict)
async def get_all_users():
    return await get_all_users_action()

@router.delete("/delete/by/id", response_model=dict)
async def delete_user_by_id(user_id: int):
    return await delete_user_by_id_action(user_id)

@router.delete("/delete/by/username", response_model=dict)
async def delete_user_by_username(username: str):
    return await delete_user_by_username_action(username)