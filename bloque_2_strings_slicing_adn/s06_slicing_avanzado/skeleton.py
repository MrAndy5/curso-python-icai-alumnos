# Sesión 06 - Skeleton

def decodificar_trama_teleco(trama: str) -> dict[str, str]:
    """
    Estructura de la trama:
    - Cabecera: primeros 4 caracteres
    - Origen: siguientes 4 caracteres
    - Destino: siguientes 4 caracteres
    - CRC: últimos 2 caracteres
    - Payload: todo lo que queda entre Destino y CRC
    
    Si len(trama) < 14, retorna diccionario vacío {}
    """
    # TODO: Implementar usando exclusivamente slicing
    pass

def es_palindromo_estricto(texto: str) -> bool:
    """Devuelve True si el texto se lee igual al revés ignorando mayúsculas/minúsculas y espacios"""
    # TODO: Limpiar espacios y comparar con reverso usando slicing [::-1]
    pass
