import os
import sys
import pytest

if __name__ == "__main__":
    print("=" * 80)
    print("BATERÍA GLOBAL DE AUTOEVALUACIÓN Y AUDITORÍA DE REGLAS ICAI (ALUMNOS)")
    print("=" * 80)
    print("Ejecutando tests sobre tus archivos skeleton.py y examen_final_skeleton.py...")
    print("Nota: Los ejercicios no implementados todavía fallarán sus aserciones.\n")
    
    ret_code = pytest.main([
        "-v",
        os.path.join(os.path.dirname(__file__), "bloque_1_fundamentos_estructurados"),
        os.path.join(os.path.dirname(__file__), "bloque_2_strings_slicing_adn"),
        os.path.join(os.path.dirname(__file__), "bloque_3_estructuras_matrices"),
        os.path.join(os.path.dirname(__file__), "bloque_4_modularidad_ficheros"),
        os.path.join(os.path.dirname(__file__), "bloque_5_integracion_simulacro"),
        os.path.join(os.path.dirname(__file__), "tests", "test_icai_rules.py")
    ])
    
    print("\n" + "=" * 80)
    if ret_code == 0:
        print("¡EXCELENTE! TODOS LOS EJERCICIOS IMPLEMENTADOS PASAN Y CUMPLEN LAS REGLAS ICAI.")
    else:
        print("INFORME DE TESTS: Revisa arriba los casos que hayan fallado para depurar tu código.")
    print("=" * 80)
        
    sys.exit(ret_code)
