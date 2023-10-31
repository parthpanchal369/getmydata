a = int(input("Enter your first number: "))
b= int(input("Enter your second number: "))
c = input("Please choose from this, +, -, *, /  ")

if c == '+':
    print(a+b)

elif c == "-":
    print(a-b)

elif c == "*":
    print(a*b)

elif c == "/":
    try:
        a/b
    except Exception as e:
        print(e)



else:
    print("enter the proper value")

