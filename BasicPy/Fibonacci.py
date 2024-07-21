num1=0
num2=1
i=2
n=int(input("Enter the no of terms:"))
print(num1)
print(num2)

    
while i<n:
    num3=num1+num2    
    print(num3)
    num1=num2
    num2=num3
    i=i+1