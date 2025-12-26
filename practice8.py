# in this code we are learn the list in python
fruits = ['apple', 'banana' ,'cherry']
print(fruits)

fruits = ['apple', 'banana' ,'cherry' , 'date','oranges' , 'kiwi']
print(fruits)
print(fruits[3])
fruits[1] = 'blackcurrant'
print(fruits[-2])
print(fruits[-5])
print(fruits[1:4])
print(fruits[1::2])
print(fruits[:4])
print(fruits[:])

numbers = [10,20,30,40,50,60,70,80,90,100]          
print(numbers[1:4])
print(numbers[::3])
print(numbers[0::2])
print(numbers[-4::-2])
print(numbers[-1::-3])

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = list1 + list2
print(list3)
for x in list3: 
    list1.append(x)
print(list1)

list1.extend(list2)
print(list1)

# list comprehension 
squares = [x**2 for x in range(10,15)]
print(squares)











