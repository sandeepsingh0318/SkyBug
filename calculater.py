def add (x,y):
    return x+y
def sub(x,y):
    return x-y
def multiple(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        print(" It cannot be  divide Zero ")
while True:
    print(" Select Any Operation ")
    print(" 1. Addition ")
    print(" 2. Subtraction ")
    print(" 3. Multiplicaton ")
    print(" 4. Dividie ")
    print(" 5. Exit ")

    choice = input(" Enter Any Operation (1/2/3/4/5) ")

    if choice == '5':
        print(" The user are exit in the calculater")
        break

    if choice in ('1','2','3','4'):

        n1=int(input(" Enter a First Number"))
        n2=int(input(" Enter a Second Number"))

        if choice == '1':
            print(n1,"+",n2,"=",add(n1,n2))
        elif choice == '2':
            print(n1,"-",n2,"=",sub(n1,n2))
        elif choice == '3':
            print(n1,"*",n2,"=",multiple(n1,n2))
        elif choice == '3':
            print(n1,"/",n2,"=",divide(n1,n2))
    else:
        print(" Invalid Input Try Again")

    
