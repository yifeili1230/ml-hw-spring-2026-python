import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():

    # ==========================================
    try:
        N = int(input("Enter the number of training pairs (N): "))
        if N <= 0:
            print("N must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. N must be an integer.")
        return

    train_features = []
    train_labels = []
    
    print(f"\nPlease provide {N} training pairs one by one:")
    for i in range(N):
        print(f" Pair {i+1}:")
        x_val = float(input("  Enter x (input feature, real number): "))
        y_val = int(input("  Enter y (class label, non-negative integer): "))
        if y_val < 0:
            print("  Warning: y should be a non-negative integer.")
        train_features.append(x_val)
        train_labels.append(y_val)

    X_train = np.array(train_features, dtype=np.float64).reshape(-1, 1)
    y_train = np.array(train_labels, dtype=np.int32)

  
    # ==========================================
    print("-" * 40)
    try:
        M = int(input("Enter the number of test pairs (M): "))
        if M <= 0:
            print("M must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. M must be an integer.")
        return

    test_features = []
    test_labels = []
    
    print(f"\nPlease provide {M} test pairs one by one:")
    for i in range(M):
        print(f" Pair {i+1}:")
        x_val = float(input("  Enter x (input feature, real number): "))
        y_val = int(input("  Enter y (class label, non-negative integer): "))
        test_features.append(x_val)
        test_labels.append(y_val)

    X_test = np.array(test_features, dtype=np.float64).reshape(-1, 1)
    y_test = np.array(test_labels, dtype=np.int32)


    # ==========================================
    best_k = None
    best_accuracy = -1.0


    max_k = min(10, N)
    
    print("\n" + "="*40)
    print(f"Grid Search for kNN (Range: 1 <= k <= {max_k})")
    print("="*40)

    for k in range(1, max_k + 1):
        knn = KNeighborsClassifier(n_neighbors=k)
        

        knn.fit(X_train, y_train)
        

        y_pred = knn.predict(X_test)
        

        acc = accuracy_score(y_test, y_pred)
        print(f"k = {k} -> Test Accuracy: {acc:.4f}")

        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k


    # ==========================================
    print("=" * 40)
    print(f"Result -> Best k: {best_k}")
    print(f"Result -> Corresponding Test Accuracy: {best_accuracy:.4f}")
    print("=" * 40)

if __name__ == "__main__":
    main()