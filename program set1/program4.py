a, b = int(input("Enter first number:")), int(input("Enter second number:"))
op = input("Enter operator:")
if op == "+":
    print(f"Sum of {a} and {b} is {a+b}")
elif op == "-":
    print(f"Difference of {a} and {b} is {a-b}")
elif op == "*":
    print(f"Product of {a} and {b} is {a*b}")
elif op == "/":
    print(f"Quotient of {a} and {b} is {a/b}")
elif op == "%":
    print(f"Remainder of {a} and {b} is {a%b}")
else:
    print("Invalid operator")
