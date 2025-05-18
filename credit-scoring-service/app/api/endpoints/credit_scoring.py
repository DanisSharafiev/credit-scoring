from fastapi import APIRouter, Depends, Request, HTTPException
from app.schema.prediction import PredictionRequest, PredictionResponse
from models.inference import model
import json
import pandas as pd

router = APIRouter(prefix="/api", tags=["credit-scoring"])

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.post("/credit-score", response_model=PredictionResponse)
async def predict_credit_score(
    request: PredictionRequest,
    req: Request):
    try:
        req.app.state.logger.info(f"Received request: {request.model_dump_json()}")
        json_data = json.loads(request.model_dump_json())
        X = pd.DataFrame({"Interest_Rate": [json_data["interest_rate"]], "Outstanding_Debt": [json_data["outstanding_debt"]]})
        req.app.state.logger.info(f"Data for prediction: {X}")
        prediction = "Good" if int(model.predict(X)[0]) else "Bad"
        req.app.state.logger.info(f"Prediction result: {prediction}")
        response = PredictionResponse(credit_score=prediction)
        req.app.state.logger.info(f"Prediction response: {response.model_dump_json()}")
    except Exception as e:
        req.app.state.logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return response
