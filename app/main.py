from fastapi import FastAPI

from app.core.config import settings
from app.routes.member import route_member

app = FastAPI(
    title=settings.PROJECT_TITLE,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
)

app.include_router(route_member)
