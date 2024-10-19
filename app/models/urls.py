from sqlalchemy import Column, String

from app.core.db import Base


class ShortUrl(Base):
    url = Column(String(256), unique=True, nullable=False)
    short = Column(String, unique=True)
