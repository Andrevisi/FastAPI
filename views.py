from fastapi import APIRouter

from services import UserService
from schemas import UserCreateInput, StandardOutput, AlternativeOutput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', response_model=StandardOutput, responses={418: {'model': AlternativeOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message='User created')
    except:
        pass