def main():
    x=int(input("Enter a Number :"))
    y=int(input("Enter a Number :"))
    print("The sum is :",add(x,y))

def add(num1=0,num2=0):
    return(num1+num2)

main()

# this convention is used because here we can independantly introduce new function after main wihtout sequence
#we just need to call main at last and it works as fine as possible
