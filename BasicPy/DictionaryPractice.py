#Dictionary is the collection of key value pairs
                     #Rule No 1
            #---------- Duplication is not allowed in dictionary------------

dic1={
    "Brand": "Audi",
    "Model": "A6",
    "Model": "Q8"
}
print(dic1)
print(f"length of dictionary 1 is {len(dic1)}\n")
dic2={
    "Name": "Alice",
    "Class": "Cs Morning",
    "Roll-No": 29,
    "Name": "Allicce"
}
print(dic2)
print(f"length of dictionary 2 is {len(dic2)}\n")


               #--------------Dictionaries are mutable/Changeable such as----------------

dic3={
    "Flower1": "Rose",
    "Flower2": "Tulip",
    "Flower3": "Lavendar"
}              
print(dic3)
print(f"length of dictionary 3 is {len(dic3)}\n")
#Mutating the dictionary
dic3["Flower1"]="SunFlower"
dic3["Flower2"]="Daffodill"
dic3["Flower3"]="Jasmine"
dic3["Flower"]="Unknown" #This will add this key value pair at the last of the output
print(f"Mutable dictionary is {dic3}\n")





#Accessing the values using key names
print(dic1["Brand"])

#Accessing values using get() method it is used to access only one value
print(dic1.get('Model'))

#All these methods return the "view object" containing keys as list
    #View object reflects any changes that are done to the dictionary So that we can view the changes of dictionary
print(dic1.keys())
dic1["Number"]="AK096"
print(dic1.keys()) #this will show that view object reflects the changes made to dictionary

#Accessing values using value() method , it is used to access all values
print(dic1.values())

#Accessing items using values() method
# item is a key value pair of dictionary & item method returns all key value pairs as list
print(dic1.items())





                         #Changing & Adding the dictionary items

NewDic={
    "Name": 'Alina',
    'Age': 19,
    "DOB": '5 August'
}                                                 

print(f"Before changing key values{NewDic}\n")
NewDic["Age"]= 18
print(f"The New Dictionary after changing value{NewDic}\n")
             #We can also use update method

             #Removing dictionary items or dictionary itself

NewDic.pop("Name")                    
print(f"\n new dictionary after deleting item is{NewDic}\n")   

#Removing the item using popitem() method
NewDic.popitem() # we donot need it to give any argument as it will always remove the last inserted item
print(f"\n new dictionary after deleting Pop item is{NewDic}\n")   

#removing an item usind del keyword
del dic1["Brand"]
print(dic1)

#Empty a dictionary using clear method
NewDic.clear()
print(NewDic)
#deleting the dictionary using del keyword
del dic2

print(dic2)

