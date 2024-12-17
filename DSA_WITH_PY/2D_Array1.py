# Program to demonstrate 2D array input and output
def main():
    # Initialize a 3x4 array
    arr = [[0 for _ in range(4)] for _ in range(3)]
    
    # Input: Taking values for the 2D array
    print("Enter elements for a 3x4 array:")
    for i in range(3):
        for j in range(4):
            print(f"array[{i}][{j}] = ", end="")
            arr[i][j] = int(input())
        print()
    
    # Output: Displaying the 2D array elements
    print("\n2D Array elements are:")
    for i in range(3):
        for j in range(4):
            print(arr[i][j], end="\t")
        print()


if __name__ == "__main__":
    main()
