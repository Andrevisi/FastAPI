from fastapi import APIRouter, HTTPException

from services import UserService
from schemas import UserCreateInput, StandardOutput, ErrorOutoput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutoput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message='User created')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))