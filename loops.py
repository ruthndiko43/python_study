# lst1=list(range(1,10))
# print(lst1)

#  for i in lst1:
#      print("Ruth")
     

# tries=list(range(1,4))

# for i in lst1:
#      pin=input("Enter pin: ")

# #display even number btn 10 and 100
# numbers=list(range(10,101)) 
# for i in numbers:
#     if 1%2==0:
#     print(1)
#     print(num)


numbers=list(range(1,101)) 

nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)

# #display number divisible by 3 and 7  btn 10 and 100

#     if 1%2==0
#     print(i)

#pin
tries=3
attempts=list(range(1,4))

for i in attempts:
	pin=input('Enter pin:')
	correct_pin='1234'
	if pin==correct_pin:
		print("Welcome")
		break
	else:
		remaining_tries=tries-i
		if remaining_tries>0:
			print(f'incorrect pin try again {remaining_tries} tries remaining')
		else:
			print("account Blocked")