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
from skeleton import balance_consolidado_banco

def test_balance_clientes():
    banco = {
        101: {"nombre": "Ines", "saldo_inicial": 1000.0, "movimientos": [250.0, -100.0, -50.0]},
        102: {"nombre": "Carlos", "saldo_inicial": 500.0, "movimientos": [-600.0]},
        103: {"nombre": "Marta", "saldo_inicial": 120.0, "movimientos": []}
    }
    res = balance_consolidado_banco(banco)
    assert res[101] == 1100.0
    assert res[102] == -100.0
    assert res[103] == 120.0
