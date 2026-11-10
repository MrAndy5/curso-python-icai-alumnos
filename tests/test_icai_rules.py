import os
import ast
import pytest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_student_code_files():
    target_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        if "venv" in root or ".pytest_cache" in root or "tests" in root or ".git" in root:
            continue
        for f in files:
            if f == "skeleton.py" or f == "examen_final_skeleton.py":
                target_files.append(os.path.join(root, f))
    return sorted(target_files)

@pytest.mark.parametrize("file_path", get_student_code_files())
def test_no_break_continue_while_true_in_student_code(file_path):
    """
    Verificación de Reglas de Oro de ICAI mediante Abstract Syntax Tree (AST):
    Certifica que el código del alumno no contiene 'break', 'continue' o 'while True'.
    
    Tolerancia cero en exámenes de programación estructurada (ICAI - GITT / IMAT).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)
        
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    for node in ast.walk(tree):
        assert not isinstance(node, ast.Break), (
            f"VIOLACIÓN REGLA ICAI: 'break' detectado en {rel_path} (Línea {node.lineno}). "
            "Sustitúyelo por una variable de control booleana (Flag / Centinela)."
        )
        assert not isinstance(node, ast.Continue), (
            f"VIOLACIÓN REGLA ICAI: 'continue' detectado en {rel_path} (Línea {node.lineno}). "
            "Reestructura la lógica con ramas if/else estructuradas."
        )
        if isinstance(node, ast.While):
            if isinstance(node.test, ast.Constant) and node.test.value is True:
                assert False, (
                    f"VIOLACIÓN REGLA ICAI: 'while True:' detectado en {rel_path} (Línea {node.lineno}). "
                    "Gobernar el bucle con un centinela: 'while not terminado:' o 'while condicion:'."
                )
