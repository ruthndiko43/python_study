# # Write a program that displays a numbers 1 to 50 inside a list.
# numbers =list(range(1,50)) 
# print(numbers)
# print(type(numbers))
# # From 1 above display the ones divisible by 7 or 5 inside a list.
# numbers =list(range(1,50)) 
# for i in numbers:
#     if i%7==0 or i%5==0:
#         print(numbers)
        
# # Find sum and average of values in the range between 10 to 40.
# numbers = list(range(10, 41))  # 10 to 40 inclusive
# total = sum(numbers)
# average = total / len(numbers)
# print("Sum:", total)
# print("Average:", average)

# # Put in a list the first 10 odd numbers between 10 to 50. 
# odd_numbers = []
# count = 0
# for num in range(10, 51):
#     if num % 2 != 0:
#         odd_numbers.append(num)
#         count += 1
#     if count == 10:
#         break
# print("First 10 odd numbers:", odd_numbers)

# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
count = 0
for num in range(1, 51):
    if num % 2 == 0:
        count += 1
print("Number of even numbers:", count)

# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.
ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]
total_quantity=0
for i in ls1:
     quantity=1[1]
     total_quantity=total_quantity + quantity
     print(total_quantity)
