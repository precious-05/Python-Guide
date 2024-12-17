# Program to display a 2D array and reverse its rows
row = int(input("Enter the row size of 2D Array: "))
col = int(input("Enter the column size for the 2D Array: "))

array = []
for i in range(row):
    row_elements = []
    for j in range(col):
        number = int(input("Enter the 2D array element: "))
        row_elements.append(number)
    array.append(row_elements)

print("\nThe 2D Array elements are:\n")
for i in range(row):
    for j in range(col):
        print(array[i][j], end="\t")
    print()

print("\n\nThe 2D Array in rows reverse order is:")
for i in range(row - 1, -1, -1):
    for j in range(col):
        print(array[i][j], end="\t")
    print()
