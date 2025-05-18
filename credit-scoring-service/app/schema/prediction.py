from pydantic import BaseModel, Field
from typing_extensions import Literal

class PredictionRequest(BaseModel):
    interest_rate: float = Field(ge=0, description="Interest rate in percentage")
    outstanding_debt: float = Field(ge=0, description="Outstanding debt in dollars")    

class PredictionResponse(BaseModel):
    credit_score: Literal["Bad", "Good"]