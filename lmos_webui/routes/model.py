from fastapi import APIRouter

from lmos_database.actions.model import (
    create_model as create_model_action,
    get_model_by_name as get_model_by_name_action,
    get_model_by_id as get_model_by_id_action,
    get_all_models as get_all_models_action,
    delete_model_by_id as delete_model_by_id_action,
    delete_model_by_name as delete_model_by_name_action,
)

router = APIRouter(tags=["Model"])


@router.post("/model/create")
async def create_model(model: dict):
    """
    this endpoint will create a new model
    """
    return await create_model_action(model)


@router.get("/model/get/by/name")
async def get_model_by_name(model_name: str):
    """
    this endpoint will return a model by name
    """
    return await get_model_by_name_action(model_name)


@router.get("/model/get/by/id")
async def get_model_by_id(model_id: int):
    """
    this endpoint will return a model by id
    """
    return await get_model_by_id_action(model_id)


@router.get("/model/get/all")
async def get_all_models():
    """
    this endpoint will list all models in the database

    WARNING: this is not the same as the models in the router
    """
    return await get_all_models_action()


@router.delete("/model/delete/by/id")
async def delete_model_by_id(model_id: int):
    """
    this endpoint will delete a model by id
    """
    return await delete_model_by_id_action(model_id)


@router.delete("/model/delete/by/name")
async def delete_model_by_name(model_name: str):
    """
    this endpoint will delete a model by name
    """
    return await delete_model_by_name_action(model_name)
