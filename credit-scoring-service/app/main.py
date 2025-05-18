from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.logging import setup_logging
from app.core.middleware import setup_middleware
from app.api.endpoints.credit_scoring import router as credit_scoring_router
from fastapi.openapi.utils import get_openapi

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.logger = setup_logging()
    app.state.logger.info("Starting up...")
    yield
    app.state.logger.info("Shutting down...")
    pass

app = FastAPI(lifespan=lifespan)

setup_middleware(app)

app.include_router(router=credit_scoring_router)

@app.get("/openapi.json", include_in_schema=False)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Credit Scoring API",
        version="1.0.0",
        description="API for predicting credit scores",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema