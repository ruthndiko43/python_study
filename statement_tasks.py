#Take three inputs from a user, separately. Print the largest of the numbers.
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3nd number: '))
if a>b and a>c:
    print("A is the greatest")
elif b>a and b>c:
    print("B is the greatest")   
elif c>a and c>b:
    print("c is the greatest")
 #   Hint: Determine what type of data is taken in as input.
 
 #Take three inputs from a user, separately. Print the largest of the numbers.
num1= int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3nd number: '))
num4 = int(input('Enter 3nd number: '))
if num1>num2 and num1>num3 and num1>num4:
    print("num1 is the greatest")
elif num2>num1 and num2>num3 and num2>num4:
    print("nu2 is the greatest")   
elif num3>num1 and num3>num2 and num3>num4:
    print("num3 is the greatest")
elif num4>num1 and num4>num2 and num4>num3:
    print("num4 is the greatest")
    
    
#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”temperature=int(input("Enter temperature: "))
temperature=int(input("Enter temperature: "))
if temperature>30:
    print("The temperature is too high")
elif temperature>15:
    print("Normal temperature")
else:
    print("Cold temperature")
#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive) and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
# Check the conditions
if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")


#write a program that checks:
#"small" if number <10
#"medium" if 10-50
#"large" if above 50
num = int(input("Enter value: "))
if num<10:
    print("Small")
elif num>=10 and num<=50:
    print("Medium")
else:
    print("Large")

#create a program that chechs a users balance:
#Insufficient funds if <100
#Moderate balance if 100-1000
#High balance if >1000
balance=int(input("Enter your balance: "))
if balance<100:
    print("Insufficient funds")
elif 100 >= balance <= 1000 :
    print("Moderate balance")
else:
    print("High balance")

#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password="secret123"
user_password=input("Enter your password: ")
if user_password==password:
    print("Access granted")
else:
    print("Access denied")
    
# Write a program that asks the user for email and password checks if the email is equal to "admin@gmail.com" and passaword is equal to "admin123" if it is print Access granted otherwise print Access Denied.
user_email=input("Enter your email: ")
user_password=input("Enter your password: ")
if user_email=="admin@gmail.com" and user_password=="admin123":
    print("Access granted")
else:
    print("Access Denied")

#5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=int(input("Enter student score: "))
student_attendance=int(input("Enter student attendace: "))
if student_score>90 and student_attendance>80:
    print("Excellent student")
else:
    print("Good score,but attendance needs improvement")

 #        Attempt the questions in the link below
#https://realpython.com/quizzes/python-conditional-statements/

