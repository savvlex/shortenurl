from sqlite3 import IntegrityError

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.core.db import AsyncSession
from app.models.urls import ShortUrl
from app.schemas.urls import OriginUrlGet, ShortUrlCreate
from app.services.utils import generate_unique_short_link

URL_GENERATE_ATTEMPTS = 5
URL_GENERATION_FAILED = 'Failed to create url: max attempts reached. Try again'
NOT_FOUND_MESSAGE = "Data doesn't exist"


async def create_url_map(
    data: ShortUrlCreate, session: AsyncSession
) -> OriginUrlGet:
    """Creates a new short URL entry in the database with a unique short."""
    existing_url = await original_exists(str(data.url), session)

    if existing_url:
        return OriginUrlGet.model_validate(existing_url)

    for _ in range(URL_GENERATE_ATTEMPTS):
        try:
            short = generate_unique_short_link()
            new_db_object = ShortUrl(url=str(data.url), short=short)
            session.add(new_db_object)
            await session.commit()
            await session.refresh(new_db_object)

            return OriginUrlGet.model_validate(new_db_object)

        except IntegrityError:
            await session.rollback()

        except SQLAlchemyError as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error),
            )

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=URL_GENERATION_FAILED,
    )


async def get_original_by_short(data: str, session: AsyncSession) -> str:
    """Returns original link if ShortURL if map exists."""
    result = await session.execute(
        select(ShortUrl).where(ShortUrl.short == data)
    )
    db_object = result.scalars().first()
    if not db_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MESSAGE
        )
    return db_object.url


async def original_exists(data: str, session: AsyncSession) -> str:
    """Returns original url (str) if it exists."""
    result = await session.execute(
        select(ShortUrl).where(ShortUrl.url == data)
    )
    db_object = result.scalars().first()
    return db_object
