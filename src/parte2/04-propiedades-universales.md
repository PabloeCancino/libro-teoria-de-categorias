# 4. Propiedades universales

## Hilo conductor

¿Qué es el producto cartesiano \\(A \times B\\)? La respuesta escolar es "el conjunto de pares ordenados". Pero esa respuesta depende de cómo se codifiquen los pares, y por eso no captura lo esencial. Lo esencial es que **dar una función hacia \\(A \times B\\) equivale a dar un par de funciones, una hacia \\(A\\) y otra hacia \\(B\\)**. Esta descripción no menciona elementos: habla solo de flechas. Por eso tiene sentido en cualquier categoría, y en cada una produce la construcción "correcta": el producto directo de grupos, la topología producto o el máximo común divisor. Este capítulo enseña a describir objetos por su **propiedad universal**.

## Ideas previas que se cristalizan

- Una función \\(X \to A \times B\\) es lo mismo que un par de funciones \\(X \to A\\), \\(X \to B\\).
- Un homomorfismo desde el grupo libre \\(F(S)\\) queda determinado por sus valores en los generadores, y estos se pueden escoger libremente.
- Un homomorfismo \\(G \to H\\) que se anula en \\(N\\) se factoriza de manera única por \\(G/N\\).
- La topología producto es la topología más gruesa que hace continuas las proyecciones.
- El máximo común divisor es el mayor divisor común; el mínimo común múltiplo, el menor múltiplo común.

---

## 1. Objetos iniciales y terminales

> **Definición 4.1 (Inicial y terminal).**
> Un objeto \\(I\\) de \\(\mathcal{C}\\) es **inicial** si para cada objeto \\(X\\) existe exactamente una flecha \\(I \to X\\). Un objeto \\(T\\) es **terminal** si para cada \\(X\\) existe exactamente una flecha \\(X \to T\\). Un objeto a la vez inicial y terminal se llama **objeto cero**.

> **Proposición 4.2 (Unicidad salvo isomorfismo único).**
> Si \\(I\\) e \\(I'\\) son objetos iniciales, existe un único isomorfismo \\(I \to I'\\).
>
> *Demostración.* Por ser \\(I\\) inicial, hay una única flecha \\(f\colon I \to I'\\); por ser \\(I'\\) inicial, una única \\(g\colon I' \to I\\). Entonces \\(g \circ f\colon I \to I\\). Pero \\(1\_I\\) también es una flecha \\(I \to I\\), y por la unicidad, \\(g \circ f = 1\_I\\). Del mismo modo, \\(f \circ g = 1\_{I'}\\). \\(\blacksquare\\)

Esta demostración de cuatro líneas es el **molde de todas las unicidades** de este capítulo. En la Sección 5 se verá que todas las propiedades universales son objetos iniciales o terminales en alguna categoría, de modo que esta prueba basta para todas.

> **Ejemplo 4.3.**
>
> | Categoría | Objeto inicial | Objeto terminal |
> | :--- | :--- | :--- |
> | \\(\mathbf{Set}\\) | \\(\emptyset\\) | Cualquier conjunto con un elemento |
> | \\(\mathbf{Top}\\) | El espacio vacío | El espacio con un punto |
> | \\(\mathbf{Grp}\\), \\(\mathbf{Ab}\\), \\(\mathbf{Vect}\_k\\) | El grupo trivial, o el espacio cero (objeto cero) | El mismo |
> | \\(\mathbf{Ring}\\) | \\(\mathbb{Z}\\) | El anillo cero |
> | Orden parcial \\(P\\) | El mínimo, si existe | El máximo, si existe |
>
> Que \\(\mathbb{Z}\\) sea inicial en \\(\mathbf{Ring}\\) dice que hay un único homomorfismo \\(\mathbb{Z} \to R\\) para cada anillo \\(R\\), forzado por \\(1 \mapsto 1\\). La **característica** de \\(R\\) se lee en el núcleo de esa flecha única.

---

## 2. Productos

> **Definición 4.4 (Producto).**
> Sean \\(A, B\\) objetos de \\(\mathcal{C}\\). Un **producto** de \\(A\\) y \\(B\\) es un objeto \\(P\\) con dos flechas \\(\pi\_1\colon P \to A\\) y \\(\pi\_2\colon P \to B\\) (las **proyecciones**) tal que, para todo objeto \\(X\\) y todo par \\(f\colon X \to A\\), \\(g\colon X \to B\\), existe **una única** flecha \\(\langle f, g \rangle\colon X \to P\\) que cumple
>
> \\[
> \pi\_1 \circ \langle f, g \rangle = f, \qquad \pi\_2 \circ \langle f, g \rangle = g.
> \\]
>
> Se escribe \\(P = A \times B\\).

El diagrama de la propiedad universal es

\\[
\begin{array}{ccccc}
 & & X & & \\\\
 & \swarrow^{f} & \Big\downarrow{\scriptstyle \langle f,g \rangle} & \searrow^{g} & \\\\
A & \xleftarrow{\ \pi\_1\ } & A \times B & \xrightarrow{\ \pi\_2\ } & B
\end{array}
\\]

y la frase clave es: **una flecha hacia el producto es lo mismo que un par de flechas hacia los factores**. En símbolos, hay una biyección

\\[
\mathcal{C}(X, A \times B) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B), \qquad h \mapsto (\pi\_1 \circ h, \pi\_2 \circ h).
\\]

Igual que los objetos iniciales, **el producto es único salvo isomorfismo único** compatible con las proyecciones (Ejercicio 2 de la Parte II).

> **Ejemplo 4.5 (Productos en las categorías conocidas).**
>
> - **\\(\mathbf{Set}\\):** el producto cartesiano con sus proyecciones; \\(\langle f, g \rangle(x) = (f(x), g(x))\\).
> - **\\(\mathbf{Grp}\\):** el producto directo con la operación componente a componente. Que \\(\langle f, g \rangle\\) sea homomorfismo es inmediato.
> - **\\(\mathbf{Top}\\):** el producto cartesiano con la **topología producto**. La propiedad universal **exige** esa topología: debe ser tan gruesa como para que toda \\(\langle f, g \rangle\\) con \\(f, g\\) continuas sea continua, y tan fina como para que las proyecciones sean continuas.
> - **Un orden parcial:** el producto de \\(a\\) y \\(b\\) es su **ínfimo** \\(a \wedge b\\), si existe. La propiedad universal dice: \\(x \le a\\) y \\(x \le b\\) si y solo si \\(x \le a \wedge b\\).
> - **\\((\mathbb{N}, \mid)\\), los naturales ordenados por divisibilidad:** el producto es el **máximo común divisor**. La propiedad universal es el teorema conocido: \\(d \mid a\\) y \\(d \mid b\\) si y solo si \\(d \mid \gcd(a,b)\\).

> **Ejemplo 4.6 (Productos infinitos y la topología de cajas).**
> El producto de una familia \\((A\_i)\_{i \in I}\\) se define de la misma manera, con una proyección por índice. En \\(\mathbf{Top}\\), el producto de una familia infinita lleva la topología producto (generada por los cilindros con finitas coordenadas restringidas) y **no** la topología de cajas. Con la topología de cajas, la función diagonal \\(\mathbb{R} \to \mathbb{R}^{\mathbb{N}}\\), \\(t \mapsto (t, t, \dots)\\), no es continua aunque cada coordenada lo sea. La teoría de categorías explica por qué la topología producto es la definición "correcta".

> **📝 Para pensar.** Antes de este capítulo, ¿cómo habrías justificado ante un estudiante que la topología producto se define con cilindros y no con cajas? Compara esa justificación con la que da la propiedad universal. ¿Cuál se apoya en una intuición y cuál en una necesidad?

---

## 3. Coproductos

Por dualidad, se invierten las flechas.

> **Definición 4.7 (Coproducto).**
> Un **coproducto** de \\(A\\) y \\(B\\) es un objeto \\(A + B\\) con flechas \\(\iota\_1\colon A \to A + B\\) e \\(\iota\_2\colon B \to A + B\\) (las **inclusiones**) tal que, para todo par \\(f\colon A \to X\\), \\(g\colon B \to X\\), existe una única \\([f, g]\colon A + B \to X\\) con \\([f,g] \circ \iota\_1 = f\\) y \\([f,g] \circ \iota\_2 = g\\).

> **Ejemplo 4.8 (Coproductos).**
>
> - **\\(\mathbf{Set}\\) y \\(\mathbf{Top}\\):** la **unión disjunta**. Una función desde \\(A \sqcup B\\) es dar una función en cada pedazo, sin condición de compatibilidad.
> - **\\(\mathbf{Grp}\\):** el **producto libre** \\(G \ast H\\), formado por las palabras reducidas que alternan elementos de \\(G\\) y de \\(H\\). No es el producto directo: en \\(G \ast H\\) los elementos de \\(G\\) y de \\(H\\) no conmutan. Ejemplo: \\(\mathbb{Z} \ast \mathbb{Z}\\) es el grupo libre en dos generadores, el grupo fundamental de la figura ocho.
> - **\\(\mathbf{Ab}\\) y \\(\mathbf{Vect}\_k\\):** la **suma directa** \\(A \oplus B\\), que coincide con el producto. Un objeto que es a la vez producto y coproducto de manera compatible se llama **biproducto**.
> - **Un orden parcial:** el **supremo** \\(a \vee b\\). En \\((\mathbb{N}, \mid)\\): el **mínimo común múltiplo**.

El teorema de Seifert–van Kampen, en su forma más sencilla, es un enunciado sobre coproductos con identificaciones: el grupo fundamental de una unión se calcula como un "producto libre amalgamado". Esa construcción es un **colímite**, el tema del Capítulo 6.

---

## 4. Flechas universales: lo libre, lo cociente, lo completado

Los productos describen un objeto por las flechas **que llegan** a él. Hay otra familia de propiedades universales que describen un objeto como **la mejor aproximación** de otro dentro de una categoría distinta.

> **Definición 4.9 (Flecha universal).**
> Sea \\(U\colon \mathcal{D} \to \mathcal{C}\\) un funtor y \\(C\\) un objeto de \\(\mathcal{C}\\). Una **flecha universal de \\(C\\) a \\(U\\)** es un par \\((A, \eta)\\), con \\(A\\) objeto de \\(\mathcal{D}\\) y \\(\eta\colon C \to UA\\) flecha de \\(\mathcal{C}\\), tal que para todo objeto \\(D\\) de \\(\mathcal{D}\\) y toda \\(f\colon C \to UD\\) existe una única \\(\bar{f}\colon A \to D\\) en \\(\mathcal{D}\\) con
>
> \\[
> U(\bar{f}) \circ \eta = f.
> \\]

> **Ejemplo 4.10 (Objetos libres).**
> Sea \\(U\colon \mathbf{Vect}\_k \to \mathbf{Set}\\) el olvidadizo y \\(X\\) un conjunto. La inclusión de la base \\(\eta\colon X \to U(k^{(X)})\\) es universal: toda función \\(f\colon X \to UW\\) se extiende de manera única a una transformación lineal \\(\bar{f}\colon k^{(X)} \to W\\). Es el principio conocido de que **una transformación lineal se define libremente en una base**. Lo mismo vale para el grupo libre (un homomorfismo se define libremente en los generadores) y para el monoide libre \\(L(X)\\).

> **Ejemplo 4.11 (Cocientes y abelianización).**
> Sea \\(i\colon \mathbf{Ab} \to \mathbf{Grp}\\) la inclusión. El cociente \\(q\colon G \to G^{\mathrm{ab}}\\) es una flecha universal de \\(G\\) a \\(i\\): todo homomorfismo de \\(G\\) en un grupo abeliano se factoriza de manera única por \\(G^{\mathrm{ab}}\\). La abelianización es **la mejor aproximación abeliana** de un grupo.

> **Ejemplo 4.12 (Más flechas universales).**
>
> - El **campo de fracciones** de un dominio entero \\(R\\): todo homomorfismo inyectivo de \\(R\\) en un campo se extiende de manera única a \\(\mathrm{Frac}(R)\\).
> - La **compactación de Stone–Čech** \\(X \to \beta X\\) de un espacio de Tychonoff: toda función continua de \\(X\\) en un compacto de Hausdorff se extiende de manera única a \\(\beta X\\).
> - La **completación** de un espacio métrico respecto de las funciones uniformemente continuas hacia espacios completos.

---

## 5. Toda propiedad universal es un objeto inicial

Las Definiciones 4.4, 4.7 y 4.9 se ven distintas, pero tienen la misma forma. Para verlo, se construye una categoría auxiliar.

> **Definición 4.13 (Categoría coma).**
> Dados \\(U\colon \mathcal{D} \to \mathcal{C}\\) y un objeto \\(C\\) de \\(\mathcal{C}\\), la **categoría coma** \\((C \downarrow U)\\) tiene por objetos los pares \\((D, f)\\) con \\(f\colon C \to UD\\). Una flecha \\((D, f) \to (D', f')\\) es una flecha \\(h\colon D \to D'\\) de \\(\mathcal{D}\\) tal que \\(U(h) \circ f = f'\\).

> **Proposición 4.14.**
> Una flecha universal de \\(C\\) a \\(U\\) es exactamente un objeto inicial de \\((C \downarrow U)\\). En consecuencia, es única salvo isomorfismo único.
>
> *Demostración.* Que \\((A, \eta)\\) sea inicial dice que para cada \\((D, f)\\) existe una única \\(h\colon A \to D\\) con \\(U(h) \circ \eta = f\\). Es la Definición 4.9 palabra por palabra. La unicidad es la Proposición 4.2. \\(\blacksquare\\)

Del mismo modo, el producto \\(A \times B\\) es un objeto terminal en la categoría de "conos" sobre \\(A\\) y \\(B\\): objetos \\(X\\) con un par de flechas \\(X \to A\\), \\(X \to B\\). El coproducto es un objeto inicial en la categoría dual. Así, **la Proposición 4.2 demuestra de una vez la unicidad de todas las construcciones universales**.

> **📝 Para pensar.** En tus cursos, ¿cuántas veces demostraste "por separado" que el grupo libre, el producto directo o el campo de fracciones son únicos salvo isomorfismo? ¿Qué ganas y qué pierdes al reducir todas esas pruebas a la Proposición 4.2?

---

## 🔑 Lo que cristalizó

- Una **propiedad universal** describe un objeto por sus flechas hacia o desde todos los demás, sin mencionar elementos.
- Productos, coproductos, objetos iniciales y terminales unifican el producto cartesiano, el producto directo, la topología producto, el ínfimo, el máximo común divisor, la unión disjunta, el producto libre y el supremo.
- Los objetos libres, los cocientes y las completaciones son **flechas universales**: las mejores aproximaciones de un objeto en otra categoría.
- Toda propiedad universal es un **objeto inicial o terminal** de una categoría adecuada, y por eso es única salvo isomorfismo único.

## 🌉 Puente

La biyección \\(\mathcal{C}(X, A \times B) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B)\\) sugiere algo más profundo: un objeto queda determinado por **el funtor** \\(\mathcal{C}(-, A)\\) que mide las flechas que llegan a él. El Capítulo 5 convierte esta sospecha en un teorema: el lema de Yoneda.
