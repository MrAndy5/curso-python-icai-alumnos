# Sesión 07: Algoritmos de Ventana Deslizante y Secuencias de ADN (Examen Intermedio)

## Objetivo Clave (Minuto 55)
Implementar algoritmos de ventana deslizante y seguimiento de secuencias contiguas óptimas sobre listas o cadenas, almacenando máximos históricos de longitud y posición de inicio.

## Concepto Trampa de Examen (Inspirado en examenA.ipynb)
1. Confundir la comprobación `if i != 'T':` olvidando las comillas en `'T'`.
2. Actualizar el récord de longitud solo al encontrar el delimitador, perdiendo la secuencia si el array termina en nucleótidos válidos sin una 'T' final.
3. Desajuste de índices entre el puntero local y el récord global.

## Esquema Temporal (60 min)
- **00-20m:** Análisis del error real en el examen intermedio de octubre 2023 de ICAI (`examenA.ipynb`).
- **20-40m:** Live-coding: Algoritmo canónico de búsqueda de subsecuencia más larga sin 'T'.
- **40-55m:** Reto interactivo: Detección de la secuencia más larga de nucleótidos consecutivos iguales.
- **55-60m:** Verificación con la secuencia de examen completa de 60 bases.
