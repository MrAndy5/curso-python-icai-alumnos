# Sesión 11 - Skeleton

def gestionar_inventario(stock_actual: dict[str, int], pedidos: list[tuple[str, int]]) -> dict[str, int]:
    """
    stock_actual: {nombre_componente: unidades_en_almacen}
    pedidos: lista de tuplas (nombre_componente, unidades_pedidas)
    
    Para cada pedido:
    - Si el componente existe en stock y hay suficientes unidades: se restan.
    - Si hay menos unidades de las pedidas: se sirve lo que quede (llega a 0).
    - Si el componente no existe: se ignora el pedido.
    
    Retorna el stock_actual actualizado sin mutar el diccionario recibido.
    """
    # TODO: Copiar diccionario y procesar pedidos
    pass
