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
from skeleton import es_matriz_simetrica, calcular_traza_matriz

def test_matriz_simetrica():
    m = [
        [1, 5, 9],
        [5, 2, -3],
        [9, -3, 7]
    ]
    assert es_matriz_simetrica(m) is True
    assert calcular_traza_matriz(m) == 10.0

def test_matriz_no_simetrica():
    m = [
        [1, 2],
        [3, 4]
    ]
    assert es_matriz_simetrica(m) is False

def test_no_cuadrada():
    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert es_matriz_simetrica(m) is False
