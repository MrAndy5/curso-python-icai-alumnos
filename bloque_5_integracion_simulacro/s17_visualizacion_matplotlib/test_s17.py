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
from skeleton import preparar_datos_histograma

def test_preparacion_datos():
    balances = {101: 500.0, 102: -150.0, 103: 0.0}
    etiq, vals, cols = preparar_datos_histograma(balances)
    assert etiq == ["Cli_101", "Cli_102", "Cli_103"]
    assert vals == [500.0, -150.0, 0.0]
    assert cols == ["green", "red", "green"]
