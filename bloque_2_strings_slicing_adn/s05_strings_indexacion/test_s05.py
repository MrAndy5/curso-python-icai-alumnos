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
from skeleton import suprimir_vocales

def test_frase_estandar():
    res = suprimir_vocales("Fundamentos de Programacion ICAI")
    assert res == "Fndmnts d Prgrmcn C"

def test_solo_vocales():
    assert suprimir_vocales("aeiouAEIOU") == ""

def test_sin_vocales():
    assert suprimir_vocales("HTML CSS") == "HTML CSS"
