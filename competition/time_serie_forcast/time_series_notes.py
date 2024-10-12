import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error

def get_dummy_data() -> pd.DataFrame:
    np.random.seed(42)
    date_range = pd.date_range(start='2020-01-01', periods=100, freq='D')
    data = np.random.randn(100).cumsum()  # Random walk
    df = pd.DataFrame(data, index=date_range, columns=['value'])
    return df

df = get_dummy_data()

# Assuming df contains columns: ['volume', 'spread', 'timestamp']
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek

# Creating lag features for volume and spread
def create_lag_features(df, lags, step, feature):
    for lag in range(step, step*lags + 1, step):
        df[f'{feature}_lag_{lag}'] = df[feature].shift(lag)
    return df

df = create_lag_features(df, lags = 5, step = 1, feature ='volume')  # Lag features for volume
df = create_lag_features(df, lags = 5, step = 1, feature ='spread')  # Lag features for spread

# Drop rows with NaN values (due to lagging)
df.dropna(inplace=True)

# Define features and target
X = df.drop(columns=['volume', 'timestamp'])  # Drop target and timestamp
y = df['volume']

# Train-test split using time series cross-validation
tscv = TimeSeriesSplit(n_splits=5)

# Initialize model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Cross-validation
for train_index, test_index in tscv.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # Train the model
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f'Fold RMSE: {rmse}')
