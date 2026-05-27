print("calculator")

num1=float(input("Enter first Number:"))
operator=input("Enter operator(+,-,*,/): ")
num2=float(input("Enter second Number:"))

if operator== "+":
    print("Answer = ", num1+num2)

elif operator== "-":
    print("Answer = ", num1-num2)

elif operator== "*":
    print("Answer = ", num1*num2)

elif operator== "/":
    if num2 !=0:
        print("Answer = ", num1/num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")