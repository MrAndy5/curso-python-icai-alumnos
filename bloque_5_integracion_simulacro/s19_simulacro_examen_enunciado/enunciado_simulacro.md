# Examen Simulacro Final de Fundamentos de Programación (ICAI)
**Grado en Ingeniería de Tecnologías de Telecomunicación (1º GITT)**
**Tiempo asignado:** 50 Minutos | **Calificación Total:** 10 Puntos

---

### INSTRUCCIONES OBLIGATORIAS:
1. **REGLA ESTRUCTURADA ESTRICTA:** No se permite el uso de los comandos `break`, `continue`, `pass`, ni `while True:`. Su utilización supondrá una **penalización automática de 2.5 puntos** en cada ejercicio donde aparezcan.
2. Todo el código debe estar debidamente documentado y modularizado.

---

### Problema 1 (5 Puntos): Ráfagas de Errores en Paquetes Digitales
En un receptor de satélite se recibe una secuencia de paquetes numéricos.
- Un valor positivo ($>0$) indica el tamaño en bytes de un paquete recibido correctamente.
- Un valor negativo ($<0$) indica un fallo de transmisión en ese slot temporal.
- El valor `0` indica el fin del flujo de datos (paquete centinela).

Implementa la función:
```python
def analizar_rafagas_transmision(flujo: list[int]) -> tuple[int, int, float]:
```
que mediante un **único bucle estructurado sin `break`** devuelva:
1. El número total de paquetes correctos recibidos.
2. La longitud de la ráfaga más larga de errores consecutivos (negativos consecutivos).
3. El tamaño promedio de los paquetes correctos recibidos (redondeado a 2 decimales). Si no hubo paquetes correctos, debe retornar `0.0`.

---

### Problema 2 (5 Puntos): Auditoría de Conexiones de Red CSV
Un archivo de registro CSV contiene trazas de tráfico entre servidores:
`ID,IP_ORIGEN,IP_DESTINO,BYTES,LATENCIA`

Implementa la función:
```python
def auditar_trafico_red(lineas_csv: list[str], umbral_latencia: float) -> dict[str, dict]:
```
1. Debe ignorar la cabecera.
2. Debe filtrar las conexiones con latencia mayor o igual a `umbral_latencia`.
3. Debe agrupar por `IP_ORIGEN` y generar un diccionario con la estructura:
```python
{
    "192.168.1.1": {
        "num_conexiones_lentas": 2,
        "total_bytes": 1700,
        "latencia_maxima": 98.5
    }
}
```
4. Si alguna línea tiene datos numéricos corruptos, debe ignorarla sin romper la ejecución.
