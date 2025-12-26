# In this code we are learn the looping statements in  python 
#Print numbers from 0 to 3 
count = 0 
while count < 4: 
    print(count)
    count+= 1

count = 3 
while count > 0: 
    print('countdown:' , count)
    count -= 1 
else: 
    print('liftoff!')

# for loop 
language = 'python' 
for x in language: 
    print(x) 

    for i in range(1,10,2): 
        print(i)
    else:    
        print('loop ended')

# pass statement 
for i in range(5): 
    pass 
print('end of program')
 
 #break statement 
for i in range(5): 
    if i ==3: 
        break
    print(i) 

# continue statement 
for i in range(5):
    if i ==3: 
        continue 
    print(i)

# nested loops 
for i in range(3):
    for j in range(1,4): 
        print(j) 
        print()

i = 1 
while i < 4: 
  for j in range(1,4): 
      print(j)
      i +=1 
