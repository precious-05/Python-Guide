# Program to take two arrays, display them, and calculate their sums
def main():
    arr1 = [0] * 5  # Array 1 of size 5
    arr2 = [0] * 5  # Array 2 of size 5

    # Input for first array
    print("Enter the elements of the 1st array:")
    for i in range(5):
        arr1[i] = int(input(f"Element {i+1}: "))

    # Display elements of the first array
    print("\nElements of 1st Array are:")
    for i in arr1:
        print(i, end=" ")
    print()

    # Input for second array
    print("\nEnter the elements of the 2nd array:")
    for i in range(5):
        arr2[i] = int(input(f"Element {i+1}: "))

    # Display elements of the second array
    print("\nElements of 2nd Array are:")
    for i in arr2:
        print(i, end=" ")
    print()

    # Calculate the sum of elements of the first array
    sum_arr1 = sum(arr1)
    print(f"\nThe sum of elements of the 1st array is: {sum_arr1}")

    # Calculate the sum of elements of the second array
    sum_arr2 = sum(arr2)
    print(f"The sum of elements of the 2nd array is: {sum_arr2}")


if __name__ == "__main__":
    main()
