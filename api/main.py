from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd

app = FastAPI(title="Real-Time Fraud Detection API")

# Direct production_model folder se load karna (No MLflow tracking URI issues)
try:
    print("Loading production model...")
    model = mlflow.pyfunc.load_model("production_model")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class TransactionData(BaseModel):
    features: dict  

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running. Use /predict endpoint."}

@app.post("/predict")
def predict_fraud(data: TransactionData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded.")
    
    try:
        input_data = pd.DataFrame([data.features])
        prediction = model.predict(input_data)
        result = "Fraudulent" if prediction[0] == 1 else "Legitimate"
        
        return {
            "prediction": result,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))