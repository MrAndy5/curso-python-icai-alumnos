# Sesión 01: Variables, Tipos Primitivos, Casting y Formateo Numérico

## Objetivo Clave (Minuto 55)
Al finalizar la sesión, el alumno sabrá recibir entradas con `input()`, aplicar conversiones de tipo forzadas (`int()`, `float()`), evaluar expresiones matemáticas con precedencia estricta y formatear tablas con operadores clásicos `%` y f-strings.

## Concepto Trampa de Examen
1. `input()` **siempre** devuelve `str`. Intentar operar directamente produce `TypeError`.
2. Diferencia entre división real `/` (produce siempre `float`) y división entera `//`.
3. Errores de redondeo al imprimir: usar `%7.2f` para alinear columnas como exige la chuleta de ICAI.

## Esquema Temporal (60 min)
- **00-20m:** Explicación teórica: tipos de datos en Python, casting y formateo `%02d` / `%7.2f`.
- **20-40m:** Live-coding: Calculadora de potencia de telecomunicaciones (vatios a dBm y atenuación).
- **40-55m:** Reto interactivo en parejas: Formateo de tabla de conversión de unidades de telecomunicaciones.
- **55-60m:** Checklist de asimilación y ejecución de tests.

## Checklist de Asimilación
1. ¿Qué tipo devuelve la expresión `4 / 2`? -> `float` (2.0).
2. ¿Qué imprime `print("%03d" % 5)`? -> `'005'`.
3. ¿Cómo convertimos la cadena `"12.75"` a número de forma segura? -> `float("12.75")`.
