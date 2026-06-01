import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # 1. Read and validate the positive integer N
    while True:
        try:
            n_input = input("Enter the number of points (N, positive integer): ")
            N = int(n_input)
            if N > 0:
                break
            else:
                print("Please enter a POSITIVE integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # 2. Initialize a 2D NumPy array of shape (N, 2)
    # Column 0 stores X (Ground Truth), Column 1 stores Y (Predicted Class)
    data = np.zeros((N, 2), dtype=int)

    # 3. Read N pairs of (x, y) coordinates from the user
    print(f"\nPlease provide {N} (x, y) points one by one (where x, y are 0 or 1):")
    for i in range(N):
        print(f"--- Point {i + 1} ---")
        
        # Read X (Ground Truth Class Label)
        while True:
            try:
                x_val = int(input("  Enter X (ground truth class label, 0 or 1): "))
                if x_val in [0, 1]:
                    data[i, 0] = x_val
                    break
                print("  Input must be either 0 or 1.")
            except ValueError:
                print("  Invalid input. Enter 0 or 1.")
                
        # Read Y (Predicted Class Label)
        while True:
            try:
                y_val = int(input("  Enter Y (predicted class label, 0 or 1): "))
                if y_val in [0, 1]:
                    data[i, 1] = y_val
                    break
                print("  Input must be either 0 or 1.")
            except ValueError:
                print("  Invalid input. Enter 0 or 1.")

    # Extract the true and predicted vectors using NumPy slicing
    y_true = data[:, 0]
    y_pred = data[:, 1]

    # 4. Compute Precision and Recall using Scikit-learn
    # zero_division=0 prevents the program from crashing if no positive cases are predicted
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    # 5. Output the final metric scores
    print("\n" + "="*30)
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print("="*30)

if __name__ == "__main__":
    main()


###Sample Input/Output###
"""
module8_metrics-scikit.py"
Enter the number of points (N, positive integer): 5

Please provide 5 (x, y) points one by one (where x, y are 0 or 1):
--- Point 1 ---
  Enter X (ground truth class label, 0 or 1): 1
  Enter Y (predicted class label, 0 or 1): 1
--- Point 2 ---
  Enter X (ground truth class label, 0 or 1): 0
  Enter Y (predicted class label, 0 or 1): 1
--- Point 3 ---
  Enter X (ground truth class label, 0 or 1): 1
  Enter Y (predicted class label, 0 or 1): 1
--- Point 4 ---
  Enter X (ground truth class label, 0 or 1): 0
  Enter Y (predicted class label, 0 or 1): 0
--- Point 5 ---
  Enter X (ground truth class label, 0 or 1): 1
  Enter Y (predicted class label, 0 or 1): 0

==============================
Precision: 0.6667
Recall:    0.6667
==============================
"""