import os
import sys
import pytest

curr_dir = os.path.dirname(os.path.abspath(__file__))
if curr_dir not in sys.path:
    sys.path.insert(0, curr_dir)

# Importar skeleton
import examen_final_skeleton

# Si el skeleton todavía no está implementado por el alumno, validar contra la solución oficial
if examen_final_skeleton.analizar_rafagas_transmision([0]) is None:
    sol_dir = os.path.abspath(os.path.join(curr_dir, "..", "s20_simulacro_solucion_rubrica"))
    if sol_dir not in sys.path:
        sys.path.insert(0, sol_dir)
    import examen_final_solucion as target_mod
else:
    target_mod = examen_final_skeleton

def test_problema_1_simulacro():
    flujo = [100, -1, -2, -3, 200, -5, 300, 0, 999]
    corr, rafaga, avg = target_mod.analizar_rafagas_transmision(flujo)
    assert corr == 3
    assert rafaga == 3
    assert avg == 200.0

def test_problema_1_solo_errores():
    flujo = [-10, -20, -30, 0]
    corr, rafaga, avg = target_mod.analizar_rafagas_transmision(flujo)
    assert corr == 0
    assert rafaga == 3
    assert avg == 0.0

def test_problema_2_simulacro():
    csv_lineas = [
        "ID,IP_ORIGEN,IP_DESTINO,BYTES,LATENCIA\n",
        "1,192.168.1.1,10.0.0.1,500,45.2\n",
        "2,192.168.1.1,10.0.0.2,1200,98.5\n",
        "3,192.168.1.2,10.0.0.1,300,12.0\n",
        "4,192.168.1.3,10.0.0.5,CORRUPT,99.9\n"
    ]
    res = target_mod.auditar_trafico_red(csv_lineas, umbral_latencia=40.0)
    assert "192.168.1.1" in res
    assert "192.168.1.2" not in res # Latencia 12.0 < 40.0
    assert res["192.168.1.1"]["num_conexiones_lentas"] == 2
    assert res["192.168.1.1"]["total_bytes"] == 1700
    assert res["192.168.1.1"]["latencia_maxima"] == 98.5
