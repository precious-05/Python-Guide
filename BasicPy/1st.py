print("Hello World in Python")
print("Excited to start my new journey :) ")

print("Even , odd number program in python")

number=10

if number%2==0:
   print("Number is Even")
else:
   print("Number is odd")


print("To print 2 statements on the same line","Separate that line in print function using comma")
print(20)
print(20+20)


#Variables in Python
name="Alina"  #can also be written in single or tripple quotes
age=19
ch='e'
old=False
young=None
print("My name is ", name)
print("My age is", age)

#printing the type of variables

print(type(name))
print(type(age))
print(type(ch))
print(young)
print(old)

#ctrl+z is used to undo any task in VS Code
#Python is a Cas Sensitive Language




#                                    Task#1:  Prnting the Sum of 2 Numbers
a=10
b=20

sum=a+b
print("Sum is ", sum)




 
 


                        #Execution of Expression
                        # sign * is used to join string and numeric values 
                        # sign + is used to concatenate 2 strings
A,B=3,2
Txt="$"    
print(A*Txt*B)      

a,b="@",4
text="&"
print((a+text)*b)               


                           # division(with 2 int will give float) & integer division(with float int will give int but display float)

x,y=9,3
print(x/y)

X,Y=1.5,3
print(X//Y)




#Conditional Statements in Python
marks=int(input("Enter your marks: "))
if(marks>90 or marks==100):
    print("Topper")
elif(marks>=50):
    print("Passed") 
else:
    print("Fail")       











"""pip is a package management system for Python. It stands for "Pip Installs Packages"
and is the standard tool used to install and manage software packages written in Python. 
Here's a more detailed overview of what pip does and how it works:

Key Functions of pip:
Installing Packages:

pip allows you to download and install packages from the Python Package Index (PyPI) and other repositories.
Example: pip install requests installs the requests package, a popular library for making HTTP requests.
Managing Package Dependencies:

When you install a package, pip automatically installs any dependencies that package requires.
Example: If package A requires package B, pip install A will also install B if it is not already installed.
Uninstalling Packages:

You can use pip to uninstall packages that are no longer needed.
Example: pip uninstall requests will remove the requests package from your environment.
Listing Installed Packages:

pip can show you a list of all the packages installed in your environment.
Example: pip list displays all installed packages along with their versions.
Upgrading Packages:

pip can update packages to their latest versions.
Example: pip install --upgrade requests updates the requests package to the latest version.
Basic Commands:
Install a package: pip install <package-name>
Uninstall a package: pip uninstall <package-name>
List installed packages: pip list
Show package information: pip show <package-name>
Search for packages: pip search <keyword>
Freeze installed packages: pip freeze (lists installed packages and their 
versions, useful for creating requirements.txt)
How pip Works:
pip connects to the Python Package Index (PyPI) or other specified repositories to fetch the packages.
It downloads the packages as .whl (wheel) files or source distributions, then installs them into your Python environment.
Importance of pip:
Simplifies the process of managing libraries and dependencies.
Ensures that you can easily share and replicate your development environment by using requirements.txt files.
Widely adopted and supported, making it an essential tool for Python development.
By using pip, you can efficiently manage the libraries and frameworks you need for your projects,
keeping your development environment organized and up-to-date."""