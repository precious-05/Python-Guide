# Program to count positive and negative numbers in an array
count_negative = 0
count_positive = 0

size = int(input("Please enter the size of array: "))
array = []

for i in range(size):
    number = int(input("\nPlease enter the element of array: "))
    array.append(number)

print("\n\nThe elements of the array are: ")
for number in array:
    print(number, end=" ")

for number in array:
    if number < 0:
        count_negative += 1
    elif number > 0:
        count_positive += 1

print(f"\n\nTotal number of negative elements in array are: {count_negative}")
print(f"Total number of positive elements in array are: {count_positive}")
