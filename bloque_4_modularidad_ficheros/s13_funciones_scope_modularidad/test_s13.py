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
from skeleton import obtener_letra_dni, validar_dni_espanol

def test_dni_valido():
    # 00000000 % 23 = 0 -> 'T'
    assert obtener_letra_dni(0) == 'T'
    assert validar_dni_espanol("00000000T") is True
    assert validar_dni_espanol(" 00000000-T ") is True

def test_dni_invalido():
    assert validar_dni_espanol("00000000R") is False
    assert validar_dni_espanol("1234A") is False
    assert validar_dni_espanol("ABCDEFGHZ") is False
