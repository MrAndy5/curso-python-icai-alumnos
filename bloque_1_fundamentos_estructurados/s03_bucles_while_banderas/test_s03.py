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
from skeleton import analizar_numeros_singulares

def test_examen_caso_oficial():
    # 8 (singular), 9 ((8)/1 != 9 -> NO), 4 ((8+9)/2 = 8.5 != 4 -> NO), 7 ((8+9+4)/3 = 7 -> SI), 0 (fin)
    datos = [8, 9, 4, 7, 0]
    res = analizar_numeros_singulares(datos)
    assert res == [
        "El numero 8 es singular",
        "El numero 9 NO es singular",
        "El numero 4 NO es singular",
        "El numero 7 es singular"
    ]

def test_cero_inmediato():
    res = analizar_numeros_singulares([0])
    assert res == []
