# 9. Adjunciones, límites y equivalencias

## Hilo conductor

El Capítulo 8 encontró adjunciones en todas partes. Este capítulo muestra qué consecuencias tiene saber que un funtor es adjunto. La principal: **los adjuntos derechos preservan límites y los adjuntos izquierdos preservan colímites**. De este solo resultado se siguen hechos tan distintos como que el grupo libre sobre una unión disjunta es un producto libre, que el producto cartesiano distribuye sobre la unión disjunta, que el cuantificador existencial distribuye sobre la disyunción, y que la inclusión de los grupos abelianos en los grupos no tiene adjunto derecho.

## Ideas previas que se cristalizan

- \\(f(S \cup S') = f(S) \cup f(S')\\), pero en general \\(f(S \cap S') \neq f(S) \cap f(S')\\).
- \\(f^{-1}\\) preserva uniones **e** intersecciones.
- \\(\exists x\\, (\varphi \vee \psi) \equiv \exists x\\, \varphi \vee \exists x\\, \psi\\), y \\(\forall x\\, (\varphi \wedge \psi) \equiv \forall x\\, \varphi \wedge \forall x\\, \psi\\).
- \\((A \sqcup A') \times B \cong (A \times B) \sqcup (A' \times B)\\).

---

## 1. Los adjuntos son únicos

> **Proposición 9.1.**
> Si \\(F \dashv G\\) y \\(F \dashv G'\\), entonces \\(G \cong G'\\) de manera natural. Dualmente, un funtor tiene a lo más un adjunto izquierdo salvo isomorfismo.
>
> *Demostración.* Para cada \\(Y\\) hay biyecciones naturales en \\(X\\):
>
> \\[
> \mathcal{C}(X, GY) \cong \mathcal{D}(FX, Y) \cong \mathcal{C}(X, G'Y).
> \\]
>
> Por el Corolario 5.6 (Yoneda), \\(GY \cong G'Y\\). La naturalidad en \\(Y\\) de las biyecciones da la naturalidad del isomorfismo. \\(\blacksquare\\)

Por eso tiene sentido hablar de **el** adjunto de un funtor. Por ejemplo, cualquier construcción del grupo libre (palabras reducidas, presentaciones, acciones sobre árboles) da el mismo funtor salvo isomorfismo natural.

---

## 2. Los adjuntos derechos preservan límites

> **Teorema 9.2 (Los adjuntos derechos preservan límites).**
> Si \\(F \dashv G\\), con \\(G\colon \mathcal{D} \to \mathcal{C}\\), entonces \\(G\\) preserva todos los límites que existen en \\(\mathcal{D}\\). Dualmente, \\(F\\) preserva todos los colímites que existen en \\(\mathcal{C}\\).
>
> *Demostración.* Sea \\(D\colon \mathcal{J} \to \mathcal{D}\\) un diagrama con límite \\((L, (\pi\_j))\\). Hay que ver que \\((GL, (G\pi\_j))\\) es un límite de \\(G \circ D\\).
>
> Sea \\((X, (\lambda\_j))\\) un cono sobre \\(G \circ D\\), con \\(\lambda\_j\colon X \to G D(j)\\). Sus transpuestas \\(\overline{\lambda\_j}\colon FX \to D(j)\\) forman un cono sobre \\(D\\): para \\(u\colon j \to k\\), la naturalidad de la transposición da
>
> \\[
> D(u) \circ \overline{\lambda\_j} = \overline{G D(u) \circ \lambda\_j} = \overline{\lambda\_k}.
> \\]
>
> Por la propiedad universal de \\(L\\), existe una única \\(h\colon FX \to L\\) con \\(\pi\_j \circ h = \overline{\lambda\_j}\\). Al transponer, \\(\overline{h}\colon X \to GL\\) cumple
>
> \\[
> G(\pi\_j) \circ \overline{h} = \overline{\pi\_j \circ h} = \lambda\_j.
> \\]
>
> Si otra \\(h'\colon X \to GL\\) cumple lo mismo, su transpuesta factoriza el mismo cono a través de \\(L\\), así que coincide con \\(h\\), y \\(h' = \overline{h}\\). \\(\blacksquare\\)

La prueba consiste en **transponer, usar la propiedad universal y transponer de regreso**. Es el patrón típico de los argumentos con adjunciones.

> **Ejemplo 9.3 (Consecuencias inmediatas).**
>
> | Adjunción | Lo que se preserva | Hecho conocido que resulta |
> | :--- | :--- | :--- |
> | Libre \\(\dashv\\) olvidadizo (grupos) | \\(U\\) preserva límites; \\(F\\) preserva colímites | \\(F(X \sqcup Y) \cong F(X) \ast F(Y)\\) |
> | \\(- \times B \dashv (-)^B\\) | \\(- \times B\\) preserva colímites | \\((A \sqcup A') \times B \cong (A \times B) \sqcup (A' \times B)\\) |
> | \\(\exists\_f \dashv f^{-1} \dashv \forall\_f\\) | \\(\exists\_f\\) preserva uniones; \\(f^{-1}\\) preserva todo; \\(\forall\_f\\) preserva intersecciones | \\(\exists\\) distribuye sobre \\(\vee\\); \\(\forall\\) sobre \\(\wedge\\) |
> | \\(\lceil - \rceil \dashv i\\) | \\(\lceil - \rceil\\) preserva supremos | \\(\lceil \max(x, y) \rceil = \max(\lceil x \rceil, \lceil y \rceil)\\) |
> | \\(D \dashv U \dashv I\\) (topología) | \\(U\\) preserva límites y colímites | Los límites y colímites de espacios tienen el conjunto subyacente esperado |

El teorema también sirve para demostrar que un adjunto **no existe**.

> **Ejemplo 9.4 (Un adjunto que no existe).**
> La inclusión \\(i\colon \mathbf{Ab} \to \mathbf{Grp}\\) tiene adjunto izquierdo, la abelianización. ¿Tiene adjunto derecho? Si lo tuviera, sería adjunto izquierdo y preservaría coproductos. Pero el coproducto de \\(\mathbb{Z}\\) y \\(\mathbb{Z}\\) en \\(\mathbf{Ab}\\) es \\(\mathbb{Z} \oplus \mathbb{Z}\\), abeliano, mientras que en \\(\mathbf{Grp}\\) es \\(\mathbb{Z} \ast \mathbb{Z}\\), que no lo es. Luego \\(i\\) no tiene adjunto derecho.

> **📝 Para pensar.** En la tabla, \\(\exists\_f\\) preserva uniones pero no intersecciones. Busca un ejemplo con \\(f\\) no inyectiva y \\(S, S'\\) disjuntos con \\(f(S) = f(S')\\). ¿Qué te dice el ejemplo sobre la regla lógica \\(\exists x\\, (\varphi \wedge \psi) \to \exists x\\, \varphi \wedge \exists x\\, \psi\\), y sobre su recíproca?

---

## 3. El teorema del funtor adjunto

El Teorema 9.2 da una condición necesaria para tener adjunto izquierdo: preservar límites. ¿Es suficiente? Casi.

> **Teorema 9.5 (Teorema general del funtor adjunto de Freyd).**
> Sea \\(\mathcal{D}\\) completa y localmente pequeña, y sea \\(G\colon \mathcal{D} \to \mathcal{C}\\) un funtor que preserva límites. Si para cada objeto \\(X\\) de \\(\mathcal{C}\\) existe un **conjunto** \\(S\_X\\) de flechas \\(X \to GY\\) tal que toda flecha \\(f\colon X \to GY'\\) se factoriza como \\(f = G(t) \circ s\\), con \\(s\colon X \to GY\\) en \\(S\_X\\) y \\(t\colon Y \to Y'\\) en \\(\mathcal{D}\\) (la **condición del conjunto solución**), entonces \\(G\\) tiene adjunto izquierdo.

La prueba (Mac Lane, Capítulo V; Riehl, Capítulo 4) construye la flecha universal desde \\(X\\) como un límite. La condición de tamaño es indispensable y es la única parte delicada. Para los olvidadizos de estructuras algebraicas se verifica con un argumento de cardinalidad: todo homomorfismo desde lo generado por \\(X\\) tiene imagen de cardinalidad acotada. El resultado garantiza la **existencia** de grupos libres, anillos de polinomios y otras construcciones sin necesidad de construirlos explícitamente.

---

## 4. Adjunciones, subcategorías reflexivas y equivalencias

> **Proposición 9.6.**
> Sea \\(F \dashv G\\) con counidad \\(\varepsilon\\). El funtor \\(G\\) es plenamente fiel si y solo si \\(\varepsilon\\) es un isomorfismo natural.
>
> *Demostración.* La función \\(\mathcal{D}(Y, Y') \to \mathcal{C}(GY, GY')\\) inducida por \\(G\\), compuesta con la biyección \\(\mathcal{C}(GY, GY') \cong \mathcal{D}(FGY, Y')\\), es la función \\(h \mapsto h \circ \varepsilon\_Y\\) (por la fórmula \\(\overline{f} = \varepsilon \circ F(f)\\) y la naturalidad de \\(\varepsilon\\)). Luego \\(G\\) es plenamente fiel si y solo si precomponer con \\(\varepsilon\_Y\\) es biyectivo para todo \\(Y'\\). Por Yoneda (en \\(\mathcal{D}^{\mathrm{op}}\\)), eso ocurre si y solo si \\(\varepsilon\_Y\\) es un isomorfismo. \\(\blacksquare\\)

Así, en una **subcategoría reflexiva** (Ejemplo 8.7) la counidad es un isomorfismo: reflejar un objeto que ya está en la subcategoría no lo cambia. Por ejemplo, la abelianización de un grupo abeliano es él mismo.

> **Proposición 9.7 (Equivalencias adjuntas).**
> Si \\(F\colon \mathcal{C} \to \mathcal{D}\\) es una equivalencia, entonces existe \\(G\\) con \\(F \dashv G\\) tal que la unidad y la counidad son isomorfismos naturales. Una adjunción así se llama **equivalencia adjunta**.

La prueba consiste en corregir uno de los dos isomorfismos de la Definición 3.9 para que se cumplan las identidades triangulares (véanse los capítulos sobre adjunciones de Riehl y de Leinster). La moraleja: **una equivalencia es una adjunción en la que nada se pierde en ningún sentido**.

---

## 5. Composición de adjunciones

> **Proposición 9.8.**
> Si \\(F \dashv G\\), con \\(F\colon \mathcal{C} \to \mathcal{D}\\), y \\(F' \dashv G'\\), con \\(F'\colon \mathcal{D} \to \mathcal{E}\\), entonces \\(F' F \dashv G G'\\).
>
> *Demostración.* \\(\mathcal{E}(F'FX, Z) \cong \mathcal{D}(FX, G'Z) \cong \mathcal{C}(X, GG'Z)\\), natural en \\(X\\) y en \\(Z\\). \\(\blacksquare\\)

> **Ejemplo 9.9.**
> El grupo libre seguido de la abelianización es adjunto izquierdo del olvidadizo \\(\mathbf{Ab} \to \mathbf{Grp} \to \mathbf{Set}\\). Por la unicidad de los adjuntos (Proposición 9.1), coincide con el **grupo abeliano libre** \\(\mathbb{Z}^{(X)}\\). Se obtiene, sin cálculo, que \\(F(X)^{\mathrm{ab}} \cong \mathbb{Z}^{(X)}\\).

---

## 🔑 Lo que cristalizó

- Los adjuntos son **únicos** salvo isomorfismo natural; la prueba es el lema de Yoneda.
- **Adjuntos derechos preservan límites; adjuntos izquierdos preservan colímites.** El patrón de prueba es transponer, usar la propiedad universal y transponer de regreso.
- Las leyes de distribución de los cuantificadores, del producto sobre la unión disjunta y del grupo libre sobre la unión son casos de ese teorema.
- Preservar límites es casi suficiente para tener adjunto izquierdo; falta una condición de tamaño (teorema de Freyd).
- Las equivalencias son adjunciones con unidad y counidad invertibles.

## 🌉 Puente

Una adjunción \\(F \dashv G\\) produce un endofuntor \\(T = GF\colon \mathcal{C} \to \mathcal{C}\\), con dos transformaciones naturales: la unidad \\(\eta\colon 1 \Rightarrow GF\\) y \\(G\varepsilon F\colon GFGF \Rightarrow GF\\). ¿Qué estructura tienen estos datos, vistos solo desde \\(\mathcal{C}\\)? Esa estructura es una **mónada**, el tema de la Parte V.
