def Add(num1,num2):
    
    return num1+num2

def Sub(num1,num2):   
    return num1-num2
def  Mul(num1,num2):    
    return num1*num2
def Divide(num1,num2):
    return num1/num2
def intDiv(num1,num2): #This could also be done using floor method which is the part of math module
    return num1//num2
def Mod(num1,num2):
    return num1%num2


num1=int(input("Enter 1st no: "))
num2=int(input("Enter 2nd no:"))

choice=str(input(f"Choose an operation:\n 1: for addition of {num1} & {num2}\n 2: for Subtraction of {num1} & {num2}\n 3: for the Multiplication of {num1} & {num2}\n 4: for the division of {num1} & {num2}\n 5: for the floor division of {num1} & {num2}\n 6: for the modulus of {num1} & {num2}\n"))
 
if choice=="1":
    print(f"Addition of {num1} & {num2} is {Add(num1,num2)}")
elif choice=="2":
     print(f"Subtraction of {num1} & {num2} is {Sub(num1,num2)}")
elif choice=="3":
     print(f"Multiplication of {num1} & {num2} is {Mul(num1,num2)}")     
elif choice=="4":
     print(f"Division of {num1} & {num2} is {Divide(num1,num2)}")  
elif choice=="5":
     print(f"Floor division of {num1} & {num2} is {intDiv(num1,num2)}") 
else:
     print(f"Modulus of {num1} & {num2} is {Mod(num1,num2)}")            


"""The result of floor division is closest integer which is lesser or equal to float value
Example: 0.1 will give ans 0
11.2 will give 11 as answer bcz 11 is smaller and closest to 11.2     

-------Benefits of using floor division-------
Benefits of Using Floor Division (//):
1. It is used to find the quotient of two numbers.

Indexing in Arrays and Lists: When you need to calculate an index based on division,
 such as dividing an array into equal parts.
 
2. It is used to find the number of times a number can be divided by another number.

3: Integer Result: Ensures an integer result from a division operation, which is useful when you need a 
whole number without any fractional part.

Rounding: Provides a way to round a number down to the nearest integer, which is useful when
you need to round a number down to the nearest whole number.

Consistency: When working with integer indices or counters, floor division guarantees that you will always get 
an integer, avoiding potential issues with floating-point arithmetic.

Efficiency: Floor division can be more efficient than using the modulo operator (%) to check for divisibility

Performance: Floor division is generally faster than converting a float result to an integer using other methods.

"""
if 3<4: 
    
    print("3 is greater than 4")

