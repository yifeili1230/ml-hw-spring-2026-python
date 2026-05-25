import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

print("=== k-NN Regression Program ===\n")

# Step 1: Read N
try:
    N = int(input("Enter N (number of training points): ").strip())
    if N <= 0:
        print("Error: N must be a positive integer.")
        exit()
except ValueError:
    print("Error: Invalid input for N. Must be a positive integer.")
    exit()

# Step 2: Read k
try:
    k = int(input("Enter k (number of neighbors): ").strip())
    if k <= 0:
        print("Error: k must be a positive integer.")
        exit()
except ValueError:
    print("Error: Invalid input for k. Must be a positive integer.")
    exit()

# Step 3: Read N points (x, y)
print(f"\nEnter {N} points (x, y) one by one:")
X_train = []
y_train = []

for i in range(N):
    try:
        x = float(input(f"Point {i+1} - Enter x: ").strip())
        y = float(input(f"Point {i+1} - Enter y: ").strip())
        X_train.append([x])      # 2D format required by scikit-learn
        y_train.append(y)
    except ValueError:
        print("Error: Invalid number format. Please enter real numbers.")
        exit()

# Convert to NumPy arrays
X_train = np.array(X_train)   # Shape: (N, 1)
y_train = np.array(y_train)   # Shape: (N,)

# Step 4: Calculate variance of labels (y values)
variance_y = np.var(y_train, ddof=0)   # Population variance (default in np.var)
print(f"\nVariance of training labels (y): {variance_y:.6f}")

# Step 5: Check if k <= N
if k > N:
    print(f"\nError: k ({k}) cannot be greater than N ({N}).")
else:
    # Step 6: Train k-NN Regressor using scikit-learn
    knn = KNeighborsRegressor(n_neighbors=k, weights='uniform')
    knn.fit(X_train, y_train)
    
    # Step 7: Get prediction point X
    try:
        X_test = float(input("\nEnter X for prediction: ").strip())
        X_test_array = np.array([[X_test]])   # 2D array
        
        # Predict
        y_pred = knn.predict(X_test_array)
        
        print(f"\nPredicted Y for X = {X_test} is: {y_pred[0]:.6f}")
        
    except ValueError:
        print("Error: Invalid input for X. Must be a real number.")

print("\nProgram finished.")