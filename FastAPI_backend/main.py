from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



with open('modelForPrediction.sav', 'rb') as f:
    model = pickle.load(f)

class ModelInput(BaseModel):
    temp: float
    Ws: float
    Rain: float
    FFMC: float
    DMC: float
    ISI: float

@app.post("/prediction")
async def model_prediction(input_data: ModelInput):
    print(input_data)
    features = [input_data.temp, input_data.Ws, input_data.Rain, input_data.FFMC, input_data.DMC, input_data.ISI]
    final_features = np.array(features).reshape(1, -1)
    prediction = model.predict(final_features)[0]

    if prediction == 1:
        pred_msg = 'Forest is Safe!'
    else:
        pred_msg = 'Forest is in Danger!'

    return {
        "prediction value": int(prediction),
        "message": pred_msg
    }