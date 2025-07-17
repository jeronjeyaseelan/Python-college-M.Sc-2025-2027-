a, b = int(input("Enter first number:")), int(input("Enter second number:"))
print(f'''
Bitwise And of {a} and {b} is {a & b}
Bitwise Or of {a} and {b} is {a | b}
Bitwise Xor of {a} and {b} is {a ^ b}
Bitwise Not of {a} is {~a}
Bitwise Not of {b} is {~b}
Bitwise left shift of {a} is {a << 2}
Bitwise right shift of {a} is {a >> 2}
''')