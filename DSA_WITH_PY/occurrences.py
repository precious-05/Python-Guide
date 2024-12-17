# Program to count the occurrences of a number in an array
size = int(input("Enter the size of array: "))
array = []

for i in range(size):
    number = int(input("Enter array element: "))
    array.append(number)

print("\n\nArray elements are:")
#print(" ".join(map(str, array)))

print(array)
user_input = int(input("\n\nFrom the array elements, enter any number whose occurrences you want to count: "))

count = 0
for number in array:
    if number == user_input:
        count += 1

print(f"\n\nThe number of occurrences of {user_input} in array is: {count}")
