from ast import operator


oerator=input("Enter the operator to be performed : ")
digits=int(input("Enter no of dits to be calculated : "))
if digits==3:
    if oerator=="+":
        def add():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            num3=int(input("Enter th num3 : "))
            print("sum of given numbers are ",(num1+num2+num3))
        add()
    elif oerator=="-":
        def subsctraction():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            num3=int(input("Enter th num3 : "))
            print("sum of given numbers are ",(num1-num2-num3))
        subsctraction()
    elif oerator=="*":
        def multiplication():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            num3=int(input("Enter th num3 : "))
            print("sum of given numbers are ",(num1*num2*num3))
        multiplication()
    elif oerator=="*":
        def division():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            num3=int(input("Enter th num3 : "))
            print("sum of given numbers are ",(num1/num2/num3))
        division()
    else:
        print("unknow input")
elif digits==2:
    if oerator=="+":
        def add():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            
            print("sum of given numbers are ",(num1+num2))
        add()
    elif oerator=="-":
        def subsctraction():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            
            print("sum of given numbers are ",(num1-num2))
        subsctraction()
    elif oerator=="*":
        def multiplication():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            
            print("sum of given numbers are ",(num1*num2))
        multiplication()
    elif oerator=="*":
        def division():
            num1=int(input("Enter th num1 : "))
            num2=int(input("Enter th num2 : "))
            
            print("sum of given numbers are ",(num1/num2))
        division()
    else:
        print("unknow input")
else:
    print("unknown")
