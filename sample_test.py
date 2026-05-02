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