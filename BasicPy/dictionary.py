
def updateDic(myDict): #using update method
  
   country=str(input("Enter a new country name:"))
   capital=str(input("Enter the capital name:")) 
   myDict.update({country: capital})   # It will add new Key-Value pair in the dictionary
   print(f"updated dictionary is: {myDict}")

myDict= {
    "Turkey" : "Istanbul",
    "France" : "Paris",
    "Japan" : "Tokyo"    
        }
print(myDict)

#using the update method in dictionary to allow the user to add new key value pair in list
updateDic(myDict)

print(myDict.keys())
print(myDict.values())
print(myDict.items())


#for getting dictionary keys,values, key-values both we use above methods


# Other methods are clear(), del, pop popitem


#pop , popitem, del, clear, update, keys, values, items
#These 8 methods must be remembered on finger-tips   Revise Daily