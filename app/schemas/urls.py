from pydantic import BaseModel, Field, HttpUrl


class ShortUrlCreate(BaseModel):
    url: HttpUrl = Field(..., max_length=256, example="https://example.com")

    class Config:
        from_attributes = True
        extra = "forbid"
        json_schema_extra = {"example": {"url": "https://example.com"}}


class OriginUrlGet(BaseModel):
    url: HttpUrl | None = Field(
        None, max_length=256, example="https://example.com"
    )
    short: str = Field(..., example="abc123")

    class Config:
        from_attributes = True
        extra = "ignore"
        json_schema_extra = {"example": {"short": "abc123"}}
