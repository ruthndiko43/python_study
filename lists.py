fruits=['Apples','Banana','Ginger','Oranges','Mango']
print(fruits)
print(type(fruits))
#index
print(fruits[4])
#slice
print(fruits[1:4])
#update
fruits[1] ='lemon'
print(fruits)
fruits[1] ='Grapes'
print(fruits)

numbers=[10,20,['mike','john','alex'],30,40,50]
print(numbers[2])
print(numbers[2][1])


numbers=[10,20,['mike','john','alex',[1,2,3,4,5]],30,40,50]
print(numbers[2])
print(numbers[2][1])
print(numbers[2][3][3])

fruits=['Apples','Banana','Ginger','Oranges','Mango']
fruits.append('xyz')
print(fruits)