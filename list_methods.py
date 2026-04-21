#append ->used items at the end of the list
my_list=['Mike','Jane','Alex','1000','200','2000',True,False]

my_list.append('Donkey')
print(my_list)

#insert ->adds an item at a specified index
my_list.insert(1,'Mary')
print(my_list)

#pop ->removes an item at a specified index 
my_list.pop(3)
print(my_list)

#sort =>used to arrange list items asc by default
lst1=[1,50,10,20,5,2]
lst1.sort()
print(lst1)

#sort =>(in descending order u write reverse=true)
lst1=[1,50,10,20,5,2]
lst1.sort(reverse=True)
print(lst1)

#extend
lst2=['Mike','Alex','Jane']
lst1=[1,50,10,20,5,2]
lst3=lst2 + lst1
print(lst3)
lst2.extend(lst1)
print(lst3)

#remove
lst2.remove('Alex')
print(lst2)

#count
print(lst2.count('Mike'))

# in membership
lst2=['Mike','Alex','Jane']
print('Alex' in lst2)




#task
lst=[10,20,30,['Jane','Mary',[1000,2000,3000]],40,50,60]

#using methods
# add 70 at the end of the list

#soln
lst.append(70)
print(lst)

# add 1500 btn 1000 and 2000
print(lst[3][2])
lst[3][2].insert(1,1500)
print(lst)

#delete 2000
print(lst[3][2])
lst[3][2].remove(2000)
print(lst)