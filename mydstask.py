#Create a file called mydstask.py and attempt the below questions:
my_ds = [23,"Jane",(560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
#1. Print KES
print(my_ds[3][2]["currency"])
#2. Print 560
print(my_ds[2])
print(type(my_ds[2]))
#3. Print Maths
print(my_ds[3][1])
#4. In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["Amount"]=90
print(my_ds)
#5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
 #    Hint: Strings can be reversed using [::]

# reverse and assign back
my_ds[4] = int(str(my_ds[4])[::-1])
print(my_ds[4])
print(my_ds)
#6. Change the name “John” to “Jane” . 
my_ds[5]=list(my_ds[5])
#modify
my_ds[5][1]='Jane'
print(my_ds)
my_ds[5]=tuple(my_ds[5])
print(my_ds)
#You can research or discuss to find the solutions above.
 #https://realpython.com/quizzes/pybasics-tuples-lists-dicts/ 
