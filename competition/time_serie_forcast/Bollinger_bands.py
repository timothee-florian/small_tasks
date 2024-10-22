import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib as ta



# Parameters for Bollinger Bands
window = 20  # Period for moving average
std_dev = 2  # Standard deviation multiplier for the bands

# 1. Calculate Bollinger Bands
df['SMA'] = ta.SMA(df['Close'], timeperiod=window)
df['UpperBB'], df['MiddleBB'], df['LowerBB'] = ta.BBANDS(df['Close'], timeperiod=window, nbdevup=std_dev, nbdevdn=std_dev, matype=0)

# 2. Measure the width of Bollinger Bands (low width indicates consolidation)
df['BB_Width'] = df['UpperBB'] - df['LowerBB']

# Define a threshold for low volatility (you may adjust this based on your data)
low_volatility_threshold = df['BB_Width'].quantile(0.25)  # Bottom 25% of band widths

# Identify periods of low volatility
df['LowVolatility'] = df['BB_Width'] < low_volatility_threshold

# 3. Detect breakout (price moving outside of the Bollinger Bands)
df['Breakout_Above'] = df['Close'] > df['UpperBB']  # Price breaking above upper band
df['Breakout_Below'] = df['Close'] < df['LowerBB']  # Price breaking below lower band

# 4. Check for volume spikes when breakout occurs
# Define volume spike threshold as 1.5x the rolling 20-period average volume
df['Volume_MA'] = df['Volume'].rolling(window=window).mean()
df['Volume_Spike'] = df['Volume'] > (1.5 * df['Volume_MA'])

# Combine conditions: low volatility followed by breakout and volume spike
df['Peak_Prediction'] = df['LowVolatility'] & (df['Breakout_Above'] | df['Breakout_Below']) & df['Volume_Spike']

# 5. Plot the results
plt.figure(figsize=(14, 8))

# Plot closing prices and Bollinger Bands
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['UpperBB'], label='Upper BB', linestyle='--', color='red')
plt.plot(df['LowerBB'], label='Lower BB', linestyle='--', color='red')

# Highlight predicted peaks
plt.scatter(df.index[df['Peak_Prediction']], df['Close'][df['Peak_Prediction']], marker='o', color='green', label='Predicted Peak')

plt.title('Bollinger Bands and Volume Spike Detection')
plt.legend()
plt.show()
