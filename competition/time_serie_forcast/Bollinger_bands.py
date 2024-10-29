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





import pandas as pd
import numpy as np

# Example data (replace with your own DataFrame)
# Let's assume df is a DataFrame with a 'Close' column for close prices
# df = pd.DataFrame({'Close': [...]})

# Parameters for Bollinger Bands
window = 20   # Moving average period
num_std_dev = 2  # Number of standard deviations for the bands

# 1. Calculate the Simple Moving Average (SMA)
df['SMA'] = df['Close'].rolling(window=window).mean()

# 2. Calculate the rolling standard deviation
df['STD'] = df['Close'].rolling(window=window).std()

# 3. Calculate the Upper and Lower Bollinger Bands
df['UpperBB'] = df['SMA'] + (num_std_dev * df['STD'])
df['LowerBB'] = df['SMA'] - (num_std_dev * df['STD'])

# Display the DataFrame with Bollinger Bands
print(df[['Close', 'SMA', 'UpperBB', 'LowerBB']].head(25))

# Optional: Plot the Bollinger Bands
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['SMA'], label=f'{window}-Period SMA', color='orange')
plt.plot(df['UpperBB'], label='Upper Bollinger Band', linestyle='--', color='green')
plt.plot(df['LowerBB'], label='Lower Bollinger Band', linestyle='--', color='red')
plt.fill_between(df.index, df['LowerBB'], df['UpperBB'], color='grey', alpha=0.2)

plt.title('Bollinger Bands')
plt.legend()
plt.show()
