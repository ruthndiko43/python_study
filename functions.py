def hello():
    print('Hello Ruth')

#calling a function
hello()

#function to calc area of  triangle
def area():
    base=10
    height=5
    area=0.5*base*height
    print(area)

area()

#create a function that calculates area of a circle.
def area_circle():
    radius=10
    area=3.14*radius*radius
    print(area)

area_circle()
    
def triangle_area(base,height):
    area=0.5*base*height
    print(area)
triangle_area(10,20)
triangle_area(30,20)
area()

#create a function that calculates area of a rectangle re use the function.
def rectangle_area(length,width):
    area=length*width
    print(area)
rectangle_area(10,20)
rectangle_area(30,20)
area()

# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

def largest_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        large=num1
    elif num2>num1 and num2>num3:
        large=num3
    else:
        large=num3
    (large)

largest_number(100,200,300)  
    
    
def largest_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        large=num1
    elif num2>num1 and num2>num3:
        large=num2
    else:
        large=num3
    print(large)

input1=int(input('Enter 1st number: '))
input2=int(input('Enter 2st number: '))
input3=int(input('Enter 3st number: '))
largest_number(input1,input2,input3)  
    
#check if a number is even 
def even_number(num):
    if num%2==0:
        return 'Even'
    elif number%2==1:
        return 'Odd'

number=int(input("Enter a number: "))
result=even_number(number)

print(f'{number} is an {result} number')

