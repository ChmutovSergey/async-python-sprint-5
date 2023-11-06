from fastapi import APIRouter

from src.schemas.user import UserRead, UserCreate, UserUpdate
from src.services.user_manager import fastapi_users_router, auth_backend

api_auth_router = APIRouter()

# auth/jwt/login
# auth/jwt/logout
api_auth_router.include_router(
    fastapi_users_router.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

# auth/registet
api_auth_router.include_router(
    fastapi_users_router.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# auth/forgot-password
# auth/reset-password
api_auth_router.include_router(
    fastapi_users_router.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

# auth/request-verify-token
# auth/verify
api_auth_router.include_router(
    fastapi_users_router.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

# user/
api_auth_router.include_router(
    fastapi_users_router.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
