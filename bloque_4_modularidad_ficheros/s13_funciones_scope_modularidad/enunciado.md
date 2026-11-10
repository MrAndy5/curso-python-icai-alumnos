# Sesión 13: Diseño de Funciones, Scope y Modularidad

## Objetivo Clave (Minuto 55)
Diseñar funciones desacopladas con parámetros formales y retornos tipados, evitando variables globales y devolviendo múltiples resultados mediante tuplas desempaquetadas.

## Concepto Trampa de Examen
1. Olvidar el `return`: la función ejecuta el cálculo pero devuelve `None` por defecto.
2. Usar la palabra clave `global` dentro de la función, penalizado severamente en ICAI por romper el principio de encapsulación modular.

## Esquema Temporal (60 min)
- **00-20m:** Declaración de funciones, paso de parámetros y ciclo de vida de variables locales.
- **20-40m:** Live-coding: **Validación matemática del DNI y NIE español con módulo 23 (Lab 8.1 ICAI).**
- **40-55m:** Reto interactivo: Refactorizar un script monolítico de cálculo de tarifas telefónicas en funciones independientes.
- **55-60m:** Verificación con pytest.
