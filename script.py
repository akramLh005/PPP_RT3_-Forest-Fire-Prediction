import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# load the model
model = pickle.load(open('modelForPrediction.sav', 'rb'))
scaler = StandardScaler()

def predict(features):
    X = pd.DataFrame([features], columns=["temp", "Ws", "Rain", "FFMC", "DMC", "ISI"])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)
    return prediction

def main():
    st.title("Fire Prediction Model")

    temp = st.slider("Temperature", min_value=0.0, max_value=100.0, step=0.1)
    ws = st.slider("Ws", min_value=0.0, max_value=100.0, step=0.1)
    rain = st.slider("Rain", min_value=0.0, max_value=100.0, step=0.1)
    ffmc = st.slider("FFMC", min_value=0.0, max_value=100.0, step=0.1)
    dmc = st.slider("DMC", min_value=0.0, max_value=100.0, step=0.1)
    isi = st.slider("ISI", min_value=0.0, max_value=100.0, step=0.1)

    features = [temp, ws, rain, ffmc, dmc, isi]

    if st.button('Predict'):
        prediction = predict(features)
        st.balloons()
        st.success(f'The predicted class is: {prediction}')

if __name__ == '__main__':
    main()
