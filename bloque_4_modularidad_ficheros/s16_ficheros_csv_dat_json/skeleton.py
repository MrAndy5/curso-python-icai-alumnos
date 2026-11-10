# Sesión 16 - Skeleton (Lab 9.2 y Proyecto 2024 ICAI)

import pickle

def calcular_pacientes_riesgo_csv(filas_csv: list[str]) -> list[dict]:
    """
    filas_csv: lista de líneas en formato 'ID,EDAD,COLESTEROL,FUMADOR(1/0)'
    La primera línea es la cabecera 'id,edad,colesterol,fumador'.
    
    Fórmula de score de riesgo:
    score = (edad * 0.4) + (colesterol * 0.05) + (15.0 si es fumador else 0.0)
    
    Retorna una lista de diccionarios con los pacientes cuyo score sea > 40.0:
    [{'id': int, 'edad': int, 'score': float redondeado a 1 decimal}]
    """
    # TODO: Saltar cabecera, parsear campos y filtrar
    pass

def serializar_a_dat(datos: any) -> bytes:
    """Simula el volcado a fichero .dat retornando los bytes usando pickle.dumps()"""
    # TODO: Retornar pickle.dumps(datos)
    pass
