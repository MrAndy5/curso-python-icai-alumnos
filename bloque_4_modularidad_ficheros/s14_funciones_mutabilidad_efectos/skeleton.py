# Sesión 14 - Skeleton (Lab 8.2 ICAI - Siete y Media)

def generar_baraja_espanola() -> list[tuple[str, float]]:
    """
    Genera una baraja de 40 cartas:
    Palos: Oros, Copas, Espadas, Bastos.
    Valores:
    - 1 al 7: su valor nominal (1.0 a 7.0 puntos)
    - 10 (Sota), 11 (Caballo), 12 (Rey): valen 0.5 puntos
    Retorna lista de tuplas ('Nombre Carta', puntos)
    """
    # TODO: Generar la baraja completa
    pass

def robar_carta(baraja: list[tuple[str, float]]) -> tuple[str, float]:
    """
    Extrae y retorna la primera carta de la baraja mutando in-place la lista.
    Si la baraja está vacía, retorna ('Sin cartas', 0.0)
    """
    # TODO: Extraer destructivamente el primer elemento
    pass
