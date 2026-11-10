# Sesión 02 - Skeleton
# REGLA ICAI: Prohibido break, continue o while True.

import math

def resolver_segundo_grado(a: float, b: float, c: float) -> tuple[str, list[float]]:
    """
    Resuelve la ecuación ax^2 + bx + c = 0.
    Retorna (tipo_solucion, lista_raices):
    - Si a == 0 y b == 0 y c == 0: ("Infinitas soluciones", [])
    - Si a == 0 y b == 0 y c != 0: ("Incompatible", [])
    - Si a == 0 y b != 0: ("Lineal", [-c / b])
    - Si a != 0:
        * discriminante > 0: ("Dos reales", [r1, r2]) ordenadas de mayor a menor
        * discriminante == 0: ("Doble", [r1])
        * discriminante < 0: ("Complejas", [])
    """
    # TODO: Implementar resolución estructurada completa
    pass
