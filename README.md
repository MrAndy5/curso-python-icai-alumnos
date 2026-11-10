# Curso Intensivo de Python (20 Horas) - Ejercicios y Esqueletos para Alumnos
### Escuela Técnica Superior de Ingeniería (ICAI) - Universidad Pontificia Comillas
**Grados:** Grado en Ing. de Tecnologías de Telecomunicación (GITT) & Grado en Ing. Matemática e Inteligencia Artificial (IMAT)

---

## 📌 Bienvenida y Propósito del Repositorio

Bienvenido al repositorio oficial de trabajo del **Curso Intensivo de Python (20h)** de ICAI. Este repositorio ha sido preparado especialmente para que dispongas de todos los **enunciados**, **esqueletos de código (*skeletons*)**, **ficheros de datos** y **baterías de tests de autoevaluación** para las 20 sesiones del curso.

El temario unifica las exigencias docentes y pedagógicas de ambas cátedras:
* **GITT (Teleco):** Formateo estricto con operador clásico `%` (`%02d`, `%7.2f`, `%s`) según la Chuleta Oficial de Rafael Palacios, algoritmia de señales/decibelios ($W \rightarrow \text{dBm}$) y detección de patrones/ADN con ventanas deslizantes.
* **IMAT (Matemática & IA):** Álgebra de Boole formal (puertas lógicas, Leyes de De Morgan, operadores bitwise), teoría de conjuntos con `set`, *comprehensions*, paso de parámetros de consola con `sys.argv` y *Type Hints* formales.
* **Reglas Universales ICAI:** Programación estructurada estricta (cero tolerancia a `break`, `continue`, `while True:`), modelo de memoria defensivo (sin aliasing accidental) y validación rigurosa de entradas.

---

## 🚀 Guía de Puesta a Punto en Visual Studio Code

### 1. Abrir la carpeta en VS Code
1. Abre **Visual Studio Code**.
2. Selecciona **File > Open Folder...** y elige la carpeta de este repositorio (`curso-python-icai-alumnos`).

### 2. Configurar el Entorno Virtual de Python
Abre una terminal integrada en VS Code (**Terminal > New Terminal** o ``Ctrl + ` ``) y ejecuta:

#### En Windows (PowerShell):
```powershell
# 1. Crear el entorno virtual
python -m venv venv

# 2. Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Si PowerShell bloquea scripts por ExecutionPolicy, ejecuta antes:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 3. Instalar las librerías necesarias
pip install -r requirements.txt
```

#### En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 💻 Metodología de Trabajo por Sesión

Cada sesión formativa se encuentra organizada en su respectivo bloque temático:

```
curso-python-icai-alumnos/
├── bloque_1_fundamentos_estructurados/
│   ├── s01_variables_operadores/
│   │   ├── enunciado.md      <-- 1. Lee aquí el objetivo y las especificaciones
│   │   ├── skeleton.py       <-- 2. Desarrolla aquí tu solución
│   │   └── test_s01.py       <-- 3. Valida tu código con pytest
│   └── ...
```

### Flujo de resolución:
1. **Leer el enunciado:** Abre `enunciado.md` para comprender los requisitos, casos de prueba esperados y posibles trampas típicas de examen.
2. **Implementar en el esqueleto:** Abre `skeleton.py`. Encontrarás la cabecera de las funciones con sus *Type Hints* y *docstrings*. Sustituye el bloque `# TODO` y `pass` por tu código estructurado.
3. **Autoevaluar con pytest:** Ejecuta desde la terminal el test individual de la sesión:
   ```bash
   pytest bloque_1_fundamentos_estructurados/s01_variables_operadores/test_s01.py -v
   ```
4. **Auditoría de Reglas ICAI:** Comprueba que no has utilizado ninguna instrucción prohibida:
   ```bash
   pytest tests/test_icai_rules.py -v
   ```
5. **Comprobar todo el curso:** En cualquier momento puedes comprobar el estado global de tu avance ejecutando:
   ```bash
   python run_all_tests.py
   ```

---

## ⚠️ Las 3 Leyes de Hierro de ICAI en Examen (Penalización Automática)

En los exámenes oficiales de programación de ICAI, el incumplimiento de estas normas conlleva **penalizaciones severas (hasta -2.5 puntos por problema)**:

1. **PROHIBIDO:** `break`, `continue`, `pass` (en la entrega final) y bucles infinitos `while True:`.
   * **Doctrina Dijkstra:** Todo bucle debe gobernarse mediante condiciones lógicas y variables de control booleanas (*flags* / centinelas como `encontrado = False`, `terminado = False`).
2. **Cuidado con el Aliasing de Memoria (Punteros en Heap):**
   * En Python, la asignación `b = a` copia la **referencia**, no el contenido. Si modificas `b`, modificarás `a` inadvertidamente.
   * Emplea siempre copias defensivas: `b = a[:]` o `b = a.copy()`. Nunca inicialices matrices con `[[0]*N]*M` (genera filas alias), usa `[[0 for _ in range(N)] for _ in range(M)]`.
3. **Formateo Estricto según la Chuleta Oficial:**
   * Utiliza la sintaxis de formateo con el operador `%` (`%02d`, `%7.2f`, `%s`) tal como se detalla en el documento de referencia `chuleta_oficial_icai.pdf` disponible en la raíz de este repositorio.

---

## 📅 Estructura de Sesiones y Cronograma del Curso (20 Sesiones)

| Bloque | Sesión | Concepto Central | Archivos Clave |
|---|:---:|---|---|
| **B1** | **01** | Heap, punteros, casting, type hints y chuleta Palacios (`%02d`, `%7.2f`) | `bloque_1/.../s01_variables_operadores/` |
| **B1** | **02** | Lógica booleana, De Morgan, operadores bitwise y raíces de 2º grado ($a=0$) | `bloque_1/.../s02_io_condicionales/` |
| **B1** | **03** | Bucles `while` estructurados (Sin break): Banderas y Algoritmo de Euclides | `bloque_1/.../s03_bucles_while_banderas/` |
| **B1** | **04** | Bucle `for`, `range()` y aproximación Taylor ($e^x, \sin x$) con doble centinela | `bloque_1/.../s04_bucles_for_series/` |
| **B2** | **05** | Strings, indexación e inmutabilidad (Supresión de vocales y tramas MAC) | `bloque_2/.../s05_strings_indexacion/` |
| **B2** | **06** | Slicing quirúrgico `[::]`, paso negativo, búsquedas seguras y palíndromos | `bloque_2/.../s06_slicing_avanzado/` |
| **B2** | **07** | Ventana deslizante ($L-W+1$) y ADN: Detección de motivos y contenido $\%GC$ | `bloque_2/.../s07_busqueda_ventanas_adn/` |
| **B2** | **08** | Métodos de cadenas: `.split()`, `.join()`, `.strip()`, `.replace()` y GPS NMEA | `bloque_2/.../s08_metodos_parsing_texto/` |
| **B3** | **09** | Listas: Mutabilidad, aliasing vs copia superficial/profunda y `id()` | `bloque_3/.../s09_listas_mutabilidad_aliasing/` |
| **B3** | **10** | Matrices 2D (listas de listas), la trampa `[[0]*N]*M`, simetría y transposición | `bloque_3/.../s10_matrices_2d_listas_anidadas/` |
| **B3** | **11** | Tuplas (unpacking), **Conjuntos (`set`)** y Diccionarios defensivos (`.get()`) | `bloque_3/.../s11_tuplas_diccionarios_base/` |
| **B3** | **12** | Diccionarios anidados, histogramas y **List/Dict Comprehensions** | `bloque_3/.../s12_diccionarios_anidados_frecuencias/` |
| **B4** | **13** | Funciones puras, Type Hints estrictos, Docstrings formales y regla LEGB | `bloque_4/.../s13_funciones_scope_modularidad/` |
| **B4** | **14** | Paso por referencia de objetos, mutación in-place vs diseño defensivo | `bloque_4/.../s14_funciones_mutabilidad_efectos/` |
| **B4** | **15** | Ficheros `.txt`: modos de apertura, lectura línea a línea eficiente y `\n` | `bloque_4/.../s15_ficheros_texto_txt/` |
| **B4** | **16** | CSV, JSON y serialización binaria `.dat` con `pickle` (Gestión de `EOFError`) | `bloque_4/.../s16_ficheros_csv_dat_json/` |
| **B5** | **17** | Visualización técnica con Matplotlib: curvas, leyendas y gráficos de ingeniería | `bloque_5/.../s17_visualizacion_matplotlib/` |
| **B5** | **18** | Proyecto Integrador: Menú estructurado con centinela y CLI con `sys.argv` | `bloque_5/.../s18_proyecto_integrador_menu/` |
| **B5** | **19** | **Simulacro Real de Examen Integrado Cronometrado (50 min)** | `bloque_5/.../s19_simulacro_examen_enunciado/` |
| **B5** | **20** | **Guías Estratégicas y Rúbrica Oficial de Calificación** | `bloque_5/.../s20_simulacro_solucion_rubrica/` |

---

## 📂 Recursos de Apoyo Incluidos

* **`chuleta_oficial_icai.pdf`:** Documento oficial de consulta permitido en exámenes presenciales de ICAI (operadores, formateo `%`, métodos de tipos básicos).
* **`data/`:** Datos de ejemplo (`coches.txt`, `country.csv`, `menu.json`, `menu2.json`) utilizados en las sesiones de ficheros y parsing.
* **`bloque_5_integracion_simulacro/s20_simulacro_solucion_rubrica/`:**
  * `diez_mandamientos_examen.md`: Decálogo con los 10 errores que suspenden a los alumnos en ICAI y cómo evitarlos.
  * `rubrica_oficial_icai.md`: Desglose oficial de puntuaciones y penalizaciones de la cátedra.
