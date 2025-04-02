import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load your dataset (e.g., CSV or database)
data = pd.read_csv(r'D:\pythonProjects\modeloML\data\ventasV2.csv', parse_dates=['fecha'])

# Example data preprocessing
data['day_of_week'] = data['fecha'].dt.dayofweek  # Extract day of week
data['month'] = data['fecha'].dt.month  # Extract month
data['year'] = data['fecha'].dt.year  # Extract year

# Create lag features (e.g., previous day's demand)
data['demand_lag_1'] = data['cantidad'].shift(1)
data['demand_lag_7'] = data['cantidad'].shift(7)  # 1 week lag

# Remove rows with missing values (from the lagging)
data = data.dropna()

X = data[['day_of_week', 'month', 'year', 'demand_lag_1', 'demand_lag_7']]  # Features
y = data['cantidad']  # Target variable

# Split the data (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


model = LinearRegression()
model.fit(X_train, y_train)


# Predict the demand on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"R-squared: {r2}")
