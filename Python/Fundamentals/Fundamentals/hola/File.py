
num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #Data Types
string = 'Hello World'#Data Types
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#variable declaration
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration
print(type(fruit))#Dictionary
print(pizza_toppings[1])#Dictionary
pizza_toppings.append('Mushrooms')#Dictionary
print(person['name'])#Dictionary
person['name'] = 'George'#Dictionary #variable declaration
person['eye_color'] = 'blue'#Dictionary #variable declaration
print(fruit[2])#Dictionary

if num1 > 45:#conditional
    print("It's greater") #Dictionary
else: #conditional
    print("It's lower") #Dictionary

if len(string) < 5:     #conditional
    print("It's a short word!") #Dictionary
elif len(string) > 15:      #conditional
    print("It's a long word!")
else:           #conditional
    print("Just right!") #Dictionary

for x in range(5): #for loop
    print(x) #Dictionary
for x in range(2,5):    #for loop
    print(x) #Dictionary
for x in range(2,10,3): #for loop
    print(x) #Dictionary
x = 0   #variable
while(x < 5): #while loop
    print(x) #Dictionary
    x += 1  #variable

pizza_toppings.pop()    #Dictionary
pizza_toppings.pop(1)   #Dictionary

print(person)   #Dictionary
person.pop('eye_color') #Dictionary
print(person)   #Dictionary

for topping in pizza_toppings:      #for loop
    if topping == 'Pepperoni':      #conditional
        continue    #for loop
    print('After 1st if statement') #Dictionary
    if topping == 'Olives': #conditional
        break #for loop

def print_hello_ten_times():    #Dictionary
    for num in range(10): #for loop
        print('Hello')#Dictionary

print_hello_ten_times()#Dictionary

def print_hello_x_times(x):#Dictionary
    for num in range(x):    #for loop
        print('Hello')  #Dictionary

print_hello_x_times(4)  #Dictionary

def print_hello_x_or_ten_times(x = 10): #Dictionary #variable declaration
    for num in range(x):#for loop
        print('Hello')#Dictionary

print_hello_x_or_ten_times()    #Dictionary
print_hello_x_or_ten_times(4)   #Dictionary


