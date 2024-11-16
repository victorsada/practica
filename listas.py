arr = [1,2,3,4]
#  .append: agregar un elemento a la lista
# arr.append(5) # [1,2,3,4,5]

# .extend(lista): concatenar una lista con otro lista 
# arr.extend([5,6]) # [1,2,3,4,5,6]

# .insert(indexToAdd, element): agregar un elemento en una posicion especifica: 
# arr.insert(3, "a") # [1,2,3,"a",4]

# .pop(): Elimina el ultimo elemento de una lista, y lo retorna: 
# opcional, le puedes pasar como parametro el index a eliminar
# indexToRemove = 2
# arr.pop(indexToRemove) # [1,2,4]

# .remove(valueToRemove): Elimina el elemento que coincida con el valor: 
# valueToRemove = 4
# arr.remove(valueToRemove) # [1,2,3]

# .count(valueToCount): Devuelve cuántas veces aparece un elemento en la lista. 
# print(arr.count(2)) # 1 --> el dos aparece una sola vez

#reverse() Invierte el orden de los elementos en la lista (modifica la lista original).
# arr.reverse()

# para verificar si existe un elemento dentro de una lista
# print(5 in arr)

# len() cuantos elementos tiene la lista
# len(arr)

# print(arr)