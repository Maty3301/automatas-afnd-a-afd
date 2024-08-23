import csv

def leer_csv(file_path):
    with open(file_path, 'r') as archivo:
        lector_csv = csv.reader(archivo, delimiter=';')
        matriz = [fila for fila in lector_csv]
    return matriz

def obtener_filas_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    return filas, columnas

def procesar_matriz(matriz):
    filas, columnas = obtener_filas_columnas(matriz)
    transiciones = []
    diccionario_estados = {}
    diccionario_transiciones = {}

    for i in range(1, columnas-1):
        transiciones.append(matriz[0][i])
                
    for i in range(1, filas):
        diccionario_estados[matriz[i][0]] = int(matriz[i][columnas-1])

    for i in range(1, filas):
        transiciones_de_un_estado = []
        for j in range(1, columnas-1):
            transiciones_de_un_estado.append( (transiciones[j-1], matriz[i][j]) )
        diccionario_transiciones[matriz[i][0]] = transiciones_de_un_estado

    return transiciones, diccionario_estados, diccionario_transiciones