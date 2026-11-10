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
from skeleton import subsecuencia_mas_larga_sin_t

def test_ejemplo_examen_oficial():
    secuencia = ['C', 'G', 'G', 'T', 'A', 'C', 'C', 'G', 'A', 'T', 'G', 'T', 'G']
    sub, lon, idx = subsecuencia_mas_larga_sin_t(secuencia)
    assert sub == "ACCGA"
    assert lon == 5
    assert idx == 4

def test_secuencia_completa_examen_2023():
    secuencia = [
        'C', 'A', 'G', 'G', 'T', 'G', 'A', 'C', 'A', 'A', 
        'C', 'C', 'G', 'G', 'A', 'C', 'C', 'T', 'G', 'A', 
        'T', 'G', 'T', 'G', 'T', 'T', 'A', 'G', 'T', 'T', 
        'G', 'T', 'C', 'G', 'A', 'G', 'C', 'A', 'A', 'T', 
        'G', 'A', 'T', 'A', 'C', 'T', 'G', 'G', 'A', 'T', 
        'T', 'T', 'C', 'T', 'C', 'A', 'C', 'T', 'G', 'G'
    ]
    sub, lon, idx = subsecuencia_mas_larga_sin_t(secuencia)
    # Entre idx 5 y 16 hay 12 caracteres sin T: 'GACAACCGGACC'
    assert lon == 12
    assert idx == 5
    assert sub == "GACAACCGGACC"
