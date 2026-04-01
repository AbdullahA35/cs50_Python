x=int(input("Value of x : "))
y=int(input("Value of y : "))

#Conditionals :

#this code runs all three ifs even if the first one is true the other are not even requried to run increasing complexity
if x<y:
    print("X is less than Y")
if x>y:
    print("X is greater than Y")
if x==y:
    print("X is equal to Y")    

#writing code using elif that makes else if and is exclusive
if x<y:
    print("X is less than Y")
elif x>y:
    print("X is greater than Y")
elif x==y:
    print("X is equal to Y")  

#writing code using the exception through else keyword
if x<y:
    print("X is less than Y")
elif x>y:
    print("X is greater than Y")
else :
    print("X is equal to Y")  

#Conditional Operators

#OR
if x<y or x>y:
    print("X is not equal to Y")
else:
    print("X is equal to Y")