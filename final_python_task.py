# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.
# base=int(input("Enter the base of Triangle: "))
# height=int(input("Enter the height of Triangle: "))
# area=0.5*base*height
# print("The area is",area)


# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.

# number=int(input("Enter a number: "))
# if number %2==0:
#     print("Even number")
# elif number%2==1:
#     print("Odd number")

# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

phone = input("Enter phone number: ").strip()
if phone.startswith("+254"):
    print("Valid number")
elif phone.startswith("07"):
    phone = "+254" + phone[1:]
    print(phone)
elif phone.startswith("01"):
    phone = "+254" + phone[1:]
    print(phone)
elif phone.startswith("7"):
    phone = "+254" + phone
    print(phone)
else:
    print("Invalid number")
   
#    TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.
email=input("Enter your email: ")
email = input("Enter email: ").strip()

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 > num3:
        largest = num2
    else:
        largest = num3

print("Largest number is:", largest)

# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.
correct_password = "admin@123"
attempts = 4

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong password!")

        if attempts > 0:
            print("Attempts left:", attempts)
        else:
            print("Account locked. No attempts left.")