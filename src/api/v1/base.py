import datetime
import sys

from fastapi import APIRouter, Depends
from sqlalchemy import exc
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from starlette import status

from src.api.v1 import file_storage
from src.config.logger import logger
from src.db.db import get_session

api_router = APIRouter()
api_router.include_router(file_storage.storage_router)


@api_router.get('/', status_code=status.HTTP_200_OK)
async def root_handler():
    return {'version': 'v1'}


@api_router.get('/ping', status_code=status.HTTP_200_OK)
async def ping(db: Session = Depends(get_session)):
    logger.info('Test ping.')
    response = {
        'api': 'v1',
        'python': sys.version_info,
    }
    response = await ping_db(db, response)

    return response


async def ping_db(db, response):
    logger.info('Test ping dependent services.')
    statement = text('SELECT version();')
    start = datetime.datetime.now()
    try:
        await db.execute(statement)
        ping_db_time = datetime.datetime.now() - start
        response = response | {'db': ping_db_time}
    # TODO Заменить Exception на на ошибки драйвера asyncpg.exception
    except (exc.SQLAlchemyError, Exception) as err:
        response = response | {'db': err.message}
    return response
