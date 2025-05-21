def siguiente_generacion(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    nueva_matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos = 0

           
            if j > 0:
                vecinos += matriz[i][j - 1]
            if j < columnas - 1:
                vecinos += matriz[i][j + 1]


            if matriz[i][j] == 1:
                if vecinos == 1 or vecinos == 2:
                    nueva_matriz[i][j] = 1  
                else:
                    nueva_matriz[i][j] = 0  
            else:
                if vecinos == 1:
                    nueva_matriz[i][j] = 1  
                else:
                    nueva_matriz[i][j] = 0  
    return nueva_matriz

def imprimir_tablero(matriz):
    for fila in matriz:
        print(fila)

matriz = [
    [0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0],
    [0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0]
]

print("Generación 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print("Generación 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print("Generación 2:")
imprimir_tablero(generacion_2)