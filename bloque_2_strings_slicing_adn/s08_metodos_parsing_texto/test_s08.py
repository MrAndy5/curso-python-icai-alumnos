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
from skeleton import extraer_telefonos_validos

def test_extraccion_telefonos():
    texto = "# 612345678 # ERROR_LOG # 915422800 # 1234 # 699887766 # INES #"
    res = extraer_telefonos_validos(texto)
    assert res == ["612345678", "915422800", "699887766"]

def test_sin_telefonos():
    assert extraer_telefonos_validos("ALERTA#FALLO#CONEXION") == []
