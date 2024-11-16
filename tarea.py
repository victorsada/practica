personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "hobbies": ["canto", "ajedrez"], "trabajo": "programador", "genero": "masculino"},
    {"nombre": "Ana", "edad": 30, "ciudad": "Barcelona", "hobbies": ["lectura", "viajes"], "trabajo": "diseñadora", "genero": "femenino"},
    {"nombre": "Luis", "edad": 35, "ciudad": "Sevilla", "hobbies": ["videojuegos", "programacion"], "trabajo": "arquitecto", "genero": "masculino"},
    {"nombre": "Marta", "edad": 22, "ciudad": "Valencia", "hobbies": ["danza", "pintura"], "trabajo": "estudiante", "genero": "femenino"},
    {"nombre": "Raúl", "edad": 18, "ciudad": "Barcelona", "hobbies": ["baloncesto", "programacion"], "trabajo": "programador", "genero": "masculino"},
    {"nombre": "Carlos", "edad": 28, "ciudad": "Sevilla", "hobbies": ["música", "tenis"], "trabajo": "ingeniero", "genero": "masculino"},
    {"nombre": "Ana", "edad": 27, "ciudad": "Valencia", "hobbies": ["programacion", "fotografía"], "trabajo": "fotógrafa", "genero": "femenino"},
    {"nombre": "Pedro", "edad": 40, "ciudad": "Barcelona", "hobbies": ["historia", "videojuegos"], "trabajo": "historiador", "genero": "masculino"},
    {"nombre": "Elena", "edad": 32, "ciudad": "Sevilla", "hobbies": ["viajes", "moda"], "trabajo": "diseñadora", "genero": "femenino"},
    {"nombre": "Sofía", "edad": 19, "ciudad": "Sevilla", "hobbies": ["yoga", "canto"], "trabajo": "estudiante", "genero": "femenino"},
]


# Ejercicios
# 1. Filtrar personas menores de 20 años
# Escribe una función que reciba la lista y devuelva el nombre de todas las personas excepto las menores de 20 años.
def eliminarPersonasMenoresVeinteAnos(personas):
  mayoresDeVeinte = []
  for persona in personas:
    if persona["edad"] > 19:
      mayoresDeVeinte.append(persona["nombre"])
    else:
      pass
  return mayoresDeVeinte

# print(eliminarPersonasMenoresVeinteAnos(personas))

# 2. Obtener todas las ciudades
# Escribe una función que devuelva una lista de las ciudades (sin duplicados) de las personas en la lista.
def obtenerCiudadesSinDuplicado(personas):
  ciudades = []
  for persona in personas:
    if persona["ciudad"] not in ciudades:
      ciudades.append(persona["ciudad"])
  
  return ciudades

# print(obtenerCiudadesSinDuplicado(personas))

# 3. Contar cuántas personas tienen un hobby específico
# Escribe una función que reciba un hobby como parámetro y devuelva cuántas personas tienen ese hobby.
def cuantasPersonasPorHobby(hobby):
  cuenta = 0
  for persona in personas:
    if hobby in persona["hobbies"]:
      cuenta = cuenta + 1
  
  return cuenta

# print(cuantasPersonasPorHobby(input("indica un hobby: ")))

# 4. Encontrar a la persona más joven
# Escribe una función que devuelva el objeto de la persona más joven de la lista.
def obtenerMasJoven(personas):
  personaMasJoven = {}
  for persona in personas:
    if len(personaMasJoven.keys()) == 0:
      personaMasJoven = persona
    elif personaMasJoven["edad"] > persona["edad"]:
      personaMasJoven = persona
    else:
      pass
      
  return personaMasJoven

# print(obtenerMasJoven(personas))

# 5. Ordenar la lista por edad
# Escribe una función que ordene la lista de personas de menor a mayor edad y devuelva el nombre solamente.
# lambda a, b: a + b --------------> def sumar(a,b): return a + b

def ordenarPersonasDeMenorAMayor(personas):
  personasOrdenadas = sorted(personas, key=lambda persona: persona["edad"]) # sorted(iterable, key=funcion que devuelve el criterio a ordenar)
  resultado = []
  for persona in personasOrdenadas:
    resultado.append(persona["nombre"])
  return resultado

# print(ordenarPersonasDeMenorAMayor(personas))

# 6. Agregar un nuevo hobby a una persona
# Escribe una función que reciba un nombre y un hobby, y agregue ese hobby al objeto de la persona con ese nombre.
# al final prueba repitiendo un nombre en la lista y a ese nombre deberia agregarse tambien el hobby
# y despues arregla la funcion de manera tal que se agregue el hobby solamente a la primer persona que encuentre, incluso si hay mas personas con el mismo nombre
def agregarHobbyAPersona(nombre, hobby):
  for persona in personas:
    if nombre == persona["nombre"]:
      persona["hobbies"].append(hobby)
    else:
      pass

# agregarHobbyAPersona("Ana", "Dormir")
# print(personas)

# 7. Obtener el promedio de edades
# Escribe una función que calcule y devuelva el promedio de las edades de todas las personas en la lista.
def caluclarPromedioDeEdad(personas):
  totalEdades = 0
  for persona in personas:
    totalEdades = totalEdades + persona["edad"]
  
  return totalEdades / len(personas)

# print(caluclarPromedioDeEdad(personas))

# 8. Agrupar personas por ciudad
# Escribe una función que agrupe las personas por ciudad y devuelva un nuevo diccionario donde la clave sea la ciudad y el valor sea una lista de personas de esa ciudad.
def obtenerPersonasPorCiudad(personas):
  resultado = {}
  for persona in personas:
    if persona["ciudad"] not in resultado:
      resultado[persona["ciudad"]] = [persona["nombre"]]
    else:
      resultado[persona["ciudad"]].append(persona["nombre"])
  
  return resultado

# print(obtenerPersonasPorCiudad(personas))

# 9. Filtrar nombre de personas entre 25 y 30 años
# Escribe una función que reciba la lista y devuelva solo las personas mayores de 30 años.
def personasEntreVeinticinoYTreinta(personas):
  resultado = []
  for persona in personas:
    if persona["edad"] > 24 and persona["edad"] < 31:
      resultado.append(persona["nombre"])
  return resultado

# print(personasEntreVeinticinoYTreinta(personas))

# 10. Obtener hobbies únicos
# Escribe una función que devuelva una lista de todos los hobbies únicos (sin repetidos) de las personas.
def obtenerHobbies(personas):
  hobbies = []
  for persona in personas:
    for hobby in persona["hobbies"]:
      if hobby not in hobbies:
        hobbies.append(hobby)
  
  return hobbies

# print(obtenerHobbies(personas))

#11. Encontrar a todas las personas de un género específico
# Escribe una función que reciba un género ("masculino" o "femenino") y devuelva una lista con los nombres de las personas de ese género.

# 12. Filtrar personas por trabajo
# Escribe una función que reciba el nombre de un trabajo y devuelva cuántas personas tienen ese trabajo.

# 13. Contar personas de cada ciudad
# Escribe una función que devuelva un diccionario donde la clave sea el nombre de la ciudad y el valor sea la cantidad de personas que viven allí.

# 14. Promedio de edad por género
# Escribe una función que calcule y devuelva el promedio de edades de hombres y mujeres por separado.

# 15. Personas con más de un hobby
# Escribe una función que devuelva una lista con los nombres de las personas que tienen más de un hobby.

# 16. Obtener la persona más mayor por ciudad
# Escribe una función que reciba el nombre de una ciudad y devuelva el objeto de la persona más mayor que vive en esa ciudad.

# 17. Personas que comparten un hobby
# Escribe una función que reciba el nombre de un hobby y devuelva una lista con los nombres de las personas que lo tienen.

# 18. Agrupar personas por trabajo (DRY)
# Escribe una función que agrupe a las personas por su trabajo en un diccionario, donde la clave sea el trabajo y el valor sea una lista con los nombres de las personas.

# 19. Obtener personas que estudian
# Escribe una función que devuelva una lista con los nombres de las personas que estudian

# 20. Top 3 de ciudades con más personas
# Escribe una función que devuelva una lista con las tres ciudades que tienen más habitantes

def topTresCiudades(personas):
  contadorCiudades = {}
  for persona in personas:
    if persona["ciudad"] not in contadorCiudades:
      contadorCiudades[persona["ciudad"]] = 1
    else:
      contadorCiudades[persona["ciudad"]] += 1
  
  ciudadesOrdenadas = sorted(contadorCiudades.items(), key=lambda x: x[1], reverse=True)
  topTres = ciudadesOrdenadas[0:3]
  resultado = []
  for ciudad in topTres:
    resultado.append(ciudad[0])
  return resultado
  
  
# print(topTresCiudades(personas))