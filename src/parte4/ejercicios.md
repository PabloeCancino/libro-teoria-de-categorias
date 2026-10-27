# Ejercicios de la Parte IV

> **Soluciones completas.** Las soluciones de todos los ejercicios de niveles 1 y 2 de esta parte están en el [Apéndice E, Parte IV](../apendices/e-soluciones/parte4.md). Las de abajo son solo una selección.

---

## 📝 Nivel 1. Verificación

1. Describa la unidad y la counidad de la adjunción \\(k^{(-)} \dashv U\\) entre \\(\mathbf{Set}\\) y \\(\mathbf{Vect}\_k\\), y verifique las dos identidades triangulares en este caso.

2. Verifique que \\(D \dashv U \dashv I\\) (Ejemplo 8.6). ¿Tiene \\(D\\) un adjunto izquierdo? ¿Tiene \\(I\\) un adjunto derecho? *(Sugerencia: pruebe si preservan los límites o colímites necesarios.)*

3. Sea \\(f\colon X \to Y\\). Verifique directamente que \\(f^{-1}(T) \subseteq S\\) si y solo si \\(T \subseteq \forall\_f(S)\\).

4. Verifique la tabla del Ejemplo 9.3 en el renglón de la currificación: calcule \\((A \sqcup A') \times B\\) y compárelo con \\((A \times B) \sqcup (A' \times B)\\).

5. Demuestre que el funtor diagonal \\(\Delta\colon \mathcal{C} \to \mathcal{C} \times \mathcal{C}\\), \\(X \mapsto (X, X)\\), tiene adjunto derecho si y solo si \\(\mathcal{C}\\) tiene productos binarios, y adjunto izquierdo si y solo si tiene coproductos binarios.

---

## 📝 Nivel 2. Construcción

6. Generalice el Ejercicio 5: el funtor diagonal \\(\Delta\colon \mathcal{C} \to [\mathcal{J}, \mathcal{C}]\\) tiene adjunto derecho si y solo si \\(\mathcal{C}\\) tiene todos los límites de forma \\(\mathcal{J}\\). Concluya que \\(\lim\colon [\mathcal{J}, \mathcal{C}] \to \mathcal{C}\\) es un adjunto derecho y que, por lo tanto, **los límites conmutan con los límites**.

7. Demuestre que el olvidadizo \\(U\colon \mathbf{Ring} \to \mathbf{Mon}\\), que conserva solo la multiplicación, tiene adjunto izquierdo: el **anillo de monoide** \\(\mathbb{Z}[M]\\). Describa la unidad.

8. Sea \\(G\\) un grupo y sea \\(\mathbf{Set}\\) vista como la categoría de \\(G\\)-conjuntos con acción trivial dentro de \\([\mathbf{B}G, \mathbf{Set}]\\). Encuentre los adjuntos izquierdo y derecho de esa inclusión. *(Respuesta esperada: el conjunto de órbitas y el conjunto de puntos fijos.)*

9. Demuestre que en una categoría cartesiana cerrada, \\(A \times (B + C) \cong (A \times B) + (A \times C)\\) cuando existen los coproductos. ¿Por qué falla esta ley en \\(\mathbf{Vect}\_k\\) con \\(\times = \oplus\\)?

10. Use el Teorema 9.2 para demostrar que el olvidadizo \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) **no** tiene adjunto derecho.

---

## 📝 Nivel 3. Exploración

11. **Lógica y adjunciones.** En el libro *Lógica y Conjuntos* (Cancino Marentes y Yarza Acuña, 2026; ver el Apéndice D) se estudian las reglas de inferencia de los cuantificadores. Escriba las cuatro reglas de introducción y eliminación de \\(\exists\\) y \\(\forall\\) y muestre que cada par corresponde a uno de los lados de las adjunciones \\(\exists\_\pi \dashv \pi^{-1} \dashv \forall\_\pi\\).

12. **Conexiones de Galois en análisis de datos.** En el análisis formal de conceptos se tiene una relación \\(R \subseteq O \times A\\) entre objetos y atributos. Defina \\(\uparrow\colon \mathcal{P}(O) \to \mathcal{P}(A)\\), que envía un conjunto de objetos a los atributos que todos comparten, y \\(\downarrow\colon \mathcal{P}(A) \to \mathcal{P}(O)\\), en sentido inverso. Demuestre que forman una conexión de Galois **antítona** (una adjunción entre \\(\mathcal{P}(O)\\) y \\(\mathcal{P}(A)^{\mathrm{op}}\\)). ¿Qué son los "conceptos formales" en este lenguaje? Discuta si esta herramienta tiene uso en el análisis de patrones de respuesta a un instrumento.

13. **Grupos de nudos y abelianización.** Use el Ejemplo 9.9 para demostrar que la abelianización del grupo de cualquier nudo es \\(\mathbb{Z}\\), a partir de la presentación de Wirtinger: todos los generadores de Wirtinger son conjugados entre sí. ¿Qué consecuencia tiene esto sobre la capacidad de la abelianización para distinguir nudos?

---

## 💡 Soluciones seleccionadas

> **Solución al Ejercicio 5.**
> Una flecha \\(\Delta X \to (A, B)\\) en \\(\mathcal{C} \times \mathcal{C}\\) es un par \\((f\colon X \to A, \ g\colon X \to B)\\). Un adjunto derecho \\(P\\) de \\(\Delta\\) requiere \\(\mathcal{C}(X, P(A,B)) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B)\\) natural en \\(X\\), que es exactamente decir que \\(P(A,B)\\) es un producto de \\(A\\) y \\(B\\) (Capítulo 4). La counidad es el par de proyecciones. El caso del coproducto es dual. \\(\blacksquare\\)

> **Solución al Ejercicio 10.**
> Si \\(U\\) tuviera adjunto derecho, sería adjunto izquierdo y preservaría colímites; en particular, el objeto inicial. Pero el inicial de \\(\mathbf{Grp}\\) es el grupo trivial, con un elemento, y el de \\(\mathbf{Set}\\) es \\(\emptyset\\). \\(\blacksquare\\)

> **Guía para el Ejercicio 13.**
> La presentación de Wirtinger tiene un generador por arco y relaciones de la forma \\(x\_k = x\_i x\_j x\_i^{-1}\\). Al abelianizar, cada relación se vuelve \\(x\_k = x\_j\\), y como el diagrama del nudo es conexo, todos los generadores se identifican. Queda el grupo abeliano libre en un generador: \\(\mathbb{Z}\\). Consecuencia: **la abelianización no distingue ningún par de nudos**. Para obtener invariantes útiles hay que retener información no abeliana, como en el polinomio de Alexander, que proviene del grupo conmutador.
