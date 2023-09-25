from enum import Enum
from typing import (
    Final,
    List,
)

VERSION_API: Final = "v1"

PRODUCTS_TAGS: Final[List[str | Enum] | None] = ["Products"]
PRODUCTS_URL: Final = VERSION_API + "/products"

AUTH_TAGS: Final[List[str | Enum] | None] = ["Authentication", "Login"]
AUTH_URL: Final = VERSION_API + "/auth/login"

TOKEN_TYPE: Final = "bearer"
TOKEN_EXPIRE_MINUTES: Final = 180

TOKEN_ALGORITHM: Final = "HS256"
OPENAPI_TITLE: Final = "API Catalogue Products"
OPENAPI_DESCRIPTION: Final = "Test API over Postgres database built with FastAPI."
