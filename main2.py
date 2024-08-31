# Creamos una matriz bidimensional de 3x3
matriz = [
    [9, 2, 7],
    [4, 5, 6],
    [3, 8, 1]
]

# Función para ordenar una fila específica en orden ascendente
def ordenar_fila(matriz, fila):
    matriz[fila].sort()

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegimos la fila que queremos ordenar
fila_a_ordenar = 1  # La segunda fila (índice 1)

# Llamada a la función de ordenación
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz después de ordenar la fila
print("\nMatriz después de ordenar la fila:")
for fila in matriz:
    print(fila)