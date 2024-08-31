# Creamos una matriz bidimensional de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si se encuentra
    return None  # Retorna None si no se encuentra

# Valor que deseas buscar
valor_a_buscar = 5

# Llamada a la función de búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Verificamos si se encontró el valor
if posicion:
    print(f"Valor {valor_a_buscar} encontrado en la posición {posicion}.")
else:
    print(f"Valor {valor_a_buscar} no se encuentra en la matriz.")