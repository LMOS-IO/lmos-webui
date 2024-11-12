from lmos_config import config
from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes import router


@asynccontextmanager
async def lifespan(app):
    # await config.load_config_data()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)
