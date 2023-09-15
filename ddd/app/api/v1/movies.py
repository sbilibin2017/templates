from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Request

router = APIRouter()


@router.get("/")
@inject
async def root():
    return {"message": "Hello  World"}
