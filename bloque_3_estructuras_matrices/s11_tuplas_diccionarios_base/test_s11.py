import os
import sys
curr_dir = os.path.dirname(os.path.abspath(__file__))
if curr_dir not in sys.path:
    sys.path.insert(0, curr_dir)
if "skeleton" in sys.modules:
    del sys.modules["skeleton"]
if "examen_final_skeleton" in sys.modules:
    del sys.modules["examen_final_skeleton"]

import pytest
from skeleton import gestionar_inventario

def test_gestion_pedidos():
    stock_inicial = {"Router": 10, "Switch": 5, "Cable": 100}
    pedidos = [("Router", 3), ("Switch", 8), ("Fibra", 10)]
    
    nuevo_stock = gestionar_inventario(stock_inicial, pedidos)
    assert nuevo_stock["Router"] == 7
    assert nuevo_stock["Switch"] == 0 # Se agotó
    assert nuevo_stock["Cable"] == 100 # Intacto
    assert "Fibra" not in nuevo_stock
    # Verificar no mutabilidad
    assert stock_inicial["Router"] == 10
