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
from skeleton import analizar_temperaturas_lineas

def test_procesar_temperaturas():
    lineas = [
        "Lunes,10.0,20.0\n",
        "Martes,5.0,15.0\n",
        "Miercoles,8.0,22.0\n"
    ]
    t_min, t_max, avg = analizar_temperaturas_lineas(lineas)
    assert t_min == 5.0
    assert t_max == 22.0
    # Suma: 10+20+5+15+8+22 = 80 / 6 = 13.33
    assert avg == 13.33

def test_lineas_vacias():
    assert analizar_temperaturas_lineas([]) == (0.0, 0.0, 0.0)
