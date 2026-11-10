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
from skeleton import clasificar_calificaciones

def test_clasificacion_completa():
    notas = [7.5, 4.0, 9.2, 3.5, 5.0, 6.8]
    apr, susp, avg = clasificar_calificaciones(notas, umbral=5.0)
    assert apr == [5.0, 6.8, 7.5, 9.2]
    assert susp == [3.5, 4.0]
    assert avg == 6.0
    # Comprobar que notas original no mutó
    assert notas == [7.5, 4.0, 9.2, 3.5, 5.0, 6.8]

def test_lista_vacia():
    assert clasificar_calificaciones([]) == ([], [], 0.0)
