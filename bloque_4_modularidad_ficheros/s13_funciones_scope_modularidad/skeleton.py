# Sesión 13 - Skeleton (Lab 8 ICAI)

TABLA_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"

def obtener_letra_dni(numero: int) -> str:
    """Calcula la letra del DNI según el algoritmo oficial (numero % 23)"""
    # TODO: Validar que numero esté entre 0 y 99999999 y devolver la letra
    pass

def validar_dni_espanol(dni_completo: str) -> bool:
    """
    Valida un DNI en formato string (ej: '50820300K' o ' 12345678-Z ').
    - Elimina espacios y guiones.
    - Comprueba que tenga 8 dígitos y 1 letra final.
    - Comprueba que la letra coincida con el algoritmo de módulo 23.
    """
    # TODO: Implementar validación y llamada a obtener_letra_dni
    pass
