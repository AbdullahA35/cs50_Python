expression=input("Enter an expression : ")
x,y,z=expression.split(" ")
match y:
    case "+":
        print(float(x)+float(z))
    case "-":
        print(float(x)-float(z))
    case "*":
        print(float(x)*float(z))
    case "/":
        print(float(x)/float(z))
    case _:
        print("unrecognised operation")