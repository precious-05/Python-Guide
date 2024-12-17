# Program to display a 2D array entered by the user
row = int(input("Enter the row size: "))
column = int(input("Enter the column size: "))

array = []

print("\n2D Array Input")
for i in range(row):
    row_elements = []
    for j in range(column):
        number = int(input(f"Input the 2D array \narray[{i}][{j}]: "))
        row_elements.append(number)
    array.append(row_elements)

print("\n\n2D Array elements are:\n")
for i in range(row):
    for j in range(column):
        print(array[i][j], end="\t")
    print()
