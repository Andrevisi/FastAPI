from fastapi import APIRouter
from services import UserService
from schemas import UserCreateInput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create')
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
    except:
        pass