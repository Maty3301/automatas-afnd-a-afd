from include.reader import leer_csv, procesar_matriz, obtener_filas_columnas
from include.transiciones import transformarAutomataDeterministico, eliminarEstadosInalcanzables

def main():
    # Leer y procesar la matriz CSV
    file_path = 'afnd.csv'
    matriz_csv = leer_csv(file_path)
    filas, columnas = obtener_filas_columnas(matriz_csv)
    transiciones, diccionario_estados, diccionario_transiciones = procesar_matriz(matriz_csv)

    print("\nMatriz antes:")
    for fila in matriz_csv:
        print(fila)

    # Transformar el autómata no determinista a determinista
    matriz_output = transformarAutomataDeterministico(matriz_csv, transiciones, diccionario_estados, diccionario_transiciones)

    # Eliminar estados inalcanzables
    matriz_output = eliminarEstadosInalcanzables(matriz_output, columnas)

    # Mostrar la matriz final después de eliminar estados inalcanzables
    print("\nMatriz final:")
    for fila in matriz_output:
        print(fila)

if __name__ == "__main__":
    main()
