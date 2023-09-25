from fastapi import FastAPI

from app.const import (
    OPENAPI_DESCRIPTION,
    OPENAPI_TITLE,
)
from app.routers import (
    auth,
    products,
)
from app.version import __version__


app = FastAPI(
    title=OPENAPI_TITLE,
    description=OPENAPI_DESCRIPTION,
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(auth.router)
app.include_router(products.router)
