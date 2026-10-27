# Ejercicios de la Parte VI

---

## 📝 Nivel 1. Verificación

1. Verifique que \\((\mathbf{Set}, \sqcup, \emptyset)\\) es una categoría monoidal. ¿Es simétrica?

2. Demuestre que en \\((\mathbf{Set}, \times, \\{\star\\})\\) todo conjunto \\(X\\) es un **comonoide** de manera única, con la diagonal \\(X \to X \times X\\) y la función \\(X \to \\{\star\\}\\). Interprete: en una categoría cartesiana, la información se puede **copiar** y **borrar**.

3. Verifique la ecuación de Yang–Baxter para el intercambio \\(s(u \otimes v) = v \otimes u\\) en \\(\mathbf{Vect}\_k\\), evaluando ambos lados en \\(u \otimes v \otimes w\\).

4. Dibuje, como diagramas de cuerdas, ambos lados de la relación de Artin \\(\sigma\_1 \sigma\_2 \sigma\_1 = \sigma\_2 \sigma\_1 \sigma\_2\\) en \\(B\_3\\) y convénzase de que son isotópicos.

5. Calcule la dimensión (traza de la identidad) de \\(k^n\\) en \\(\mathbf{Vect}\_k\\) usando la fórmula del Ejemplo 12.11.

---

## 📝 Nivel 2. Construcción

6. Demuestre que un monoide en \\((\mathbf{Ab}, \otimes, \mathbb{Z})\\) es lo mismo que un anillo. Precise qué propiedad del producto tensorial se usa para traducir la bilinealidad.

7. Demuestre que en una categoría monoidal **simétrica** la traza es cíclica: \\(\mathrm{tr}(g \circ f) = \mathrm{tr}(f \circ g)\\) para \\(f\colon A \to B\\), \\(g\colon B \to A\\) con \\(A\\), \\(B\\) dualizables. Hágalo con diagramas de cuerdas.

8. Sea \\(V = k^2\\) con base \\(e\_1, e\_2\\) y sea \\(R\colon V \otimes V \to V \otimes V\\) definida por \\(R(e\_i \otimes e\_j) = q\\, e\_j \otimes e\_i\\) si \\(i = j\\) y \\(R(e\_i \otimes e\_j) = e\_j \otimes e\_i\\) si \\(i \neq j\\), con \\(q \neq 0\\). ¿Satisface \\(R\\) la ecuación de Yang–Baxter? ¿Qué representación de \\(B\_3\\) produce? ¿Es genuinamente trenzada (es decir, \\(R^2 \neq 1\\))?

9. Calcule el corchete de Kauffman del diagrama estándar del enlace de Hopf (dos cruces) y luego \\(X(L)\\) con la corrección por la torsión. Compare con el corchete de dos círculos separados.

10. Calcule el corchete de Kauffman de un diagrama del nudo trébol con tres cruces. Verifique que \\(X\\) distingue el trébol de su imagen especular.

---

## 📝 Nivel 3. Exploración

11. **Categorías de Markov.** Demuestre que en la categoría de núcleos de Markov finitos con el tensor del Ejemplo 12.3, cada conjunto tiene una "copia" \\(X \rightsquigarrow X \times X\\) dada por la diagonal, pero que la copia **no es natural**: copiar una variable aleatoria y luego aplicar un núcleo a cada copia no es lo mismo que aplicar el núcleo y luego copiar. Interprete esta falla en términos de muestras independientes frente a una misma observación usada dos veces.

12. **Funtorialidad de un invariante propio.** Tome un invariante combinatorio de nudos con el que trabaje (o el número de enlace, como caso de prueba). Responda: (a) ¿puede definirse también para enredos con extremos? (b) si \\(T\_1\\) y \\(T\_2\\) son enredos componibles, ¿se calcula el invariante de \\(T\_2 \circ T\_1\\) a partir de datos de \\(T\_1\\) y \\(T\_2\\)? (c) ¿qué estructura algebraica deben tener esos datos para que la composición funcione? Si las tres respuestas son afirmativas, el invariante es **candidato** a ser funtorial. Para aplicar el Teorema 13.8 hace falta además que respete el producto tensorial, los cruces, los duales y el giro, es decir, que provenga de un funtor de listón.

13. **Seudo-álgebras.** Escriba con detalle qué datos y qué ecuaciones tiene una seudo-álgebra de la 2-mónada de listas del Ejemplo E.2, y compruebe que el pentágono aparece como una de sus condiciones de coherencia.

---

## 💡 Soluciones seleccionadas

> **Solución al Ejercicio 3.**
> El lado izquierdo de la ecuación de Yang–Baxter, \\((s \otimes 1)(1 \otimes s)(s \otimes 1)\\), envía \\(u \otimes v \otimes w\\) a \\(v \otimes u \otimes w\\), luego a \\(v \otimes w \otimes u\\) y luego a \\(w \otimes v \otimes u\\). El lado derecho, \\((1 \otimes s)(s \otimes 1)(1 \otimes s)\\), lo envía a \\(u \otimes w \otimes v\\), luego a \\(w \otimes u \otimes v\\) y luego a \\(w \otimes v \otimes u\\). Ambos invierten el orden. \\(\blacksquare\\)

> **Solución al Ejercicio 5.**
> \\(\mathrm{coev}(1) = \sum\_{i=1}^n e\_i \otimes e^i\\). La simetría lo envía a \\(\sum\_i e^i \otimes e\_i\\), y la evaluación da \\(\sum\_i e^i(e\_i) = n\\). La dimensión categórica coincide con la dimensión usual. \\(\blacksquare\\)

> **Guía para el Ejercicio 9.**
> Al resolver los dos cruces con la regla del corchete se obtienen cuatro estados. Dos de ellos dan un solo círculo y dos dan dos círculos, con pesos \\(A^2\\), \\(A^{-2}\\) y \\(1\\) según el tipo de suavizado. El resultado es \\(\langle \text{Hopf} \rangle = -A^4 - A^{-4}\\). Para dos círculos separados, el corchete es \\(\delta = -A^2 - A^{-2}\\) y la torsión es \\(0\\). Para el enlace de Hopf, según la orientación, \\(w = 2\\) o \\(w = -2\\), y la corrección da \\(X = -A^{-2} - A^{-10}\\) o \\(X = -A^{2} - A^{10}\\). Ninguno coincide con \\(\delta\\): el enlace de Hopf no es el enlace trivial de dos componentes.
