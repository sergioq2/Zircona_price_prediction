# Import necessary modules and packages
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import uvicorn
from main import prediction
import json

# Define a data model using Pydantic to represent diamond attributes
class DiamondData(BaseModel):
    carat: float = 0.2
    cut: str = "Ideal"
    color: str = "E"
    clarity: str = "SI2"
    depth: float = 61.5
    table: float = 55.0

# Create a FastAPI instance
app = FastAPI()

# Define a route to handle the home endpoint
@app.get("/home")
def home():
    # Return a welcome message for the API
    return {"message": "Welcome to the API to predict the price of a diamond by Sergio Quintero"}

# Define a route to handle the prediction endpoint
@app.post("/predict")
def predict(data: DiamondData):
    try:
        # Convert Pydantic model to JSON-serializable format
        data = jsonable_encoder(data)
        data = json.dumps(data)
        
        # Make a prediction using the imported 'prediction' function
        prediction_result = prediction(data)
        prediction_result = float(prediction_result)
        # Return the prediction result
        return {"prediction": prediction_result}
    except Exception as e:
        # Handle prediction failure and return an error message
        return {"error": f"Prediction failed: {str(e)}"}

# Run the FastAPI application using uvicorn when this script is executed
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
