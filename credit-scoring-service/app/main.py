from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.logging import setup_logging
from app.core.middleware import setup_middleware
from app.api.endpoints.credit_scoring import router as credit_scoring_router

app = FastAPI()

app.include_router(router=credit_scoring_router)

@asynccontextmanager
def lifespan():
    app.state.logger = setup_logging()
    app.state.logger.info("Starting up...")
    setup_middleware(app)
    yield
    app.state.logger.info("Shutting down...")
    pass