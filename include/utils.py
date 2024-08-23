import re

def transicionEsNoDeterminista(transicion):
    return "," in transicion

def separarEstados(transicion):
    return str(transicion).split(sep=',')

def unionEstadosTransiciones(estado_compuesto, transiciones, diccionario_transiciones):
    lista_estados = separarEstados(estado_compuesto)
    result = []

    for transicion in transiciones:
        nuevaTransicion = ""
        for estado in lista_estados:
            lista_tuplas_transiciones = diccionario_transiciones[estado]
            for t, q in lista_tuplas_transiciones:
                if t == transicion:
                    nuevaTransicion += q
                    break
        result.append((transicion, formatearTransicion(nuevaTransicion)))

    return result

def formatearTransicion(transicionSinFormatear):
    if all(char == '-' for char in transicionSinFormatear):
        return '-'
    
    if '-' in transicionSinFormatear:
        cadena_sin_guiones = transicionSinFormatear.replace('-', ',')
        estados = sorted(set(cadena_sin_guiones.split(',')))  # Eliminar duplicados y ordenar
        result = ','.join([s for s in estados if s])
        return result

    estados = sorted(set(re.sub(r'(\d)(Q)', r'\1,\2', transicionSinFormatear).split(',')))  # Eliminar duplicados y ordenar
    return ','.join(estados)