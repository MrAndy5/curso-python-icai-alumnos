# Sesión 15: Ficheros de Texto Plano (.txt): Lectura y Escritura Segura

## Objetivo Clave (Minuto 55)
Abrir, leer, escribir y procesar ficheros de texto con `with open(...)`, recorriendo línea por línea, sanitizando con `.strip()` y agregando datos estadísticos.

## Concepto Trampa de Examen
El salto de línea `\n` al final de cada línea leída. Si no se aplica `.strip()`, comparaciones como `if linea == "Lunes"` fallarán porque `linea` es `"Lunes\n"`.
Olvidar el cierre con `.close()` si no se usa el gestor de contexto `with`.

## Esquema Temporal (60 min)
- **00-20m:** Modos de apertura `'r'`, `'w'`, `'a'`. Lectura en bloque vs iterador por línea.
- **20-40m:** Live-coding: **Procesador del fichero de temperaturas diarias (Lab 9.1 ICAI).**
- **40-55m:** Reto interactivo: Exportar un informe resumen con formateo limpio a `resumen.txt`.
- **55-60m:** Verificación de lectura de ficheros.
