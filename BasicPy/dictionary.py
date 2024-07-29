
def updateDic(myDict): #using update method
  
   country=str(input("Enter a new country name:"))
   capital=str(input("Enter the capital name:")) 
   myDict.update({country: capital})
   print(f"updated dictionary is: {myDict}")

myDict= {
    "Turkey" : "Istanbul",
    "France" : "Paris",
    "Japan" : "Tokyo"    
        }
print(myDict)

#using the update method in dictionary to allow the user to add new key value pair in list
updateDic(myDict)

