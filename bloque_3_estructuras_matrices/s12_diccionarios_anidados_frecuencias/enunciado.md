# Sesión 12: Diccionarios Anidados y Conteo de Frecuencias

## Objetivo Clave (Minuto 55)
Gestionar estructuras jerárquicas complejas (`dict` de `dict` y `dict` de `list`), iterar con desempaquetado de tuplas `for k, v in d.items():` y calcular balances acumulados (Proyecto 2024 de ICAI).

## Concepto Trampa de Examen
El fallo al insertar en subestructuras: intentar `d[clave].append(x)` sin inicializar primero `d[clave] = []`. Produce `KeyError`.

## Esquema Temporal (60 min)
- **00-20m:** Estructuras complejas en Python. Anatomía del modelo de datos de "ComillasFinance S.A.".
- **20-40m:** Live-coding: Consolidación de balances de clientes bancarios con operaciones positivas y negativas (Proyecto 2024).
- **40-55m:** Reto interactivo: Empresa de Camiones (Lab 7): cálculo del camión que transportó mayor tonelaje total.
- **55-60m:** Validación con asertos.
