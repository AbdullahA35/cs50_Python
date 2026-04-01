"""num= int (input("Enter a number : "))
if(num%2==0):
    print("The number is Even")
else:
    print("The number is Odd") """
    
#Using function and boolean returns
def main():
    x=int(input("Enter a number : "))
    if(is_even(x)):
        print("The number is Even")
    else:
        print("The number is Odd")

def is_even(n):
    if(n%2==0):
        return True
    else:
        return False
    #Another way to write this is
    #return True if n%2==0 else False
    #OR 
    #return (n%2==0)

main()