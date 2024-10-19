from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse

from app.core.db import AsyncSession, get_async_session
from app.crud.urls import create_url_map, get_original_by_short
from app.schemas.urls import OriginUrlGet, ShortUrlCreate

router = APIRouter()


@router.post(
    "/",
    response_model=OriginUrlGet,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_unset=True,
)
async def create_short_url(
    url_create: ShortUrlCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_short = await create_url_map(url_create, session)
    return new_short


@router.get("/{short}")
async def redirect_to_original(
    short: str, session: AsyncSession = Depends(get_async_session)
):
    original_url = await get_original_by_short(short, session)
    return RedirectResponse(
        url=original_url,
        status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    )
