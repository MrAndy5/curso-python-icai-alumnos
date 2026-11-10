# Sesión 05: Strings, Inmutabilidad y Recorridos Carácter a Carácter

## Objetivo Clave (Minuto 55)
Acceder a posiciones específicas de cadenas mediante indexación positiva y negativa, comprender la inmutabilidad y generar nuevas cadenas acumulativas sin errores de tipo.

## Concepto Trampa de Examen
Intentar mutar un carácter directamente: `cadena[0] = 'X'`. Python lanza `TypeError`. Para transformar un texto se debe construir un nuevo string mediante concatenación `+`.

## Esquema Temporal (60 min)
- **00-20m:** Representación de caracteres, indexación bidireccional y función `len()`.
- **20-40m:** Live-coding: Supresión selectiva de vocales y filtrado de caracteres no numéricos (Lab 5.1).
- **40-55m:** Reto interactivo: Codificador de rotación alfanumérica simple usando `ord()` y `chr()`.
- **55-60m:** Comprobación de asertos del skeleton.
