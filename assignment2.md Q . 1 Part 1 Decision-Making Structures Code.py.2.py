# Part 1: Decision-Making Structures

# Q1: Positive, Negative, Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q2: Larger of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is larger")
else:
    print(f"{b} is larger")

# Q3: Largest of Three Numbers

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
if a >= b and a >= c:
    print(f"{a} is largest")
elif b >= a and b >= c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")

# Q4: String Search

if "Mass" in "Saylani Mass IT":
    print("String found")
else:
    print("String not found")

# Q5: Age Category

age = int(input("Enter age: "))
if age < 18:
    print("Minor")
elif 18 <= age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# Q6: Even or Odd

n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q7: Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,x,/): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "x":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# Q8: Check Range

n = int(input("Enter number: "))
if 20 <= n < 40:
    print("In range")
else:
    print("Out of range")

# Q9: Divisibility

n = int(input("Enter number: "))
if n % 2 == 0 and n % 3 == 0:
    print("Divisible by both 2 and 3")
elif n % 2 == 0:
    print("Divisible by 2")
elif n % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")

# Q10: Pass/Fail

score = int(input("Enter score: "))
if score > 60:
    print("Pass")
else:
    print("Fail")

# Q11: Prime Check

n = int(input("Enter number: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# Q12: Temperature Category

temp = float(input("Enter temperature in Celsius: "))
if temp < 0:
    print("Freezing")
elif 0 <= temp < 26:
    print("Moderate")
else:
    print("Hot")



