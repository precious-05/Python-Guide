List=[]
for k in range(0,5,1):
    num=(float(input("Enter the number to add in list"))) 
    #float data type is used bcz we have to calculate average too
    List.append(num)
  
print(List)
List.sort()
print(List)
x=max(List)
print(f"{x} are the max in the list")
y=min(List)
print(f"{y} are the min in the list")

Sum=sum(List) 
avg=Sum/len(List)

print (f"Sum of the list is {Sum}")
print (f"Average is {avg}")

min (33)