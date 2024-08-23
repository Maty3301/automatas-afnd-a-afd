import csv

def leer_csv(directorio_archivo):
    with open(directorio_archivo, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')
        matriz = [fila for fila in lector_csv]
    return matriz

def obtener_filas_matriz(matriz):
    return len(matriz)

def obtener_columnas_matriz(matriz):
    return len(matriz[0]) if obtener_filas_matriz(matriz) > 0 else 0

def obtener_datos_matriz(matriz):
    filas = obtener_filas_matriz(matriz)
    columnas = obtener_columnas_matriz(matriz)
    lista_transiciones = []
    diccionario_estados = {}
    diccionario_transiciones = {}

    for i in range(1, columnas-1):
        lista_transiciones.append(matriz[0][i])
                
    for i in range(1, filas):
        diccionario_estados[matriz[i][0]] = int(matriz[i][columnas-1])

    for i in range(1, filas):
        transiciones_de_un_estado = []
        for j in range(1, columnas-1):
            transiciones_de_un_estado.append( (lista_transiciones[j-1], matriz[i][j]) )
        diccionario_transiciones[matriz[i][0]] = transiciones_de_un_estado

    return lista_transiciones, diccionario_estados, diccionario_transiciones