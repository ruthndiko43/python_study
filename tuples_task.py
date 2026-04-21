#1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers = (10, 20, 30, 40, 50)
numbers =list(numbers)
print(type(numbers))
print(numbers)
numbers.append(60)
print(numbers)
numbers[2]=35
print(numbers)
numbers =tuple(numbers)
print(type(numbers))
print(numbers)
#2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
values=list(values)
print(type(values))
values.sort()
print(values)
values=tuple(values)
print(values)
print(type(values))
#3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
 fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
 fruits=list(fruits)
#Count occurrences of "banana",Remove all occurrences of "banana".
#4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
#5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]
