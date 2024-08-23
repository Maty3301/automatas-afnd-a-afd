from .utils import separarEstados, formatearTransicion, transicionEsNoDeterminista

def unionEstadosTransiciones(estado_compuesto, transiciones, diccionario_transiciones):
    lista_estados = separarEstados(estado_compuesto)
    result = []

    for transicion in transiciones:
        nuevaTransicion = ""

        for estado in lista_estados:
            lista_tuplas_transiciones = diccionario_transiciones[estado]

            for t, q in lista_tuplas_transiciones: # t = transicion, q = estado
                if t == transicion:
                    nuevaTransicion += q
                    break

        result.append((transicion, formatearTransicion(nuevaTransicion)))

    return result

def transformarAutomataDeterministico(matriz, transiciones, diccionario_estados, diccionario_transiciones):
    columnas = len(matriz[0]) if len(matriz) > 0 else 0
    matriz_output = [fila.copy() for fila in matriz]
    estados_procesados = {fila[0] for fila in matriz_output}

    i = 1
    while i < len(matriz_output):
        for j in range(1, columnas-1):
            estado_actual = matriz_output[i][j]
            if transicionEsNoDeterminista(estado_actual):
                result = unionEstadosTransiciones(estado_actual, transiciones, diccionario_transiciones)
                nuevo_estado_compuesto = ",".join(sorted(separarEstados(estado_actual)))

                if nuevo_estado_compuesto not in estados_procesados:
                    nuevoEstado = [formatearTransicion(nuevo_estado_compuesto)]
                    nuevoEstado.append(result[0][1])
                    nuevoEstado.append(result[1][1])

                    F = any(diccionario_estados[estado] for estado in separarEstados(nuevo_estado_compuesto))
                    nuevoEstado.append(int(F))

                    matriz_output.append(nuevoEstado)
                    estados_procesados.add(nuevo_estado_compuesto)

        i += 1

    return matriz_output

def eliminarEstadosInalcanzables(matriz_output, columnas):
    # Asumamos que el estado inicial es el que está en matriz_output[1][0]
    estado_inicial = matriz_output[1][0]

    # Set para almacenar los estados alcanzables
    alcanzables = set()
    alcanzables.add(estado_inicial)

    # Cola para realizar un recorrido en amplitud (BFS) desde el estado inicial
    cola = [estado_inicial]

    while cola:
        estado_actual = cola.pop(0)
    
        # Busca las transiciones desde este estado
        for i in range(1, len(matriz_output)):
            if matriz_output[i][0] == estado_actual:
                for j in range(1, columnas-1):
                    estado_siguiente = matriz_output[i][j]
                    # Si el estado de destino no ha sido visitado, lo añadimos a la cola
                    if estado_siguiente not in alcanzables and estado_siguiente != '':
                        alcanzables.add(estado_siguiente)
                        cola.append(estado_siguiente)

    # Crear una nueva matriz que solo contenga los estados alcanzables
    nueva_matriz_output = []

    for i in range(1, len(matriz_output)):
        if matriz_output[i][0] in alcanzables:
            nueva_matriz_output.append(matriz_output[i])
        else:
            print("\nEliminando estado inalcanzable: ", matriz_output[i][0])

    # Reemplazamos matriz_output con la nueva matriz
    return nueva_matriz_output