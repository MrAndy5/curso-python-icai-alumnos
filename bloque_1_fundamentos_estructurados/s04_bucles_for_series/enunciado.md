# Sesión 04: Bucle For, Range y Series Matemáticas (Taylor)

## Objetivo Clave (Minuto 55)
Dominar la iteración con `range()` en sus 3 formas, calculando sumatorios y series de potencias con acumuladores de signo, potencia y factorial sin recurrir a librerías externas.

## Concepto Trampa de Examen
1. Calcular el factorial desde cero en cada término de la serie ($1 \cdot 2 \cdots k$), lo que degrada el rendimiento a $O(N^2)$.
2. Confundir la indexación del término $n$ con la potencia $2n+1$.
3. No controlar la paridad del signo alternante $(-1)^n$.

## Esquema Temporal (60 min)
- **00-20m:** Funcionamiento de `range(inicio, fin, paso)` y mecánica de acumuladores en bucle `for`.
- **20-40m:** Live-coding: **Aproximación de seno de Taylor (Lab 4 de ICAI):**
  $$sen(x) = \sum_{n=0}^{N-1} rac{(-1)^n \cdot x^{2n+1}}{(2n+1)!}$$
- **40-55m:** Reto guiado: Serie de Maclaurin de $\cos(x)$ o exponencial $e^x$.
- **55-60m:** Validación numérica frente al módulo `math`.
