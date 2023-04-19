x = [ [5,2,3], [10,8,9] ] 
x[1][0]= 15
print(x)

#Cambiar Apellido

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]


print(estudiantes[0])


#CAMBIAR VALORES




directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

z[0]['y']=30
print(z)



#Iterar a traves de una lista de diccionarios





estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def  interateDictionary(estudiantes):

        for i in range(len(estudiantes) - len(estudiantes), len (estudiantes)):
                for key, value in estudiantes[i].items():
                        print(value)
                return True 
        print(interateDictionary(estudiantes))

        

#OBTENER VALORES DE UNA LISTA DE DICCIONARIOS

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def  interateDictionary(estudiantes, name):

        for i in range(len(estudiantes) - len(estudiantes), len (estudiantes)):
            for key, value in estudiantes[name].items():
                        print(value)
           
        print(interateDictionary(estudiantes))


dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print((dojo))


