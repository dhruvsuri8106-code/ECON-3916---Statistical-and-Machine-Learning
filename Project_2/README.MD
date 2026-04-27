# MLB Pitch Outcome Predictor
### ECON 3916 — Statistical and Machine Learning | Project 2

---

## Overview

This project investigates whether we can predict the advantage a baseball play gives to the hitting team using pitching data and match context. Specifically, the target variable is delta_home_win_exp — the change in home team win expectancy resulting from a given pitch or play.

This is a regression prediction problem: rather than inferring causation, the goal is to forecast how much a play shifts win probability based on observable pitching and game features.

Potential stakeholders: Pitchers and coaching staff who want to understand which pitch characteristics correlate with hitter success, and adjust their approach accordingly.

---

## Dataset

Name: MLB Statcast Data 2018
Source: https://www.kaggle.com/datasets/s903124/mlb-statcast-data
Observations: 184,480 pitches
Features: 93 columns
Target Variable: delta_home_win_exp
Access Date: April 16, 2026

---

## Project Structure

Project_2/
├── Project_2.ipynb         # Main analysis notebook
├── app.py                  # Streamlit web application
├── model.pkl               # Saved Random Forest model
├── requirements.txt        # Python dependencies
└── README.md

---

## Methodology

### 1. Exploratory Data Analysis (EDA)

- Loaded and inspected the full Statcast dataset (184K+ rows, 93 columns)
- Visualized distributions of key features: release_speed, spin_axis, and the target delta_home_win_exp
- Generated a full correlation heatmap across all numeric features
- Applied Tukey Fences (IQR method) for outlier detection on delta_run_exp
- Identified and addressed missing data — most missingness was in the events column, due to pitches not put in play

Key EDA findings:
- The target variable is highly concentrated near 0 — most pitches have minimal win probability impact. Outlier values correspond to high-leverage events like home runs or clutch strikeouts.
- delta_run_exp is the most correlated feature with the target, but multicollinearity is limited given the low average run totals per game.
- The cleaned sample is biased toward balls put in play; pitches with no event outcome were dropped with the events column.

### 2. Feature Engineering and Preprocessing

- Removed rows with missing values across the three selected features and the target
- Final feature set: release_speed, spin_axis, delta_run_exp
- 80/20 train/test split with random_state=42 for reproducibility

### 3. Modeling

Two regression models were trained and evaluated:

Model 1 — Linear Regression (Baseline)
A simple, interpretable baseline to establish a performance floor. Metrics: RMSE, MAE, R2

Model 2 — Random Forest Regressor
An ensemble tree-based model with 50 estimators, trained using all available CPU cores (n_jobs=-1). Metrics: RMSE, MAE, R2

### 4. Model Evaluation

- 3-fold cross-validation using neg_mean_squared_error on the training set for both models
- Side-by-side CV RMSE comparison to assess generalization
- Actual vs. Predicted scatter plot for the Random Forest model
- Feature importance chart (Gini-based), annotated with a caveat distinguishing predictive importance from causal effect

---

## Results Summary

Model 1 - Linear Regression: see notebook for CV RMSE
Model 2 - Random Forest: see notebook for CV RMSE

The Random Forest model outperformed the linear baseline, capturing non-linear relationships between pitch characteristics and win expectancy shifts.

Feature importance order (Random Forest): delta_run_exp > release_speed > spin_axis

---

## Streamlit App

An interactive prediction app was built with Streamlit, allowing users to adjust pitch parameters via sliders and observe the predicted change in home win expectancy in real time.

App features:
- Sidebar sliders for release_speed, spin_axis, and delta_run_exp
- Live prediction display with interpretation guide
- Line chart showing how predicted win expectancy shifts as release speed varies

Running the App Locally:
pip install -r requirements.txt
streamlit run app.py

---

## Dependencies

streamlit>=1.31.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.4.0
matplotlib>=3.7.0
seaborn>=0.12.0
joblib>=1.3.0

---

## Limitations and Caveats

- Sample bias: Rows with missing events data (non-contact pitches) were dropped, so the model is trained only on balls put in play. Results may overstate pitcher disadvantage relative to all pitch types.
- Predictive, not causal: Feature importances reflect statistical association, not causation.
- Feature scope: Only three features were used in the final model. Incorporating additional Statcast metrics (e.g., launch angle, exit velocity, pitch type) could substantially improve performance.

---

## Course

ECON 3916 — Statistical and Machine Learning
