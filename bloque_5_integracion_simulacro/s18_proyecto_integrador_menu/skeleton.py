# Sesión 18 - Skeleton (Proyecto Oficial 2024 ICAI)
# REGLA ICAI: Bucle de menú estructurado sin break, continue ni while True.

def crear_banco() -> dict[int, dict]:
    """Retorna un diccionario de banco vacío"""
    return {}

def insertar_cliente(banco: dict[int, dict], id_cli: int, nombre: str, password: str, saldo_inicial: float) -> bool:
    """
    Inserta un nuevo cliente en el banco.
    Estructura cliente: {'nombre': nombre, 'password': password, 'saldo': saldo_inicial}
    - Si el id_cli ya existe o saldo_inicial < 0, no se inserta y retorna False.
    - Si es válido, se inserta y retorna True.
    """
    # TODO: Implementar inserción segura
    pass

def cambiar_password(banco: dict[int, dict], id_cli: int, pass_antigua: str, pass_nueva: str) -> bool:
    """
    Cambia la contraseña si id_cli existe y pass_antigua coincide.
    Retorna True si cambió con éxito, False en caso contrario.
    """
    # TODO: Implementar cambio de contraseña
    pass

def realizar_transferencia(banco: dict[int, dict], origen: int, destino: int, cantidad: float) -> bool:
    """
    Transfiere 'cantidad' de la cuenta 'origen' a la cuenta 'destino'.
    Condiciones:
    - cantidad > 0
    - origen y destino deben existir en el banco
    - banco[origen]['saldo'] >= cantidad
    Retorna True si tuvo éxito, False en caso contrario.
    """
    # TODO: Implementar transferencia atómica
    pass
