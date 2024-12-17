# Program to display odd or even numbers based on user choice
size = int(input("Please enter the size of array: "))
array = []

for i in range(size):
    number = int(input("Enter the element you want to store in array: "))
    array.append(number)

print("\n---The elements are---: ")
#print(" ".join(map(str, array)))
print(array)
choice = input("\nEnter the choice:\nChoice 'o' for odd numbers & choice 'e' for even numbers: ")

if choice == 'e':
    print("Even numbers in array are:")
    for number in array:
        if number % 2 == 0:
            print(number, end=" ")
else:
    print("Odd numbers in array are:")
    for number in array:
        if number % 2 != 0:
            print(number, end=" ")
