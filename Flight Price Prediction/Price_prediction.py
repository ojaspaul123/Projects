import streamlit as st
import pandas as pd
import pickle

# Load model
with open("flight_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("✈️ Flight Price Prediction App")

st.write("Enter flight details to predict price")

# User Inputs
airline = st.selectbox("Airline", ["IndiGo", "Air India", "Jet Airways", "SpiceJet","Vistara", "GoAir"])
source = st.selectbox("Source", ["Delhi", "Mumbai", "Kolkata", "Bangalore","Hyderabad","Cochin","New Delhi"])
destination = st.selectbox("Destination", ["Cochin", "Delhi", "Hyderabad", "Kolkata","Banglore","New Delhi","Mumbai"])

total_stops = st.selectbox("Total Stops", [0, 1, 2, 3])


dep_hour = st.slider("Departure Hour", 0, 23)
dep_min = st.slider("Departure Minute", 0, 59)

arrival_hour = st.slider("Arrival Hour", 0, 23)
arrival_min = st.slider("Arrival Minute", 0, 59)
duration_hours = st.number_input("Duration (hours)", min_value=0)
duration_mins = st.number_input("Duration (minutes)", min_value=0)

# Prediction button
if st.button("Predict Price"):
    
    input_df = pd.DataFrame({
    "Airline": [airline],
    "Source": [source],
    "Destination": [destination],
    "Total_Stops": [total_stops],
    "Dep_hours": [dep_hour],         
    "Dep_min": [dep_min],
    "Arrival_hours": [arrival_hour], 
    "Arrival_min": [arrival_min],
    "Duration_hours": [duration_hours],
    "Duration_min": [duration_mins]  
})

    prediction = model.predict(input_df)

    st.success(f"💰 Estimated Price: ₹ {int(prediction[0])}")