# Ejercicios de la Parte V

> **Soluciones completas.** Las soluciones de todos los ejercicios de niveles 1 y 2 de esta parte están en el [Apéndice E, Parte V](../apendices/e-soluciones/parte5.md). Las de abajo son solo una selección.

---

## 📝 Nivel 1. Verificación

1. Verifique las leyes de mónada para la mónada de elementos opcionales \\(X \mapsto X + \\{\bot\\}\\).

2. Verifique la ley de asociatividad de la mónada \\(\mathcal{P}\\): para \\(\mathfrak{S} \in \mathcal{P}\mathcal{P}\mathcal{P}(X)\\), unir primero los conjuntos de nivel interior y luego el resultado da lo mismo que unir primero los de nivel exterior.

3. Demuestre que la composición de Kleisli es asociativa y que \\(\eta\\) es neutra para ella. Indique en qué paso usa cada ley de la mónada.

4. Calcule la composición de Kleisli de dos núcleos de Markov entre conjuntos de dos elementos, dados por las matrices estocásticas
   \\(\begin{pmatrix} 0.9 & 0.2 \\\\ 0.1 & 0.8 \end{pmatrix}\\) y \\(\begin{pmatrix} 0.7 & 0.5 \\\\ 0.3 & 0.5 \end{pmatrix}\\).

5. Sea \\(c\\) la cerradura topológica en \\(\mathcal{P}(X)\\) para un espacio \\(X\\). Verifique que es una mónada sobre el orden \\((\mathcal{P}(X), \subseteq)\\) y describa sus álgebras.

---

## 📝 Nivel 2. Construcción

6. Complete la demostración del Teorema 10.13: verifique que las asignaciones \\(g \mapsto g \circ \eta\_X\\) y \\(f \mapsto a \circ T(f)\\) son mutuamente inversas y que \\(a \circ T(f)\\) es un morfismo de álgebras.

7. Demuestre que las \\(\mathcal{P}\\)-álgebras son los retículos completos y que los morfismos de álgebras son las funciones que preservan supremos arbitrarios.

8. Sea \\(M\\) un monoide. Demuestre que \\(T(X) = M \times X\\), con \\(\eta\_X(x) = (e, x)\\) y \\(\mu\_X(m, (n, x)) = (mn, x)\\), es una mónada en \\(\mathbf{Set}\\), y que sus álgebras son los conjuntos con una acción de \\(M\\) (los \\(M\\)-conjuntos).

9. Encuentre una adjunción que produzca la mónada de elementos opcionales y describa su categoría de Kleisli y su categoría de Eilenberg–Moore. Demuestre que, en este caso, son equivalentes. Después muestre que para la mónada de listas no lo son. *(Sugerencia: en la categoría de Kleisli de las listas, todo objeto es un álgebra libre; ¿lo es todo monoide?)*

10. **La mónada de excepciones.** Para un conjunto fijo \\(E\\), considere \\(T(X) = X + E\\) (cálculos que pueden terminar con un error de tipo \\(E\\)). Demuestre que es una mónada y describa sus álgebras.

---

## 📝 Nivel 3. Exploración

11. **Clases latentes como composición de Kleisli.** Tome \\(\Theta = \\{\text{dominio}, \text{no dominio}\\}\\) y tres reactivos dicotómicos. Escriba el modelo de clases latentes con independencia local como una previa \\(\\{\star\\} \rightsquigarrow \Theta\\) compuesta con un núcleo \\(\Theta \rightsquigarrow \\{0,1\\}^3\\). Calcule, con números concretos, la distribución marginal de los ocho patrones mediante la composición de Kleisli. Después invierta el núcleo con la regla de Bayes. ¿Qué parte del cálculo es "categórica" y qué parte es aritmética ordinaria?

12. **La mónada de seudo-distribuciones.** Si en \\(\mathcal{D}\\) se permiten pesos negativos que suman 1, ¿se obtiene una mónada? ¿Cuáles son sus álgebras? Compare con los espacios afines.

13. **Lectura dirigida.** Lea la introducción del artículo de Fritz (2020) sobre categorías de Markov. Escriba una página que responda: ¿qué resultado de estadística clásica reformula el artículo, y qué hipótesis de teoría de la medida elimina?

---

## 💡 Soluciones seleccionadas

> **Solución al Ejercicio 4.**
> Si \\(f\\) es la primera matriz y \\(g\\) la segunda, \\(g \circ\_{\mathcal{D}} f\\) corresponde al producto \\(G F\\):
>
> \\[
> \begin{pmatrix} 0.7 & 0.5 \\\\ 0.3 & 0.5 \end{pmatrix} \begin{pmatrix} 0.9 & 0.2 \\\\ 0.1 & 0.8 \end{pmatrix} = \begin{pmatrix} 0.68 & 0.54 \\\\ 0.32 & 0.46 \end{pmatrix}.
> \\]
>
> Cada columna suma 1: la composición de núcleos de Markov es otro núcleo de Markov.

> **Solución al Ejercicio 8.**
> Las leyes de mónada se reducen a las del monoide: \\(\mu \circ T\mu\\) y \\(\mu \circ \mu T\\) envían \\((m, (n, (p, x)))\\) a \\((m(np), x)\\) y a \\(((mn)p, x)\\), iguales por asociatividad; las leyes de unidad son \\(ex = x = xe\\) en la primera coordenada. Un álgebra \\(a\colon M \times A \to A\\) cumple \\(a(e, x) = x\\) y \\(a(m, a(n, x)) = a(mn, x)\\): es una acción de \\(M\\) sobre \\(A\\). \\(\blacksquare\\)

> **Guía para el Ejercicio 9.**
> La adjunción es la de los conjuntos con un punto distinguido: el adjunto izquierdo agrega un punto nuevo, \\(X \mapsto X + \\{\bot\\}\\), y el derecho olvida cuál era el punto. La categoría de Eilenberg–Moore es la de conjuntos punteados; la de Kleisli, la de funciones parciales. Son equivalentes: una función parcial \\(X \to Y\\) es lo mismo que una función punteada \\(X + \\{\bot\\} \to Y + \\{\bot\\}\\), y todo conjunto punteado es isomorfo a uno de la forma \\(X + \\{\bot\\}\\). Es decir, aquí **toda álgebra es libre**. Para la mónada de listas no ocurre así: el monoide \\(\mathbb{Z}/2\\) no es libre (un monoide libre no trivial no tiene elementos de orden finito distintos del neutro), así que la comparación de Kleisli en Eilenberg–Moore no es esencialmente sobreyectiva y, por lo tanto, **no es una equivalencia**. (Que no exista ninguna otra equivalencia entre ambas categorías requiere un argumento adicional, por ejemplo, comparar qué objetos son proyectivos.)
