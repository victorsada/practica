persona = {
    "nombre": "Juan",
    "edad": 16,
    "sexo": "masculino"
}

isAdult = persona["edad"] > 17

# if isAdult:
#     print("es mayor de edad")
# elif persona["edad"] == 15:
#   print("tiene 15 años")
# else:
#   print("es menor de edad")



# edad = 17
# mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
# print(mensaje)

if not persona["edad"]  > 18:
    print("eres menor de edad")


for x in range(1, 10):
    print(x)