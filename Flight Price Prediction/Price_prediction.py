import streamlit as st
import pandas as pd
import pickle
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Flight Price Predictor",
    page_icon="✈️",
    layout="centered"
)
# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    with open("flight_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()
# ---------------- TITLE ----------------
st.title("✈️ Flight Price Prediction")
st.markdown("### Predict Flight Ticket Prices in Real Time")

st.divider()
# ---------------- USER INPUTS ----------------

col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox(
        "Select Airline",
        ["IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara", "GoAir"]
    )

    source = st.selectbox(
        "Source",
        ["Delhi", "Mumbai", "Kolkata", "Bangalore",
         "Hyderabad", "Cochin", "New Delhi"]
    )

    total_stops = st.selectbox(
        "Total Stops",
        [0, 1, 2, 3]
    )

    dep_hour = st.slider(
        "Departure Hour",
        0, 23, 10
    )

    dep_min = st.slider(
        "Departure Minute",
        0, 59, 30
    )

with col2:
    destination = st.selectbox(
        "Destination",
        ["Cochin", "Delhi", "Hyderabad",
         "Kolkata", "Banglore", "New Delhi", "Mumbai"]
    )

    arrival_hour = st.slider(
        "Arrival Hour",
        0, 23, 12
    )

    arrival_min = st.slider(
        "Arrival Minute",
        0, 59, 45
    )

    duration_hours = st.number_input(
        "Duration Hours",
        min_value=0,
        max_value=24,
        value=2
    )

    duration_mins = st.number_input(
        "Duration Minutes",
        min_value=0,
        max_value=59,
        value=30
    )

st.divider()

# ---------------- PREDICTION ----------------

if st.button("🔮 Predict Price", use_container_width=True):

    # Create DataFrame
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

    # Prediction
    prediction = model.predict(input_df)

    predicted_price = int(prediction[0])

    # Result Display
    st.success("Prediction Successful ✅")

    st.metric(
        label="Estimated Flight Price",
        value=f"₹ {predicted_price}"
    )

    st.balloons()

# ---------------- FOOTER ----------------

st.markdown("---")
