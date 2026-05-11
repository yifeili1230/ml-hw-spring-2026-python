class DataProcessor:
    def __init__(self):
        self.data = []

    def insert(self, number):
        self.data.append(number)

    def search(self, x):
        if x in self.data:
            return self.data.index(x) + 1
        else:
            return -1

def main():
    processor = DataProcessor()

    try:
        n = int(input("Enter N (positive integer): "))
        if n <= 0:
            print("N must be a positive integer.")
            return
    except ValueError:
        print("Invalid input for N.")
        return

    for i in range(n):
        try:
            num = int(input(f"Enter number {i+1}: "))
            processor.insert(num)
        except ValueError:
            print("Invalid number, skipping...")


    try:
        x = int(input("Enter X to search: "))
        print(processor.search(x))
    except ValueError:
        print("Invalid input for X.")

if __name__ == "__main__":
    main()