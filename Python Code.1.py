# Q.1  Use if, if-else and if-elif-else statements in make decisions in program


# Part,1: Use 'if' statement to check if number is positive

number = 10
if number > 0:
    print("The number is positive.")

# Part,2: Use 'if-else' to check true or false number

number = 7
if number % 2 == 0:
    print("The number is true.")
else:
    print("The number is false.")
# Part,3  Use 'if-elif-else' to assign grade

# Ask user to input percentage of student and display corresponding letters
#
# 1.  A -> Grade Range >=80 and <= 100
# 2.  B -> Grade Range >=70 and <80
# 3.  C -> Grade Range >=60 and <70
# 4.  D -> Grade Range >=50 and <60
# 5.  Fails -> Grade Range <50

grade = input("Enter percentage: ")
grade = float(grade)

if grade >= 80 and grade <= 100:
    print("A grade")
elif grade >= 70 and grade < 80:
    print("B grade")
elif grade >= 60 and grade < 70:
    print("C grade")
elif grade >= 50 and grade < 60:
    print("D grade")
else:
    print("Fail")

print("End of code")
