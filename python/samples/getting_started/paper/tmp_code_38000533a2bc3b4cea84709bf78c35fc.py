import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Create a date range for February
date_range = pd.date_range(start='2/1/2022', end='2/28/2022')

# Generate random daily amounts sold
np.random.seed(0)  # for reproducibility
daily_amounts = np.random.randint(50, 200, size=len(date_range))

# Create a DataFrame
df = pd.DataFrame(daily_amounts, columns=['Amount'], index=date_range)

# Fit an ARIMA model
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit(disp=0)

# Make prediction for the first week of March
pred = model_fit.predict(start='3/1/2022', end='3/7/2022')

# Plot the original data and the prediction
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Amount'], label='Original')
plt.plot(pred.index, pred, label='Prediction', linestyle='--')
plt.legend()
plt.show()