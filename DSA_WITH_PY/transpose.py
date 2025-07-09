# Program to take a 2D array and display its transpose

# Input row and column size
row = int(input("Enter the row size: "))
col = int(input("Enter the column size: "))

# Initialize the 2D array
array = []

# Input the 2D array elements
for i in range(row):
    row_elements = []
    for j in range(col):
        value = int(input(f"array[{i}][{j}]: "))
        row_elements.append(value)
    array.append(row_elements)

# Display the original 2D array
print("\nThe 2D array is:")
for i in range(row):
    for j in range(col):
        print(array[i][j], end="\t")
    print()

# Display the transpose of the 2D array
print("\nThe 2D array after taking transpose is:")
for i in range(col):  # Transpose: rows become columns
    for j in range(row):
        print(array[j][i], end="\t")
    print()
