print("Hello World !") #Normal print function
print ("Hello") #Print function that uses + sign
print("Hello","World")

#taking input using print function
print("What is your name ?")
name = input()
print("Hello"+name) #printing using + operator
# "+" operator in print doesn't accept two strings together

#taking input using input function only
name1=input("What is your name ?") #shows the output string and takes input at same line
print("Hello",name1)

# "#" used for single line comments
# """ """ is used for multiline comments

#  STRING FUNCTIONS/METHODS
# strip() : removes the spaces present between the string
name2="Abdullah Aamir"
name2.strip()
print(name2)

# capitalize() : capitalizes the first initial of the string3
name3="abdullah aamir"
name3.capitalize()
print(name3)

# title() : cpitalizes each initial at the start and after the spaces
name4="aqeel arshad"
name4.title()
print(name4)

# split() : splits a string at the given character
first,last=name4.split(" ")

# Overriding the print function
#overriding the print function so that it doesn't end line automatically
print("This is line 1",end="")
print("This is line2")

#overiding the print function such that is doesn't print spaces even when comma is used
print("My name is ","Abdullah", sep="")

# Special String
print(f"My name is {name}")

# INT Data Type
# In python input is always in the form of string that is then converted to other data types when required later on
x=1
y=2
#adding x and y
print(x+y)

#Another way to add x and y
z=x+y
print(z)

# FLOAT(Decimal) Data Type
x=3.2
# round off to nearest integer
print(round(x))

# round off to n(2) decimal places
print(round(3.666666,2))

#round off to n(2) decimal places using special string
a=3.6666666
print(f"{a:.2f}")

#print comma acc to proper convention
b=1000000
print(f"{b:,}")


#Writing function in Python
def hello(to="World"): #here "to" is a default argument that has default argument "World"
    print("Hello",to)

#Calling/using the function
nameA=input("What is your name ?")
hello(nameA)
