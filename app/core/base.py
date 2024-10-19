"""
Файл коннектор, для добавление моделей в зону
видимости Alembic. При масштабировании проекта,
избавляет от кучи лишних импортов в env.py.
"""

from app.core.db import Base  # noqa
from app.models.urls import ShortUrl  # noqa
