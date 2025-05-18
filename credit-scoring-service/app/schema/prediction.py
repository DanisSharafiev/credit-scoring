from pydantic import BaseModel
from enum import Enum
from typing_extensions import Literal

class PredictionRequest(BaseModel):
    age: int

class PredictionResponse(BaseModel):
    credit_score: Literal["Bad", "Good"]