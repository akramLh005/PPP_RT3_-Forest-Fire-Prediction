from fastapi import FastAPI
from fastapi import Request 
import pickle 
import numpy as np

app=FastAPI()

with open('modelForPrediction.sav', 'rb') as f:
     model = pickle.load(f)

@app.post("/prediction")
async def model_prediction(request : Request):
    data = await request.json()
    Temperature=float(data["temp"])
    Wind_Speed =float(data["Ws"])
    Rain=float(data["Rain"])
    FFMC=float(data["FFMC"])
    DMC=float(data["DMC"])
    ISI=float(data["ISI"])
    
    features = [Temperature, Wind_Speed,Rain,FFMC, DMC, ISI]
    for i in features:
        print(type(i))
    Float_features = [float(x) for x in features]
    final_features = np.array(Float_features).reshape(1, -1)
    prediction=model.predict(final_features)[0]
    if prediction == 1:
        pred_msg = 'Forest is Safe!'
    else:
        pred_msg = 'Forest is in Danger!'
    return { 
            "prediction value":int(prediction),
            "message" : pred_msg
           }