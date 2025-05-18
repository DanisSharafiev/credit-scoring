from fastapi import APIRouter, Depends, Request, HTTPException
from app.schema.prediction import PredictionRequest, PredictionResponse
from models.inference import model

router = APIRouter(prefix="/api/", tags=["credit-scoring"])

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.post("/credit-score", response_model=PredictionResponse)
async def predict_credit_score(
    request: PredictionRequest,
    req: Request):
    try:
        req.app.state.logger.info(f"Received request: {request.model_dump_json()}")
        json_data = request.model_dump_json()
        X = [json_data["interest_rate"], json_data["outstanding_debt"]]
        req.app.state.logger.info(f"Data for prediction: {X}")
        response = PredictionResponse("Good" if int(model.predict(X)[0]) else "Bad")
        req.app.state.logger.info(f"Prediction response: {response.model_dump_json()}")
    except Exception as e:
        req.app.state.logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return response
