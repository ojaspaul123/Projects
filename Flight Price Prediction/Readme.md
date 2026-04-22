# ✈️ Flight Price Prediction

A complete end-to-end Machine Learning project that predicts Indian domestic flight prices based on airline, route, timing, and stops — with an interactive **Streamlit web app** for real-time predictions.
---

<img width="1916" height="1097" alt="Screenshot 2026-04-23 012313" src="https://github.com/user-attachments/assets/90cba8f7-68f5-4cd5-ab35-12805c56d9fb" />
<img width="1916" height="1114" alt="Screenshot 2026-04-23 012326" src="https://github.com/user-attachments/assets/040d8e64-4e48-40bc-ba40-2291b386b73e" />

---

## 📁 Repository Structure

```
flight-price-prediction/
│
├── flight-price-analysis-and-prediction.csv   # Cleaned dataset used for training
├── flight_price_analysis_and_prediction.ipynb # EDA + Feature Engineering notebook
├── Flight_Price_Prediction.ipynb              # Model building & evaluation notebook
├── flight_model.pkl                           # Trained ML model (serialized)
└── Price_prediction.py                        # Streamlit web application
```

---

## 📊 Dataset — `flight-price-analysis-and-prediction.csv`

The dataset contains **67 records** of Indian domestic flight data with the following features:

| Column | Description |
|---|---|
| `Airline` | Name of the airline (IndiGo, Air India, SpiceJet, etc.) |
| `Source` | Departure city |
| `Destination` | Arrival city |
| `Total_Stops` | Number of stops (0 = non-stop) |
| `Price` | Ticket price in ₹ *(target variable)* |
| `Date`, `Month`, `Year` | Date of journey |
| `Dep_hours`, `Dep_min` | Departure time |
| `Arrival_hours`, `Arrival_min` | Arrival time |
| `Duration_hours`, `Duration_min` | Total flight duration |

---

## 🔍 Notebook 1 — `flight_price_analysis_and_prediction.ipynb`

### What I Did
- Loaded and explored the raw flight price dataset
- Performed **Exploratory Data Analysis (EDA)**:
  - Checked for missing values, duplicates, and outliers
  - Visualized price distributions across airlines, sources, and destinations
  - Analyzed correlations between flight duration, stops, and price
- Engineered features by extracting date/time components from raw date strings
- Encoded categorical variables (Airline, Source, Destination) for model compatibility
- Exported the cleaned dataset as the CSV file used downstream

### Problems Faced & Solutions

| Problem | Solution |
|---|---|
| Raw date/time fields stored as strings | Parsed using `pd.to_datetime()` and extracted hour/minute components |
| Categorical columns not accepted by ML models | Applied `LabelEncoder` / `pd.get_dummies()` for one-hot encoding |
| Inconsistent city names (e.g., `Banglore` vs `Bangalore`) | Standardized values during cleaning |
| Outlier prices skewing the model | Investigated with boxplots; retained outliers as valid premium fares |

---

## 🤖 Notebook 2 — `Flight_Price_Prediction.ipynb`

### What I Did
- Loaded the cleaned dataset from Notebook 1
- Split data into **features (X)** and **target (y = Price)**
- Trained and evaluated multiple regression models:
  - Linear Regression
  - Decision Tree Regressor
  - **Random Forest Regressor** ✅ *(best performer)*
- Evaluated using **MAE**, **RMSE**, and **R² Score**
- Tuned hyperparameters to improve accuracy
- Serialized the final trained model using `pickle` → saved as `flight_model.pkl`

### Problems Faced & Solutions

| Problem | Solution |
|---|---|
| Model receiving unseen categorical labels during prediction | Ensured training and inference used the same encoding pipeline |
| Linear Regression underfitting the data | Switched to ensemble model (Random Forest) for better non-linear fit |
| Model column order mismatch during inference | Explicitly defined and matched column order in `Price_prediction.py` |
| `pickle` version incompatibility warnings | Ensured same Python/sklearn version used for saving and loading |

---

## 🚀 Trained Model — `flight_model.pkl`

- Algorithm: **Random Forest Regressor**
- Serialized with Python's `pickle` library
- Input features: `Airline`, `Source`, `Destination`, `Total_Stops`, `Dep_hours`, `Dep_min`, `Arrival_hours`, `Arrival_min`, `Duration_hours`, `Duration_min`
- Output: Predicted flight price in **₹ (INR)**

---

## 🌐 Web App — `Price_prediction.py`

An interactive **Streamlit** application that lets users predict flight prices through a clean UI without writing any code.

### Features
- Dropdown menus for Airline, Source, Destination, and Total Stops
- Sliders for departure and arrival time (hour & minute)
- Number inputs for flight duration
- Instant price prediction on button click

### How to Run
<img width="1536" height="1073" alt="Screenshot 2026-04-23 012443" src="https://github.com/user-attachments/assets/e33319cb-d9dc-4188-80f0-4d92ec6b9c9f" />

```bash
# 1. Install dependencies
pip install streamlit pandas scikit-learn

# 2. Make sure flight_model.pkl is in the same directory

# 3. Launch the app
streamlit run Price_prediction.py
```

The app will open at `http://localhost:8501`

### App Preview

> Select your flight details → Click **"Predict Price"** → Get estimated price like **₹ 5,248**

### Problems Faced & Solutions

| Problem | Solution |
|---|---|
| `python run Price_prediction.py` gave a "No such file" error | Correct command is `python -m streamlit run Price_prediction.py` |
| Model expected different column names than what the app sent | Matched DataFrame column names exactly to training feature names |
| `duration_mins` vs `Duration_min` column name mismatch | Renamed key in the input DataFrame to match training schema |
| App reloading on every slider interaction | Normal Streamlit behavior — added `st.button()` to trigger prediction only on demand |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| Pandas | Data manipulation |
| Scikit-learn | Machine learning |
| Matplotlib / Seaborn | Data visualization |
| Pickle | Model serialization |
| Streamlit | Web application |

---

## 📌 Key Learnings

- Real-world datasets always need cleaning — inconsistent values and type mismatches are the norm
- Feature engineering (breaking timestamps into hour/minute) significantly improved model performance
- The column names and order during prediction **must exactly match** what the model was trained on
- Streamlit makes deploying ML models as apps extremely fast — the entire UI was built in one Python file

---

## 🎯 Accuracy Score - Price Prediction - Machine learning
- This model preditcion have 0.9160 R² score that a decent score to accurate the prediction but not perfect.

**THANK YOU**
