from module5_mod import DataProcessor

def main():
    processor = DataProcessor()
    
    try:
        n = int(input("Enter N (positive integer): "))
        if n <= 0:
            return
    except ValueError:
        return


    for i in range(n):
        try:
            num = int(input(f"Enter number {i+1}: "))
            processor.insert(num)
        except ValueError:
            continue


    try:
        x = int(input("Enter X to search: "))
        print(processor.search(x))
    except ValueError:
        pass

if __name__ == "__main__":
    main()