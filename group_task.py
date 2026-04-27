#Q1
#A payroll company needs to calculate employee taxes using different salary bands. Create a system that applies different tax rates depending on salary level and displays final pay.
# Payroll Tax Calculator

salary = float(input("Enter employee salary: "))

# Determine tax rate based on salary bands
if salary <= 20000:
    tax_rate = 0.10   # 10%
elif salary <= 50000:
    tax_rate = 0.20   # 20%
else:
    tax_rate = 0.30   # 30%

# Calculate tax and net salary
tax = salary * tax_rate
net_pay = salary - tax

print("Salary:", salary)
print("Tax:", tax)
print("Net Pay:", net_pay)
#Q2
#A university hostel manager wants to know whether rooms are available. Create a program that checks room count and rejects new applicants when no rooms remain.
# Hostel Room Checker

total_rooms = int(input("Enter total number of rooms: "))
capacity_per_room = int(input("Enter capacity per room: "))
current_students = int(input("Enter current number of students: "))

# Calculate total capacity
total_capacity = total_rooms * capacity_per_room

# Check availability
if current_students < total_capacity:
    available_space = total_capacity - current_students
    print("Rooms available!")
    print("Available spaces:", available_space)
else:
    print("No rooms available. Reject new applicants.")
#Q3
#An investor watches stock prices daily. Build a program that sends alerts whenever a stock price drops below a chosen buying target.
# Stock Price Alert

target_price = float(input("Enter your buying target price: "))
current_price = float(input("Enter current stock price: "))

if current_price <= target_price:
    print("Alert! Stock price is low. Consider buying.")
else:
    print("Price still high. Keep watching.")
#Q4
#A ride-hailing company wants to manage customer expectations. If no drivers are available nearby, inform the customer to retry later
# Ride-Hailing Driver Checker

available_drivers = int(input("Enter number of available drivers nearby: "))

if available_drivers > 0:
    print("Driver available! Booking confirmed.")
else:
    print("No drivers nearby. Please try again later.")
