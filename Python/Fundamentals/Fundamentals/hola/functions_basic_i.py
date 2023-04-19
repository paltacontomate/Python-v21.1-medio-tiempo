#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#1  La respuesta de print va a ser igual a la declaracion de numero_de_grupos_alimentarios =(5)

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#2 El Print number_of_days_in_a_week_silicon_or_triangle_sides da error porque no cuenta como variable

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#3 Se ejecuta el print de la variable number_of_books_on_hold y se imprime 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#4 Agregan un print(10) al final de la función number_of_fingers

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#5  Ponen un print(5) al final de la función number_of_great_lakes y una variable x


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#6 declara la función add con dos parámetros, b y c 



#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#7 establece la función concatenate con dos parámetros, b y c 

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#8 toma el parametro b de la función number_of_oceans_or_fingers y devuelve el valor 5, consecutivamente imprime el valor 100 y 10
 
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#9 al ejecutar el print de la variable number_of_days_in_a_week_silicon_ da como resultado el valor 7 y el valor 14 = 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#10 declara la función addition con dos parámetros, b y c imprimiendo como resultado el valor 3 y el valor 5 = 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#11 imprime declara la función foobar y imprime el valor 500,500,300,500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#12 imprime declara la función foobar y imprime el valor 500,500,300,500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#13 se hace un return de la función foobar y imprime el valor 500,500

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#14 imprime los numeros 1,2 y 3

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#15 imprime los numeros 1,3,5 y 10