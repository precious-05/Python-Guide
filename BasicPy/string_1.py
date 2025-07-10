

def Upper(string):
    print("The string in uppercase is: ",string.upper())

def Lower(string):
    print("The string in lowercase is: ",string.lower())

def Reverse(string):
    print("The string in reverse order is: ",string[::-1])

def Hyphen(string):
    print("Replaced the spaces with hyphen",string.replace(' ','-'))

string=str(input("Enter a String:"))

Upper(string)
Lower(string)
Reverse(string)
Hyphen(string)
#string.swapcase
#split method
#Strings are immutable data types
#They are ordered and can be indexed or sliced
#count specific words such as count("The")