#In this code we will discuss functions in python 

# create or define function 
def greetings():
    print('welcome to python tutorial by gurjit')
    #call the function
    greetings()

#function to adds two numbers print result
def add2numbers(a,b):
    result = a + b
    print('the sum is:',result)
#calling this function with parameter 
add2numbers(5,7)

def add(a,b):
    return a + b #thjis line sends back sum a and b 
result = add(3,5)
print(result)

#function to convert celsius to fahrenheit 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit

#calling this function to return a value 
temp_f = celsius_to_fahrenheit(25)
print('temperature in fahrenheit is:' , temp_f)

def greetings(name):
    print('hello,'  + name  + '!')
greetings('gurjit')

def add_numbers(*args):
    return sum(args)
result = add_numbers(1,2,3,4,5,6)
print(result)

def greetings(*names):
    for name in names: 
         print(f"hello , {name}!")
greetings('gurjit', 'rajveer')

