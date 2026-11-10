# Sesión 10: Matrices y Listas Anidadas (Listas de Listas)

## Objetivo Clave (Minuto 55)
Crear, indexar bidimensionalmente `M[fila][col]` y recorrer matrices rectangulares y cuadradas con bucles anidados estructurados sin `break`.

## Concepto Trampa de Examen
1. Inicialización corrupta: `M = [[0]*3]*3`. Esto triplica la misma lista en memoria. Modificar `M[0][0]=1` cambia todas las filas.
2. Desbordamiento de límites: confundir filas (`len(M)`) con columnas (`len(M[0])`).

## Esquema Temporal (60 min)
- **00-20m:** Arquitectura de listas de listas en Python.
- **20-40m:** Live-coding: Comprobación de matriz simétrica ($M = M^T$) con bucle `while` estructurado (Tutoría 8-Oct ICAI).
- **40-55m:** Reto interactivo: Cálculo de la traza (suma diagonal principal) y transpuesta de una matriz rectangular.
- **55-60m:** Pruebas unitarias de matrices.
