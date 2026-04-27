#Create a new file extra_if_task.py
#1.
#Write a program that checks login credentials:
#"Access granted" if email = "admin@gmail.com" and password = "Admin@123"
#"Wrong password" if email is correct but password is wrong
#"Email not found" otherwise
email=input("Enter your email: ")
password=input("Enter password: ")
correct_email="admin@gmail.com"
correct_password ="Admin@123"
if email == correct_email and password ==correct_password:
    print("Access granted")
elif email == correct_email and password!=correct_password:
    print("Wrong password")
else:
    print("Email not found")
#2.
#Create a program that validates an email:
#"Invalid email" if it does not contain "@" or "."
#"Gmail account" if it ends with "@gmail.com"
#"Other email provider" otherwise
email = input("Enter email: ")

if "@" not in email or "." not in email: #other way to do this (email.find("@")==-1 or email.find(".")==-1:)
    print("Invalid email")

elif email.endswith("@gmail.com"):
    print("Gmail account")

else:
    print("Other email provider")
#3.
#Write a program that checks password strength:
#"Weak" if length < 6
#"Strong" if length > 10 and contains both digits and uppercase letters

password = input("Enter your password: ")

if len(password) < 6:
    print("Weak")

elif 6 <= len(password) <= 10 and any(char.isdigit() for char in password):# and password.isalnum():
    print("Moderate")

elif len(password) > 10 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong")

else:
    print("Does not meet any strength category")
#4.
#Write a program that checks a password:
#"Invalid" if it does not start with a capital letter
#"Invalid" if it does not end with a number
#"Valid password" otherwise

password = input("Enter password: ")

if not password[0].isupper():
    print("Invalid")

elif not password[-1].isdigit():
    print("Invalid")

else:
    print("Valid password")
#5.
#Write a program that takes a number and checks:

#"Fizz" if divisible by 3
#"Buzz" if divisible by 5
#"FizzBuzz" if divisible by both
#Otherwise print the number

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")

else:
    print(number)
#6.
#Create a program that takes a score and prints a grade:
#A (≥ 80)
#B (70–79)
#C (60–69)
#D (50–59)
#F (< 50)

score = int(input("Enter score: "))

if score >= 80:
    print("A")

elif 70 <= score <= 79:
    print("B")

elif 60 <= score <= 69:
    print("C")

elif 50 <= score <= 59:
    print("D")

else:
    print("F")

#7.
#Create a program that takes two numbers and prints:
#"Equal" if same
#"First is greater"
#"Second is greater"
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("Equal")

elif num1 > num2:
    print("First is greater")

else:
    print("Second is greater")

#8.
#Write a program that takes a day number (1–7) and prints:
#Weekday (1–5)
#Weekend (6–7)
#Invalid input otherwise

day = int(input("Enter day number (1-7): "))

if 1 <= day <= 5:
    print("Weekday")

elif 6 <= day <= 7:
    print("Weekend")

else:
    print("Invalid input")

#9.
#Create a program that takes a temperature and prints:
#"Freezing" if ≤ 0
#"Cold" if 1–15
#"Warm" if 16–30
#"Hot" if > 30

temp = int(input("Enter temperature: "))

if temp <= 0:
    print("Freezing")

elif 1 <= temp <= 15:
    print("Cold")

elif 16 <= temp <= 30:
    print("Warm")

else:
    print("Hot")

#10.
#Create a program that takes a year and prints:
#"Leap year" if divisible by 4
#"Century year" if divisible by 100
#"Common year" otherwise

year = int(input("Enter a year: "))

if year % 100 == 0:
    print("Century year")

elif year % 4 == 0:
    print("Leap year")

else:
    print("Common year")