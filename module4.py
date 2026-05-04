def main():

    try:
        n = int(input("Enter a positive integer N: "))
        if n <= 0:
            print("N must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return


    numbers = []
    print(f"Please provide {n} numbers one by one:")
    for i in range(n):
        try:
            num = int(input(f"Number {i+1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return


    try:
        x = int(input("Enter an integer X to search for: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return


    if x in numbers:
        print(numbers.index(x) + 1)
    else:
        print("-1")

if __name__ == "__main__":
    main()