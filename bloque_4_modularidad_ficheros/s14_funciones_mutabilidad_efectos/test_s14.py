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
from skeleton import generar_baraja_espanola, robar_carta

def test_baraja_completa():
    mazo = generar_baraja_espanola()
    assert len(mazo) == 40
    # Primera carta es '1 de Oros' con 1.0 pt
    c1 = robar_carta(mazo)
    assert c1 == ("1 de Oros", 1.0)
    assert len(mazo) == 39 # Se mutó in-place

def test_mazo_vacio():
    vacio = []
    c = robar_carta(vacio)
    assert c == ("Sin cartas", 0.0)
