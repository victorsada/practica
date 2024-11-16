personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "hobbies": ["canto", "Ajedrez"], "trabajo": "programador", "genero": "masculino"},
    {"nombre": "Ana", "edad": 30, "ciudad": "Barcelona", "hobbies": ["lectura", "viajes"], "trabajo": "diseñadora", "genero": "femenino"},
    {"nombre": "Luis", "edad": 35, "ciudad": "Sevilla", "hobbies": ["videojuegos", "programacion"], "trabajo": "arquitecto", "genero": "masculino"},
    {"nombre": "Marta", "edad": 22, "ciudad": "Valencia", "hobbies": ["danza", "pintura"], "trabajo": "estudiante", "genero": "femenino"},
    {"nombre": "Raúl", "edad": 18, "ciudad": "Barcelona", "hobbies": ["baloncesto", "programacion"], "trabajo": "programador", "genero": "masculino"},
    {"nombre": "Carlos", "edad": 28, "ciudad": "Sevilla", "hobbies": ["música", "tenis"], "trabajo": "ingeniero", "genero": "masculino"},
    {"nombre": "Ana", "edad": 27, "ciudad": "Valencia", "hobbies": ["programacion", "fotografía"], "trabajo": "fotógrafa", "genero": "femenino"},
    {"nombre": "Pedro", "edad": 40, "ciudad": "Barcelona", "hobbies": ["historia", "videojuegos"], "trabajo": "historiador", "genero": "masculino"},
    {"nombre": "Pedro", "edad": 40, "ciudad": "Barcelona", "hobbies": ["historia", "videojuegos"], "trabajo": "historiador", "genero": "masculino"},
    {"nombre": "Elena", "edad": 32, "ciudad": "Sevilla", "hobbies": ["viajes", "moda"], "trabajo": "diseñadora", "genero": "femenino"},
    {"nombre": "Sofía", "edad": 20, "ciudad": "Sevilla", "hobbies": ["yoga", "canto"], "trabajo": "estudiante", "genero": "femenino"},
]




# 7. Obtener el promedio de edades
# Escribe una función que calcule y devuelva el promedio de las edades de todas las personas en la lista.

def promedioEdades ():
  promedioEdades=0
  totalEdades=0
  for persona in personas:
    totalEdades+=persona["edad"]
  promedioEdades=totalEdades/len(personas)    
  return promedioEdades

print (promedioEdades())






# Ejercicios
# 1. Filtrar personas menores de 20 años
# Escribe una función que reciba la lista y devuelva el nombre de todas las personas menores de 20 años.

# # def personasMenoresDeVeinte(paramPersonas):
#   resultado = []
#   for persona in paramPersonas:
#     if persona["edad"] <= 20:
#       resultado.append(persona["nombre"])
#   return resultado

# print(personasMenoresDeVeinte(personas))

