# Class to represent a Stack
class Stack:
    def __init__(self):  # Default Constructor
        self.top = -1  # Initialize top to -1
        self.arr = [0] * 5  # Array of size 5 initialized with zeros

    # Method to check if the stack is empty (underflow condition)
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    # Method to check if the stack is full (overflow condition)
    def is_full(self):
        if self.top == 4:  # Because the size of the array is 5
            return True
        else:
            return False

    # Method to push an element onto the stack
    def push(self, value):
        if self.is_full():
            print("-----The Stack is Overflow-----")
        else:
            self.top += 1
            self.arr[self.top] = value

    # Method to pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("-----The Stack is Underflow-----")
        else:
            self.arr[self.top] = 0
            self.top -= 1

    # Method to peek at a specific position in the stack
    def peek(self, position):
        if self.is_empty():
            print("-----The Stack is Underflow-----")
            return 0
        else:
            return self.arr[position]

    # Method to display all values in the stack
    def display(self):
        print("All values in Stack are:")
        for i in range(4, -1, -1):  # Display stack from top to bottom
            print(f"| {self.arr[i]} |", end=" ")
        print()


# Main function to perform stack operations
def main():
    S1 = Stack()
    while True:
        print("\nWhat Stack operation do you want to perform? Press 0 to Exit:")
        print("1: push()")
        print("2: pop()")
        print("3: isEmpty()")
        print("4: isFull()")
        print("5: peek()")
        print("6: display()")

        option = int(input("Enter your choice: "))
        if option == 0:
            break
        elif option == 1:
            value = int(input("Enter the element to push: "))
            S1.push(value)
        elif option == 2:
            S1.pop()
        elif option == 3:
            print("Stack is Empty:", S1.is_empty())
        elif option == 4:
            print("Stack is Full:", S1.is_full())
        elif option == 5:
            position = int(input("Enter the position to peek(): "))
            print(f"The value at position {position} is: {S1.peek(position)}")
        elif option == 6:
            S1.display()
        else:
            print("Invalid Option! Try Again.")


if __name__ == "__main__":
    main()
