import numpy as np

class KNNRegression:
    def __init__(self, k):

        self.k = k
        self.points_x = None
        self.points_y = None

    def fit(self, x_vals, y_vals):

        self.points_x = np.array(x_vals, dtype=float)
        self.points_y = np.array(y_vals, dtype=float)

    def predict(self, X):

        distances = np.abs(self.points_x - X)
        

        nearest_indices = np.argsort(distances)[:self.k]
        
  
        prediction_y = np.mean(self.points_y[nearest_indices])
        
        return prediction_y

def main():
    print("--- k-NN Regression Program ---")
    

    try:
        N = int(input("Enter the number of points (N, positive integer): "))
        k = int(input("Enter the number of nearest neighbors (k, positive integer): "))
        
        if N <= 0 or k <= 0:
            print("Error: N and k must be positive integers.")
            return
    except ValueError:
        print("Error: Invalid input. N and k must be integers.")
        return


    if k > N:
        print(f"Error: k ({k}) cannot be greater than N ({N}).")
        return


    x_vals = []
    y_vals = []
    print(f"\nPlease provide {N} (x, y) points:")
    for i in range(N):
        try:
            x = float(input(self_defined_prompt := f"  Point {i+1} - Enter x value: "))
            y = float(input(self_defined_prompt := f"  Point {i+1} - Enter y value: "))
            x_vals.append(x)
            y_vals.append(y)
        except ValueError:
            print("Error: X and Y must be real numbers. Program terminated.")
            return

    try:
        X_test = float(input("\nEnter the target X value to predict Y: "))
    except ValueError:
        print("Error: X must be a real number.")
        return


    knn_regr = KNNRegression(k)
    knn_regr.fit(x_vals, y_vals)
    result_y = knn_regr.predict(X_test)


    print(f"\n[Result] The predicted Y value for X = {X_test} using {k}-NN Regression is: {result_y}")

if __name__ == "__main__":
    main()