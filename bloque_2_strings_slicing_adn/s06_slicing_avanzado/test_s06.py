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
from skeleton import decodificar_trama_teleco, es_palindromo_estricto

def test_trama_valida():
    trama = "SYNC00010002HOLA_MUNDO7F"
    res = decodificar_trama_teleco(trama)
    assert res["cabecera"] == "SYNC"
    assert res["origen"] == "0001"
    assert res["destino"] == "0002"
    assert res["payload"] == "HOLA_MUNDO"
    assert res["crc"] == "7F"

def test_trama_corta():
    assert decodificar_trama_teleco("SYNC123") == {}

def test_palindromo():
    assert es_palindromo_estricto("Anita lava la tina") is True
    assert es_palindromo_estricto("Teleco ICAI") is False
