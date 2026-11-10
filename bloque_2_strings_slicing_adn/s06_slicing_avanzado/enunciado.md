# Sesión 06: Slicing Quirúrgico de Cadenas y Tramas Binarias

## Objetivo Clave (Minuto 55)
Dominar la sintaxis `cadena[inicio:fin:paso]` con pasos positivos y negativos (`[::-1]`), extracción simétrica y parsing de cabeceras de paquetes de telecomunicación.

## Concepto Trampa de Examen
El límite superior del slice es no inclusivo (`s[1:4]` toma índices 1, 2, 3; excluye el 4). La confusión habitual al omitir límites con pasos negativos (`s[::-1]`).

## Esquema Temporal (60 min)
- **00-20m:** Álgebra de índices del slicing. Casos borde (índices fuera de rango en slicing no lanzan IndexError, se truncan).
- **20-40m:** Live-coding: Decodificador de tramas de red fijas `[CABECERA:4][ORIGEN:4][DESTINO:4][PAYLOAD][CRC:2]`.
- **40-55m:** Reto interactivo: Verificador de palíndromos puro en una línea de slice.
- **55-60m:** Validación de tests.
