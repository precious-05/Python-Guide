f=open("htmll.txt","r") #open() returns a file pointer
#r mode is default mode means if we dont write it in open function still the file is read successfully
content=f.read() #it also reads the blank spaces
print(content)
f.close()