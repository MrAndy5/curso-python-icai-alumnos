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
from skeleton import calcular_potencia_dbm

def test_potencia_valida():
    dbm, txt = calcular_potencia_dbm(0.001) # 1 mW -> 0 dBm
    assert dbm == 0.0
    assert "0.00 dBm" in txt

def test_potencia_20mw():
    dbm, txt = calcular_potencia_dbm(0.02) # 20 mW -> 13.01 dBm
    assert dbm == 13.01
    assert "Potencia:   0.0200 W | Nivel:  13.01 dBm" == txt

def test_potencia_invalida():
    dbm, txt = calcular_potencia_dbm(-0.5)
    assert dbm == -999.0
    assert txt == "Potencia invalida"
