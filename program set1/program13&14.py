# Program demonstrating mathematical functions
import math

# Basic arithmetic
a = 10
b = 3
# Math module functions
x = 16

print("\nMath module functions:")
print(f"Square root: {math.sqrt(x)}")
print(f"Absolute value: {math.fabs(-x)}")
print(f"Factorial: {math.factorial(5)}")
print(f"GCD of {a} and {b}: {math.gcd(a,b)}")
print(f"Floor: {math.floor(3.7)}")
print(f"Ceiling: {math.ceil(3.2)}")

# Trigonometric functions
angle = math.pi/6  # 30 degrees

print("\nTrigonometric functions:")
print(f"Sin: {math.sin(angle)}")
print(f"Cos: {math.cos(angle)}")
print(f"Tan: {math.tan(angle)}")

# Logarithmic functions
print("\nLogarithmic functions:")
print(f"Natural log of {x}: {math.log(x)}")
print(f"Log base 10 of {x}: {math.log10(x)}")
print(f"e raised to power 2: {math.exp(2)}")
print(f"2 raised to power 3: {math.pow(2,3)}")

