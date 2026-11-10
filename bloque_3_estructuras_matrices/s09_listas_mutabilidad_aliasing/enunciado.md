# Sesión 09: Listas, Mutabilidad, Aliasing y Métodos In-Place

## Objetivo Clave (Minuto 55)
Dominar la mutabilidad de listas, entender el paso de referencias en memoria para evitar bugs de aliasing (`b = a` vs `b = a[:]`), y dominar métodos in-place (`.append()`, `.extend()`, `.sort()`, `.remove()`).

## Concepto Trampa de Examen
El fallo recurrente:
```python
def procesar(lista):
    lista_ordenada = lista.sort() # ¡Retorna None! lista.sort() muta in-place
```
Además, modificar una lista mientras se itera con `for x in lista: lista.remove(x)`, lo que salta elementos.

## Esquema Temporal (60 min)
- **00-20m:** Diagrama de punteros en Heap. Copias superficiales vs aliasing.
- **20-40m:** Live-coding: Depuración y clasificación de calificaciones (Lab 6.2).
- **40-55m:** Reto interactivo: Eliminación segura de duplicados manteniendo el orden original.
- **55-60m:** Verificación de asertos.
