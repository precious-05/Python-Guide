# Program to convert the array entered by the user into ascending order
temporary = 0
array = []

print("Program to convert the array entered by the user in ascending order: ")
for i in range(4):
    number = int(input("Enter a Number: "))
    array.append(number)

if array[0] > array[1]:
    array[0], array[1] = array[1], array[0]

if array[0] > array[2]:
    array[0], array[2] = array[2], array[0]

if array[0] > array[3]:
    array[0], array[3] = array[3], array[0]

if array[1] > array[2]:
    array[1], array[2] = array[2], array[1]

if array[1] > array[3]:
    array[1], array[3] = array[3], array[1]

if array[2] > array[3]:
    array[2], array[3] = array[3], array[2]

print("Ascending order of given array is:")
for number in array:
    print(number)
