
import streamlit as st
import pandas as pd
import numpy as np
import joblib  # to load saved model
import matplotlib.pyplot as plt # Added import for matplotlib.pyplot
import seaborn as sns # Added import for seaborn, as it's often used with matplotlib

st.title('MLB Statcast Data 2018: Pitch Outcome Predictor')
st.markdown('This app predicts the `delta_home_win_exp` (advantage to hitting team) based on pitching data and match context.')

# Load model (saved from your Colab notebook)
model = joblib.load('model.pkl')

# Get feature ranges from your original DataFrame (assuming df_cleaned is available or you know the ranges)
# For a more robust app, you might save these min/max values alongside the model.
release_speed_min = 44.2
release_speed_max = 105.0
release_speed_mean = 88.6

spin_axis_min = 0.0
spin_axis_max = 360.0
spin_axis_mean = 179.0

delta_run_exp_min = -1.487
delta_run_exp_max = 3.579
delta_run_exp_mean = 0.0001

# Sidebar controls for input features
st.sidebar.header('Input Pitch Parameters')
release_speed = st.sidebar.slider(
    'Release Speed (mph)',
    min_value=float(release_speed_min),
    max_value=float(release_speed_max),
    value=float(release_speed_mean)
)
spin_axis = st.sidebar.slider(
    'Spin Axis (degrees)',
    min_value=float(spin_axis_min),
    max_value=float(spin_axis_max),
    value=float(spin_axis_mean)
)
delta_run_exp = st.sidebar.slider(
    'Delta Run Expectancy (change in expected runs)',
    min_value=float(delta_run_exp_min),
    max_value=float(delta_run_exp_max),
    value=float(delta_run_exp_mean),
    format='%.3f'
)

# Prepare input data for prediction
input_data = pd.DataFrame({
    'release_speed': [release_speed],
    'spin_axis': [spin_axis],
    'delta_run_exp': [delta_run_exp]
})

# Generate prediction
prediction = model.predict(input_data)[0]

st.subheader('Predicted Delta Home Win Expectancy')
st.metric('Prediction', f'{prediction:.4f}')

st.markdown("""
**Interpretation:**
*   A positive value indicates an increase in the home team's win expectancy for the play.
*   A negative value indicates a decrease in the home team's win expectancy for the play.
*   Values closer to zero suggest a play with minimal impact on win expectancy.
""")

# Placeholder for a simple visualization (e.g., how prediction changes with one input)
# For more complex charts, you'd need to generate more data points.
st.subheader('How Prediction Changes with Release Speed (holding other features constant)')
# Create a range of release speeds
plot_release_speeds = np.linspace(release_speed_min, release_speed_max, 50)
# Create input data for these speeds, keeping other features constant
plot_data = pd.DataFrame({
    'release_speed': plot_release_speeds,
    'spin_axis': spin_axis,
    'delta_run_exp': delta_run_exp
})
# Get predictions for this range
plot_predictions = model.predict(plot_data)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=plot_release_speeds, y=plot_predictions, ax=ax)
ax.set_xlabel('Release Speed')
ax.set_ylabel('Predicted Delta Home Win Expectancy')
ax.set_title('Predicted Win Expectancy vs. Release Speed')
st.pyplot(fig)
