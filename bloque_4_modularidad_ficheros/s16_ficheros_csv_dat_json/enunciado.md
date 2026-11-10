# Sesión 16: Ficheros Estructurados: CSV, JSON y Persistencia Binaria (.dat)

## Objetivo Clave (Minuto 55)
Leer ficheros CSV tabulares, manipular jerarquías JSON (`json.loads/dumps`) y persistir objetos complejos en ficheros binarios `.dat` con `pickle` (requisito obligatorio del Proyecto 2024 de ICAI).

## Concepto Trampa de Examen
Tratar los números leídos de un CSV como datos numéricos sin aplicar `int()` o `float()`. En `.dat`, olvidar abrir el fichero en modo binario `'rb'` o `'wb'` (produce `TypeError: write() argument must be str, not bytes`).

## Esquema Temporal (60 min)
- **00-20m:** Diferencia entre texto plano, delimitadores CSV, formato JSON y serialización `.dat` con `pickle`.
- **20-40m:** Live-coding: **Datos de Pacientes y Cálculo de Riesgo de Infarto (Lab 9.2 ICAI):** Filtrado de pacientes de riesgo desde CSV y guardado en binario.
- **40-55m:** Reto interactivo: Cargar y modificar `menu.json` (Class 10 del profesor).
- **55-60m:** Validación cruzada de persistencia.
