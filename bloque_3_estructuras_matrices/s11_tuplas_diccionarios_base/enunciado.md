# Sesión 11: Tuplas y Diccionarios Básicos (Clave-Valor)

## Objetivo Clave (Minuto 55)
Manipular diccionarios para almacenamiento y consulta en $O(1)$, emplear tuplas como registros inmutables y verificar existencia de claves con `in` y `.get()`.

## Concepto Trampa de Examen
El error `KeyError: 'clave'`. Ocurre al leer directamente `d[clave]` cuando no existe. En examen se exige validar siempre con `if clave in d:` o usar `d.get(clave, valor_por_defecto)`.

## Esquema Temporal (60 min)
- **00-20m:** Diccionarios en memoria (tablas hash). Métodos `.keys()`, `.values()`, `.items()`.
- **20-40m:** Live-coding: Actualizador de inventario de equipos de telecomunicaciones (Lab 7).
- **40-55m:** Reto interactivo: Inversión de un diccionario (intercambio de claves y valores únicos).
- **55-60m:** Validación de pruebas.
