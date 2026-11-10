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
import pickle
from skeleton import calcular_pacientes_riesgo_csv, serializar_a_dat

def test_analisis_pacientes():
    datos = [
        "id,edad,colesterol,fumador",
        "101,60,250.0,1", # 24 + 12.5 + 15 = 51.5 (> 40)
        "102,20,150.0,0"  # 8 + 7.5 = 15.5 (<= 40)
    ]
    riesgos = calcular_pacientes_riesgo_csv(datos)
    assert len(riesgos) == 1
    assert riesgos[0]["id"] == 101
    assert riesgos[0]["score"] == 51.5
    
    # Comprobar serialización binaria a .dat
    b = serializar_a_dat(riesgos)
    recuperados = pickle.loads(b)
    assert recuperados[0]["score"] == 51.5
