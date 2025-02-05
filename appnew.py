from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the saved model and scaler
model = joblib.load('manufacturing_defect_model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define the input schema
class PredictionRequest(BaseModel):
    features: list[float]  # Expecting a list of floats as input

@app.get('/')
def home():
    return {"message": "Manufacturing Defect Prediction API is Running!"}

@app.post('/predict')
def predict(request: PredictionRequest):
    try:
        # Convert input to numpy array and reshape
        data = np.array(request.features).reshape(1, -1)
        
        # Scale the data
        scaled_data = scaler.transform(data)
        
        # Make prediction
        prediction = model.predict(scaled_data)
        
        return {"DefectStatus": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
