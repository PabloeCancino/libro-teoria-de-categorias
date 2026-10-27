# Ejercicios de la Parte II

> **Soluciones completas.** Las soluciones de todos los ejercicios de niveles 1 y 2 de esta parte están en el [Apéndice E, Parte II](../apendices/e-soluciones/parte2.md). Las de abajo son solo una selección.

---

## 📝 Nivel 1. Verificación

1. Determine los objetos iniciales y terminales, si existen, de: \\(\mathbf{Pos}\\); \\(\mathbf{Mon}\\); la categoría de campos y homomorfismos de campos; el orden \\((\mathbb{N}, \mid)\\).

2. Demuestre que si \\((P, \pi\_1, \pi\_2)\\) y \\((P', \pi\_1', \pi\_2')\\) son productos de \\(A\\) y \\(B\\), existe un único isomorfismo \\(h\colon P' \to P\\) con \\(\pi\_1 \circ h = \pi\_1'\\) y \\(\pi\_2 \circ h = \pi\_2'\\). Imite la Proposición 4.2.

3. Calcule el producto y el coproducto de dos objetos en la categoría \\(\mathbf{B}M\\) asociada al monoide \\((\mathbb{N}, +, 0)\\), o demuestre que no existen.

4. Verifique que el funtor \\(G \mapsto \\{(g,h) \in G \times G \mid gh = hg\\}\\), de \\(\mathbf{Grp}\\) en \\(\mathbf{Set}\\), es representable y encuentre el objeto que lo representa.

5. En \\((\mathbb{N}, \mid)\\), ¿cuál es el producto de una familia infinita de números? ¿Y el coproducto?

---

## 📝 Nivel 2. Construcción

6. Complete la demostración del lema de Yoneda: pruebe que la biyección \\(\mathrm{Nat}(\mathcal{C}(-,A), F) \cong F(A)\\) es natural en \\(A\\) (respecto de flechas \\(A' \to A\\)) y en \\(F\\) (respecto de transformaciones \\(F \Rightarrow F'\\)).

7. Enuncie y demuestre la versión covariante del lema de Yoneda: \\(\mathrm{Nat}(\mathcal{C}(A, -), F) \cong F(A)\\) para \\(F\colon \mathcal{C} \to \mathbf{Set}\\).

8. Use el lema de Yoneda para demostrar que \\((A \times B) \times C \cong A \times (B \times C)\\) en cualquier categoría con productos binarios, **sin construir el isomorfismo a mano**. *(Sugerencia: compare los funtores \\(\mathcal{C}(-, (A \times B) \times C)\\) y \\(\mathcal{C}(-, A \times (B \times C))\\).)*

9. Demuestre que, en una categoría con objeto terminal \\(1\\) y productos binarios, \\(A \times 1 \cong A\\).

10. Sea \\(U\colon \mathbf{CRing} \to \mathbf{Set}\\) el olvidadizo de los anillos **conmutativos**. Demuestre que \\(U \times U\\) es representable por \\(\mathbb{Z}[x, y]\\) y deduzca que la suma y la multiplicación de un anillo conmutativo provienen, vía Yoneda, de ciertos homomorfismos \\(\mathbb{Z}[t] \to \mathbb{Z}[x, y]\\). ¿Cuáles? ¿Qué anillo representa a \\(U \times U\\) si se trabaja en \\(\mathbf{Ring}\\), sin conmutatividad?

---

## 📝 Nivel 3. Exploración

11. **Seifert–van Kampen como propiedad universal.** Sea \\(X = U \cup V\\) con \\(U\\), \\(V\\) y \\(U \cap V\\) abiertos arco-conexos que contienen al punto base. Enuncie el teorema de Seifert–van Kampen como una propiedad universal: \\(\pi\_1(X)\\) es el objeto universal entre los grupos que reciben homomorfismos de \\(\pi\_1(U)\\) y \\(\pi\_1(V)\\) que coinciden en \\(\pi\_1(U \cap V)\\). Use este enunciado para calcular el grupo fundamental de la figura ocho.

12. **Grupos de nudos.** La presentación de Wirtinger expresa el grupo de un nudo como un cociente de un grupo libre por relaciones, una por cruce. Describa esa construcción como una composición de flechas universales (Definición 4.9): primero libre, luego cociente. ¿Qué propiedad universal tiene el resultado?

13. **Ínfimos y medición.** En un conjunto de puntajes ordenado parcialmente por dominancia (el puntaje \\(a\\) domina a \\(b\\) si es mayor o igual en todas las subescalas), ¿qué son el producto y el coproducto de dos puntajes? ¿Existen siempre? ¿Qué interpretación tienen?

---

## 💡 Soluciones seleccionadas

> **Solución al Ejercicio 4.**
> Un par de elementos que conmutan es lo mismo que un homomorfismo desde \\(\mathbb{Z}^2 = \mathbb{Z} \times \mathbb{Z}\\): los generadores \\(e\_1, e\_2\\) conmutan, y \\(\mathbb{Z}^2\\) es el grupo libre en dos generadores que conmutan. Explícitamente, el homomorfismo \\(f\colon \mathbb{Z}^2 \to G\\) corresponde al par \\((f(e\_1), f(e\_2))\\). El objeto representante es \\(\mathbb{Z}^2\\) y el elemento universal es el par \\((e\_1, e\_2)\\).

> **Solución al Ejercicio 8.**
> Para cada \\(X\\) hay biyecciones naturales en \\(X\\):
>
> \\[
> \mathcal{C}(X, (A \times B) \times C) \cong \mathcal{C}(X, A \times B) \times \mathcal{C}(X, C) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B) \times \mathcal{C}(X, C),
> \\]
>
> y lo mismo para \\(A \times (B \times C)\\). Luego \\(\mathcal{C}(-, (A \times B) \times C) \cong \mathcal{C}(-, A \times (B \times C))\\) y, por el Corolario 5.6, los objetos son isomorfos. El isomorfismo explícito se recupera aplicando la biyección del lema a la identidad: es \\(\langle \pi\_1 \pi\_1, \langle \pi\_2 \pi\_1, \pi\_2 \rangle \rangle\\).

> **Solución al Ejercicio 10.**
> Para \\(R\\) conmutativo, un homomorfismo \\(\mathbb{Z}[x,y] \to R\\) es la elección de dos elementos de \\(R\\), las imágenes de \\(x\\) e \\(y\\). La suma de \\(R\\) es una transformación natural \\(U \times U \Rightarrow U\\), es decir, \\(\mathbf{CRing}(\mathbb{Z}[x,y], -) \Rightarrow \mathbf{CRing}(\mathbb{Z}[t], -)\\). Por la versión covariante del lema de Yoneda (Ejercicio 7), esas transformaciones corresponden a homomorfismos \\(\mathbb{Z}[t] \to \mathbb{Z}[x,y]\\): la suma corresponde a \\(t \mapsto x + y\\) y la multiplicación a \\(t \mapsto xy\\). Esta es la idea germinal de ver la recta afín como un **objeto anillo** en la categoría de esquemas. En \\(\mathbf{Ring}\\), sin conmutatividad, un homomorfismo \\(\mathbb{Z}[x,y] \to R\\) es un par de elementos **que conmutan**; el representante de \\(U \times U\\) es el anillo de polinomios no conmutativos \\(\mathbb{Z}\langle x, y \rangle\\).

> **Guía para el Ejercicio 13.**
> El producto de dos puntajes es su mínimo coordenada por coordenada; el coproducto, su máximo coordenada por coordenada. Ambos existen si el conjunto de puntajes posibles es cerrado bajo esas operaciones, por ejemplo si es un producto de cadenas. Si solo se consideran los puntajes observados en una muestra, en general no existen. La diferencia entre ambas situaciones ilustra que una propiedad universal depende de la categoría en la que se plantea.
