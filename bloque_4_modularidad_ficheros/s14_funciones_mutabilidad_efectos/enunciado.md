# Sesión 14: Argumentos Mutables y Efectos Laterales en Funciones

## Objetivo Clave (Minuto 55)
Distinguir cuándo una función debe modificar in-place una estructura recibida (efecto lateral deseado) y cuándo debe protegerla, evitando los peligrosos argumentos por defecto mutables `def f(x, l=[])`.

## Concepto Trampa de Examen
El comportamiento de los argumentos por defecto mutables en Python:
```python
def agregar(x, lista=[]): # ¡La lista se comparte entre llamadas!
    lista.append(x)
    return lista
```
Solución obligatoria: `def agregar(x, lista=None): if lista is None: lista = []`.

## Esquema Temporal (60 min)
- **00-20m:** Paso de parámetros por asignación de objetos (Call by Object Reference).
- **20-40m:** Live-coding: **Juego de las Siete y Media (Lab 8.2 ICAI):** gestión de la baraja con extracción destructiva controlada (`del baraja[0]`).
- **40-55m:** Reto interactivo: Depuración de funciones con efectos laterales no deseados.
- **55-60m:** Validación con tests.
