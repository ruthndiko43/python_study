if 20<10:
    print("20 is greater")
else:
    print("20 is less")
    
    #check if someone is eligible to vote
age=20

if age >=18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')


#check if temperature is greater that 30 print too hot otherwise normal temperature
temp=int(input(("Enter temperature: ")))
print(temp)
if temp>30:
    print('TOO HOT')
else:
    print('normal temperature')
    
#check if temperature is greater that 30 print too hot , temperature above 15 and less normal temperature
temp=int(input(("Enter temperature: ")))
print(temp)
if temp>30:
    print('TOO HOT')
elif temp>15 and temp<30:
    print('normal temperature')
     
#grading system
marks=int(input(("Enter Marks: ")))
print(marks)

if marks>=80:
    print('Grade A')
elif marks>=70 and marks <80:
    print('Grade B')
elif marks>=60 and marks <70:
    print('Grade C')
elif marks>=50 and marks <60:
    print('Grade D')
else:
    print('Grade E')
    