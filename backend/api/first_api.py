from fastapi import APIRouter, Depends
from typing import Union
from schemas.first_api import Item

router = APIRouter()

# 依赖函数


def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
# 前置依赖注入


@router.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


async def after_request():
    print("after dependence")
    pass


@router.get("/items/", response_model=dict)
async def read_items_after(request: dict = Depends(after_request)):
    return {"message": "items returns success"}
