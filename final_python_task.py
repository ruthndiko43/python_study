# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.
base=int(input("Enter the base of Triangle: "))
height=int(input("Enter the height of Triangle: "))
area=0.5*base*height
print("The area is",area)


# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.

number=int(input("Enter a number: "))
if number %2==0:
    print("Even number")
elif number%2==1:
    print("Odd number")

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
        

# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
marks=input("Enter students marks(1-100): ")
if marks>79:
    print("A")
elif marks>60 and marks<79:
    print("B")
elif marks>49 and marks<59:
    print("C")
elif marks>40 and marks<49:
    print("D")
else:
    print("E")

# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and
# print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points,
# the function should print: “License suspended”.

    speed = int(input("Enter speed: "))

if speed <= 70:
    print("Ok")
else:
    points = (speed - 70) // 5
    print("Points:", points)

    if points > 12:
        print("License suspended")
        
        
#  TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....


rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)
    
    
# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.
# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.

products = [['omo','30kshs','300'],
            ['milk','50kshs','200'],
            ['bread','45kshs','359'],
            ['coffee','5kshs','79']]

total = 0

for item in products:
    stock = int(item[2])   # last value
    total += stock

print("Total stock:", total)


# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.datetime
# Once you learn functions,revisit this and write this code inside a function.

year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

current_year = int(input("Enter current year: "))
current_month = int(input("Enter current month: "))
current_day = int(input("Enter current day: "))

birth_days = year * 365 + month * 30 + day
current_days = current_year * 365 + current_month * 30 + current_day

age_days = current_days - birth_days

years = age_days // 365
months = (age_days % 365) // 30
days = (age_days % 365) % 30

print("Age:", years, "years", months, "months", days, "days")

# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.
# Once you learn functions,revisit this and write this code inside a function.



# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

tries = 0

while tries < 3:
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == "admin@mail.com" and password == "Admin@123":
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")
        tries += 1

if tries == 3:
    print("You have been blocked")


# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.


   valid = False

while not valid:
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    try:
        num1 = float(a)
        num2 = float(b)
        valid = True
    except:
        print("invalid character entered")

result = num1 + num2
print("Sum:", result)