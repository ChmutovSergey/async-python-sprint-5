import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import auth, base
from config.config import settings
from config.logger import logger

app = FastAPI(
    title=settings.project_name,
    default_response_class=ORJSONResponse,
)

app.include_router(auth.api_auth_router)
app.include_router(base.api_router, prefix='/api/v1')

if __name__ == '__main__':
    logger.info('Server started.')
    uvicorn.run(
        'main:app',
        host=settings.api.host,
        port=settings.api.port,
    )
