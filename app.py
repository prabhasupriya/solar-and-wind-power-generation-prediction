import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model1.pkl", "rb"))

st.title("⚡ Solar and Wind Power Generation Prediction ⚡")

# User inputs StartHour', 'EndHour
StartHour = st.number_input("Start Hour (0-23)", min_value=0, max_value=23, step=1)
EndHour = st.number_input("End Hour (0-23)", min_value=0, max_value=23, step=1)
dayOfYear = st.number_input("Day of Year (1-365)", min_value=1, max_value=365, step=1)

if st.button("Predict Power"):
    input_data = np.array([[StartHour, EndHour, dayOfYear]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Power Generation: {prediction[0]:.2f} kWh")
