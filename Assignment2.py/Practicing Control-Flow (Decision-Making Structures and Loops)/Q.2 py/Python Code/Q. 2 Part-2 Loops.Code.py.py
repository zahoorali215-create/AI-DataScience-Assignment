# Part 2: Loops

# 1. Print 1 to 30

for i in range(1,31):
    print(i)

# 2. Even numbers 1 to 50 (while)

n = 1
while n <= 50:
    if n % 2 == 0:
        print(n)
    n += 1

# 3 .Multiplication table

num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 4. Odd numbers 1 to 50 (while)

n = 1
while n <= 50:
    if n % 2 != 0:
        print(n)
    n += 1
# 5. Sum of numbers 1 to 50

total = 0
for i in range(1, 51):
    total += i
print("Sum:", total)

# 6. Print each character

text = "Python"
for ch in text:
    print(ch)

# 7. Factorial using while

n = int(input("Enter number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial:", fact)

# 8. Countdown 10 to 1

for i in range(10, 0, -1):
    print(i)

# 9. Password until correct

correct_password = "1234"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password")
# 10. Square of numbers 1 to 10

for i in range(1, 11):
    print(f"{i}^2 = {i*i}")

# 11. Sum of even and odd (1–50)

even_sum = 0
odd_sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

# 12. First 10 Fibonacci numbers
# Bonus Challenge
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b










