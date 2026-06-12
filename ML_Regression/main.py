import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# 1. Load the datasets
train_df = pd.read_csv('dataset/spring2026_kaggle_linear_regression_challenge_train.csv')
test_df = pd.read_csv('dataset/spring2026_kaggle_linear_regression_challenge_test.csv')


# 2. Separate features (X) and target (y)
feature_cols = [f'x{i}' for i in range(15)]
X = train_df[feature_cols]
y = train_df['target']

X_test = test_df[feature_cols]
test_ids = test_df['Id']

# 3. Handle Missing Values (Imputation)
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
X_test_imputed = imputer.transform(X_test)

# 4. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)
X_test_scaled = scaler.transform(X_test_imputed)

# 5. Local Validation
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Calculate local validation RMSE
val_preds = model.predict(X_val)
rmse = np.sqrt(mean_squared_error(y_val, val_preds))
print(f"--- Local Validation RMSE: {rmse:.4f} ---")

# 6. Train on FULL training data and Predict for Kaggle Test Set
final_model = Ridge(alpha=1.0)
final_model.fit(X_scaled, y)
final_preds = final_model.predict(X_test_scaled)

# 7. Save Submission
submission = pd.DataFrame({
    'Id': test_ids,
    'target': final_preds
})
submission.to_csv('Yifei_Li.csv', index=False)
print("Submission file successfully generated!")