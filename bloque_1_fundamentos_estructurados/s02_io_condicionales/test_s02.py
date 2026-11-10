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
from skeleton import resolver_segundo_grado

def test_dos_reales():
    # x^2 - 5x + 6 = 0 -> raices 3.0, 2.0
    tipo, raices = resolver_segundo_grado(1.0, -5.0, 6.0)
    assert tipo == "Dos reales"
    assert raices == [3.0, 2.0]

def test_raiz_doble():
    # x^2 - 4x + 4 = 0 -> raiz 2.0
    tipo, raices = resolver_segundo_grado(1.0, -4.0, 4.0)
    assert tipo == "Doble"
    assert raices == [2.0]

def test_complejas():
    tipo, raices = resolver_segundo_grado(1.0, 0.0, 1.0)
    assert tipo == "Complejas"
    assert raices == []

def test_lineal():
    tipo, raices = resolver_segundo_grado(0.0, 2.0, -8.0)
    assert tipo == "Lineal"
    assert raices == [4.0]
