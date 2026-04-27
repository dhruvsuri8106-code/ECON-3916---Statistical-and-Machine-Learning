---

## Methodology

### 1. Exploratory Data Analysis (EDA)

- Loaded and inspected the full Statcast dataset (184K+ rows, 93 columns)
- Visualized distributions of key features: `release_speed`, `spin_axis`, and the target `delta_home_win_exp`
- Generated a full correlation heatmap across all numeric features
- Applied **Tukey Fences (IQR method)** for outlier detection on `delta_run_exp`
- Identified and addressed missing data — most missingness was in the `events` column, due to pitches not put in play

**Key EDA findings:**
- The target variable is highly concentrated near 0, as expected — most pitches have minimal win probability impact. Outlier values correspond to high-leverage events like home runs or clutch strikeouts.
- `delta_run_exp` is the most correlated feature with the target, but multicollinearity is limited given the low average run totals per game.
- The cleaned sample is biased toward balls put in play; pitches with no event outcome were dropped with the `events` column.

### 2. Feature Engineering & Preprocessing

- Removed rows with missing values across the three selected features and the target
- Final feature set: **`release_speed`**, **`spin_axis`**, **`delta_run_exp`**
- 80/20 train/test split with `random_state=42` for reproducibility

### 3. Modeling

Two regression models were trained and evaluated:

#### Model 1 — Linear Regression (Baseline)
A simple, interpretable baseline to establish a performance floor. Metrics: RMSE, MAE, R²

#### Model 2 — Random Forest Regressor
An ensemble tree-based model with 50 estimators, trained using all available CPU cores (`n_jobs=-1`). Metrics: RMSE, MAE, R²

### 4. Model Evaluation

- **3-fold cross-validation** using `neg_mean_squared_error` on the training set for both models
- Side-by-side CV RMSE comparison to assess generalization
- Actual vs. Predicted scatter plot for the Random Forest model
- Feature importance chart (Gini-based), annotated with a caveat distinguishing *predictive* importance from *causal* effect

---

## Results Summary

| Model | CV RMSE (mean) |
|---|---|
| Linear Regression | — |
| Random Forest | — |

> *(See notebook output cells for exact metric values)*

The **Random Forest** model outperformed the linear baseline, capturing non-linear relationships between pitch characteristics and win expectancy shifts.

**Feature importance order (Random Forest):** `delta_run_exp` > `release_speed` > `spin_axis`

---

## Streamlit App

An interactive prediction app was built with **Streamlit**, allowing users to adjust pitch parameters via sliders and observe the predicted change in home win expectancy in real time.

**App features:**
- Sidebar sliders for `release_speed`, `spin_axis`, and `delta_run_exp`
- Live prediction display with interpretation guide
- Line chart showing how predicted win expectancy shifts as release speed varies

### Running the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Dependencies
