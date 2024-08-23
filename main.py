from include.reader import leer_csv, obtener_datos_matriz, obtener_columnas_matriz
from include.transiciones import (
    transformar_automata_deterministico,
    eliminar_estados_inalcanzables,
)


def main():
    matriz_csv = leer_csv("afnd.csv")
    lista_transiciones, diccionario_estados, diccionario_transiciones = (
        obtener_datos_matriz(matriz_csv)
    )

    print("\nTabla de Automatas Finitos No Deterministico:")
    for fila in matriz_csv:
        print(fila)

    matriz_resultado = transformar_automata_deterministico(
        matriz_csv, lista_transiciones, diccionario_estados, diccionario_transiciones
    )

    matriz_resultado = eliminar_estados_inalcanzables(
        matriz_resultado, obtener_columnas_matriz(matriz_csv)
    )

    print("\nTabla de Automatas Finitos Deterministico:")
    for fila in matriz_resultado:
        print(fila)


if __name__ == "__main__":
    main()
