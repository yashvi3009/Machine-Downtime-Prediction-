from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load the pre-trained model at startup
model = joblib.load("D:\\Machine\\logistic_regression_model.pkl")

class PredictionItem(BaseModel):
    Temperature: float
    Run_Time: int

@app.get("/")
async def root():
    return {"message": "Welcome to the Machine Downtime Prediction API. Use /predict or /upload endpoints."}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        return {"error": "Only CSV files are supported"}
    
    with open("uploaded_data.csv", "wb") as f:
        f.write(await file.read())
    
    return {"message": f"File '{file.filename}' uploaded successfully"}


@app.post("/predict")
async def predict(item: PredictionItem):
    # input data for prediction
    input_data = pd.DataFrame([{
        "Machine_ID": 0,  
        "Temperature": item.Temperature,
        "Run_Time": item.Run_Time
    }])

    # prediction
    yhat = model.predict(input_data)[0]
    confidence = max(model.predict_proba(input_data)[0])  

    return {
        "Downtime": "Yes" if yhat == 1 else "No",
        "Confidence": float(confidence)
    }
