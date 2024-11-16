# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     print(numero)  # Imprime cada número de la lista



# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1 # contador = contador + 1


personas = [{"nombre": "Juan", "edad": 20}, {"nombre": "Ana", "edad": 17}]

nombres=[]
for persona in personas:
  if persona["edad"] >= 18:
      nombres.append(persona["nombre"])

# print(nombres)
