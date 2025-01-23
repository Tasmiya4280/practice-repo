num1 = int(input("enter the 1st number :"))
num2 = int(input("enter the 2nd number :"))
choice = input("Enter the operation : (options + , - , *, /, %)")

if choice == "+":
    sum = num1+num2
    print("sum of 2 numbers is:", sum)
elif choice == "-":
    diff = num1-num2
    print("sum of 2 numbers is:", diff)
elif choice == "*":
    prod = num1*num2
    print("sum of 2 numbers is:", prod)
elif choice == "/":
    division = num1/num2
    print("sum of 2 numbers is:", division)
elif choice == "%":
    remainder = num1%num2
    print("sum of 2 numbers is:", remainder )