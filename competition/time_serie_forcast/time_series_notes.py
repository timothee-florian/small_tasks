import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV, TimeSeriesSplit
from sklearn.metrics import mean_squared_error, make_scorer

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


param_grid = {
        'n_estimators': np.arange(50, 300, 50),        # Number of trees
        'max_depth': [10, 20, 30, None],               # Maximum depth of the tree
        'min_samples_split': [2, 5, 10],               # Minimum number of samples to split an internal node
        'min_samples_leaf': [1, 2, 4],                 # Minimum number of samples required at a leaf node
        'max_features': ['auto', 'sqrt', 'log2'],      # Number of features to consider at each split
        'bootstrap': [True, False]                     # Whether to bootstrap samples or not
    }

    # Initialize Random Forest Regressor
model = RandomForestRegressor(random_state=42)
metric = mean_squared_error
def random_search_parmater(metric, model, param_grid):

    # Define the parameter grid
    

    # Custom scoring function (you can use RMSE as a metric)
    scorer = make_scorer(metric, greater_is_better=False)

    # Time series cross-validator
    tscv = TimeSeriesSplit(n_splits=5)

    # RandomizedSearchCV setup
    random_search = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_grid,
        n_iter=50,             # Number of parameter settings sampled
        cv=tscv,               # TimeSeriesSplit for cross-validation
        verbose=2,
        random_state=42,
        n_jobs=-1,             # Use all available processors
        scoring=scorer         # Use custom scorer (negative MSE)
    )

    # Fit RandomizedSearchCV
    random_search.fit(X, y)

    # Best parameters from the search
    print("Best Parameters:", random_search.best_params_)

    # Best model's performance
    best_model = random_search.best_estimator_
    y_pred = best_model.predict(X_test)
    rmse = np.sqrt(metric(y_test, y_pred))
    print(f'Best Model RMSE: {rmse}')