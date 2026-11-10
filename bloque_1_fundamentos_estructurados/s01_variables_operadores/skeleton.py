# Sesión 01 - Skeleton
# REGLA ICAI: Programación estructurada pura.

import math

def calcular_potencia_dbm(potencia_w: float) -> tuple[float, str]:
    """
    Calcula el nivel de señal en dBm dada la potencia en Vatios (W).
    Fórmula: P_dBm = 10 * log10(P_W / 0.001)
    
    Retorna una tupla: (p_dbm redondeada a 2 decimales, texto_formateado)
    El texto formateado debe tener la estructura exacta:
    'Potencia: %8.4f W | Nivel: %6.2f dBm' usando el operador %
    
    Si potencia_w <= 0.0, debe retornar (-999.0, "Potencia invalida")
    """
    # TODO: Implementar validación y cálculo
    pass

if __name__ == "__main__":
    dbm, txt = calcular_potencia_dbm(0.02)
    print("Resultado:", txt)
