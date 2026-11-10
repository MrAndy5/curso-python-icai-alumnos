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
import math
from skeleton import aproximar_seno_taylor

def test_seno_pi_sextos():
    # sen(pi/6) = 0.5
    x = math.pi / 6.0
    aprox = aproximar_seno_taylor(x, 5)
    assert aprox == 0.5

def test_seno_cero():
    assert aproximar_seno_taylor(0.0, 3) == 0.0

def test_seno_pi_medios():
    # sen(pi/2) = 1.0
    x = math.pi / 2.0
    aprox = aproximar_seno_taylor(x, 8)
    assert abs(aprox - 1.0) < 1e-4
