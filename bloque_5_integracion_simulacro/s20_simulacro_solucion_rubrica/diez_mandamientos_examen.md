# Los 10 Mandamientos del Alumno de ICAI para el Día del Examen

1. **No usarás `break`, ni `continue`, ni `pass`, ni `while True:`:** Gobernarás tus bucles con una bandera lógica clara (`stay = False`, `terminar = True`).
2. **No confundirás la copia con la referencia:** Si quieres clonar una lista, escribirás `b = a[:]` o `b = a.copy()`.
3. **Validarás siempre las entradas:** Ante la petición de enteros positivos, pondrás un `while n < 0:` de reintento.
4. **Desconfiarás de la división:** Siempre verificarás que el denominador no sea `0` antes de calcular promedios.
5. **No mutarás una lista mientras la recorres:** Si necesitas eliminar elementos, iterarás sobre una copia `for x in lista[:]:`.
6. **Recordarás que el slicing excluye el extremo:** `cadena[0:5]` solo tiene 5 caracteres (índices del 0 al 4).
7. **No esperarás que `.sort()` devuelva la lista:** Recordarás que ordena in-place y retorna `None`.
8. **Sanitizarás toda línea de fichero:** Aplicarás `.strip()` para exterminar el salto de línea `\n` invisible.
9. **No usarás `global`:** Las funciones recibirán parámetros formales y retornarán resultados con `return`.
10. **Comprobarás la existencia de claves:** Antes de acceder a `diccionario[clave]`, verificarás con `if clave in diccionario:`.
