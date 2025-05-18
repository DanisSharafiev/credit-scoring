from pathlib import Path

class Config:
    MODEL_PATH = Path(__file__).parents[2] / "models" / "model.pkl"

