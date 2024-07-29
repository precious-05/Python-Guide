#Steps
#----Open the text file in read mode -----  Then read each line by using loop 
#----Count each word in a line using split() and len() ----- Print the results

file=open("htmll.txt","r")
#content=file.read()
count=0
 
for line in file:
    totalwords=line.split(" ")
    print(totalwords)
    count+=len(totalwords)

file.close()   #If we have opened a file it is very necessary to close that file too
    
print("No of words in html text file are: ",count)    
