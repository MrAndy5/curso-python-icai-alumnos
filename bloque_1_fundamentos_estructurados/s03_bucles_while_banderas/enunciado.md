# Sesión 03: Bucles While con Banderas de Control (Estilo Oficial ICAI)

## Objetivo Clave (Minuto 55)
Dominar bucles interactivos e indeterminados gobernados por variables de estado booleanas (`seguir = True`, `enc = False`), calculando acumulaciones, promedios móviles y validaciones sin usar jamás `break`.

## Concepto Trampa de Examen
**LA PENALIZACIÓN MÁXIMA EN ICAI:**
En el examen oficial de ICAI figura en cabecera:
> *'No se permite el uso los comandos break, continue, pass, ni while (True)... Su utilización será penalizada.'*
Cualquier parada de bucle debe estar en la condición lógica de la cabecera del `while`.

## Esquema Temporal (60 min)
- **00-20m:** Deconstrucción del bucle estructurado. Cómo sustituir `while True: break` por `while not terminado:`.
- **20-40m:** Live-coding: **Examen GITT 3/10/2024 - Números Singulares.** Promedio acumulado de números precedentes.
- **40-55m:** Reto interactivo: **Examen GITT 3/10/2024 - Tiro parabólico al hoyo de golf** con contador de intentos.
- **55-60m:** Auditoría de código para certificar 0 ocurrencias de break/continue.
