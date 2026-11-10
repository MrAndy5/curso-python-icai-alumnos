# Sesión 12 - Skeleton

def balance_consolidado_banco(clientes: dict[int, dict]) -> dict[int, float]:
    """
    clientes: {
        id_cliente: {
            'nombre': str,
            'saldo_inicial': float,
            'movimientos': list[float]
        }
    }
    
    Retorna un diccionario {id_cliente: saldo_final_redondeado_a_2_decimales}
    donde saldo_final = saldo_inicial + sum(movimientos)
    """
    # TODO: Iterar con .items() y calcular balances consolidados
    pass
