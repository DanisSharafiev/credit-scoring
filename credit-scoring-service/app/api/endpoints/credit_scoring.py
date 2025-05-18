from fastapi import APIRouter, Depends
from app.schema.prediction import PredictionRequest, PredictionResponse

router = APIRouter(prefix="/api/", tags=["credit-scoring"])

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.post("/credit-score")
async def predict_credit_score(
    request: PredictionRequest,
    response_model=PredictionResponse):
    pass
