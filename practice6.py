print('hello world')
print("you give me ")
print('''a triple quote''')
print("\"new line\" and  'single ' can be used.")

#formatted string 
name = 'gurjit' 
age = 18 
print('my name is %s and i am %d years old.' % (name, age))

name = 'gurjit' 
age = 18 
print(' my name is {} and i am {} .' .format(name, age))

name = 'gurjit' 
age = 18 
print(f'my name is {name} and i am {age} years old.')

#escape sequence 
print('hello \nworld') 
print('hello \tworld')

name = 'gurjit'
name[0:4] = 'gurj'
name[0:4:2] = 'gj'
name[5:] = 'it'
name[-3:] = 'jit'
name[::-1] = 'tijrug'
print(name)

