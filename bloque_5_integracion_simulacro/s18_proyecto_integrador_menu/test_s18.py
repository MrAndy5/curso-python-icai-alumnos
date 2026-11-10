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
from skeleton import crear_banco, insertar_cliente, cambiar_password, realizar_transferencia

def test_operaciones_bancarias():
    banco = crear_banco()
    assert insertar_cliente(banco, 1, "Ines", "pass123", 1000.0) is True
    assert insertar_cliente(banco, 1, "Ines_Duplicada", "pass999", 500.0) is False # Duplicado
    assert insertar_cliente(banco, 2, "Pablo", "pass456", 200.0) is True
    
    # Cambio pass
    assert cambiar_password(banco, 1, "erronea", "nueva") is False
    assert cambiar_password(banco, 1, "pass123", "nueva_pass") is True
    assert banco[1]["password"] == "nueva_pass"
    
    # Transferencia
    assert realizar_transferencia(banco, 1, 2, 300.0) is True
    assert banco[1]["saldo"] == 700.0
    assert banco[2]["saldo"] == 500.0
    
    # Transferencia con saldo insuficiente
    assert realizar_transferencia(banco, 2, 1, 9999.0) is False
