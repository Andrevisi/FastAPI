from asyncio import gather
from fastapi import APIRouter, HTTPException
from typing import List

from services import *
from schemas import *

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutoput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
    
@user_router.delete('/delete/{user_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutoput}})
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
    
@user_router.post('/favorite/add', response_model=StandardOutput, responses={400: {'model': ErrorOutoput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
    
@user_router.delete('/favorite/remove/{user_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutoput}})
async def user_favorite_remove(user_id: int, symbol: str):
    try:
        await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
    
@user_router.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutoput}})
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
    
@assets_router.get('/day_summary/{user_id}', response_model=List[DaySummaryOutput], responses={400: {'model': ErrorOutoput}})
async def day_summary(user_id: int):
    try:
        user = await UserService.get_by_id(user_id)
        favorites_symbols = [favorite.symbol for favorite in user.favorites]
        tasks = [AssetService.day_summary(symbol=symbol) for symbol in favorites_symbols]
        return await gather(*tasks)

        # response = []
        # for symbol in favorites_symbols:
        #     result = await AssetService.day_summary(symbol=symbol)
        #     response.append(result)

    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))