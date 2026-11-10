# Sesión 17 - Skeleton (Proyecto 2024 ICAI)
import matplotlib.pyplot as plt

def preparar_datos_histograma(balances_dict: dict[int, float]) -> tuple[list[str], list[float], list[str]]:
    """
    Recibe un diccionario {id_cliente: balance_euros}.
    Retorna una tupla de 3 listas:
    1. etiquetas: lista de strings con formato 'Cli_XXX'
    2. valores: lista de saldos (floats)
    3. colores: 'green' si el saldo >= 0, 'red' si saldo < 0
    """
    # TODO: Generar las 3 listas requeridas
    pass

def renderizar_grafico_balances(etiquetas: list[str], valores: list[float], colores: list[str], ruta_guardado: str = "") -> None:
    """Configura y guarda o muestra el gráfico de barras"""
    plt.figure(figsize=(7, 4))
    plt.bar(etiquetas, valores, color=colores, edgecolor='black')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title("Estado de Cuentas - ICAI Finance")
    plt.xlabel("Clientes")
    plt.ylabel("Saldo (€)")
    plt.grid(True, linestyle=':', alpha=0.6)
    if ruta_guardado:
        plt.savefig(ruta_guardado)
    plt.close()
