import joblib
from app.core.config import Config

def load_model():
    return joblib.load(Config.MODEL_PATH)

model = load_model()
