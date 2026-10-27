# 12. Categorías monoidales

## Hilo conductor

El producto tensorial de espacios vectoriales es asociativo, pero no de manera literal: \\((U \otimes V) \otimes W\\) y \\(U \otimes (V \otimes W)\\) son espacios distintos, unidos por un isomorfismo canónico. Lo mismo ocurre con el producto cartesiano de conjuntos. Una **categoría monoidal** es una categoría con una manera de "multiplicar" objetos y flechas, asociativa y unitaria salvo isomorfismos coherentes. Este capítulo la define, demuestra que **una mónada es un monoide en la categoría de endofuntores**, introduce los **diagramas de cuerdas** y prepara, con los objetos duales, el terreno de los nudos.

## Ideas previas que se cristalizan

- \\((U \otimes V) \otimes W \cong U \otimes (V \otimes W)\\) y \\(k \otimes V \cong V\\).
- \\((A \times B) \times C \cong A \times (B \times C)\\) y \\(\\{\star\\} \times A \cong A\\).
- Un anillo es un grupo abeliano con una multiplicación bilineal, asociativa y con unidad.
- La traza de una transformación lineal no depende de la base.
- Los axiomas de mónada tienen la forma de los axiomas de monoide (Capítulo 10).

---

## 1. La definición

> **Definición 12.1 (Categoría monoidal).**
> Una **categoría monoidal** \\((\mathcal{V}, \otimes, I, \alpha, \lambda, \rho)\\) consta de una categoría \\(\mathcal{V}\\), un funtor \\(\otimes\colon \mathcal{V} \times \mathcal{V} \to \mathcal{V}\\) (el **producto tensorial**), un objeto \\(I\\) (la **unidad**) e isomorfismos naturales
>
> \\[
> \alpha\_{A,B,C}\colon (A \otimes B) \otimes C \to A \otimes (B \otimes C), \qquad \lambda\_A\colon I \otimes A \to A, \qquad \rho\_A\colon A \otimes I \to A,
> \\]
>
> llamados **asociador** y **unitores**, que satisfacen dos axiomas de coherencia:
>
> - **Pentágono:** para todos \\(A, B, C, D\\),
>
> \\[
> (1\_A \otimes \alpha\_{B,C,D}) \circ \alpha\_{A, B \otimes C, D} \circ (\alpha\_{A,B,C} \otimes 1\_D) = \alpha\_{A,B,C \otimes D} \circ \alpha\_{A \otimes B, C, D}.
> \\]
>
> - **Triángulo:** \\((1\_A \otimes \lambda\_B) \circ \alpha\_{A,I,B} = \rho\_A \otimes 1\_B\\).
>
> Si \\(\alpha\\), \\(\lambda\\) y \\(\rho\\) son identidades, la categoría monoidal es **estricta**.

El pentágono compara las dos maneras de reasociar \\(((A \otimes B) \otimes C) \otimes D\\) hasta \\(A \otimes (B \otimes (C \otimes D))\\): una con tres pasos y otra con dos. ¿Por qué basta con exigir solo esto?

> **Teorema 12.2 (Coherencia de Mac Lane, 1963).**
> En una categoría monoidal, todo diagrama **formal** construido solo con \\(\alpha\\), \\(\lambda\\), \\(\rho\\), sus inversas, identidades y \\(\otimes\\) conmuta. Una forma relacionada del teorema: toda categoría monoidal es equivalente, mediante un funtor monoidal fuerte, a una categoría monoidal estricta.

La consecuencia práctica es que se pueden **omitir los paréntesis** y los isomorfismos canónicos: cualquier manera de insertarlos da el mismo resultado. "Formal" significa que el diagrama se obtiene al sustituir objetos en un diagrama de palabras abstractas; la precisión se debe a Kelly, que corrigió un descuido de la prueba original de Mac Lane. Es la justificación rigurosa de escribir \\(A \otimes B \otimes C\\) sin más.

> **Ejemplo 12.3 (Categorías monoidales).**
>
> | Categoría | \\(\otimes\\) | Unidad | Observación |
> | :--- | :--- | :--- | :--- |
> | \\(\mathbf{Set}\\) | \\(\times\\) | \\(\\{\star\\}\\) | **Cartesiana**: el tensor es el producto |
> | \\(\mathbf{Set}\\) | \\(\sqcup\\) | \\(\emptyset\\) | **Cocartesiana** |
> | \\(\mathbf{Vect}\_k\\) | \\(\otimes\_k\\) | \\(k\\) | No es el producto (\\(\oplus\\)) |
> | \\(\mathbf{Ab}\\) | \\(\otimes\_{\mathbb{Z}}\\) | \\(\mathbb{Z}\\) | |
> | \\(\mathbf{Mat}\_k\\) | Producto de Kronecker | \\(1\\) | En objetos, \\(n \otimes m = nm\\) |
> | \\([\mathcal{C}, \mathcal{C}]\\) | Composición \\(\circ\\) | \\(1\_{\mathcal{C}}\\) | **Estricta**; no conmutativa |
> | \\(([0, \infty], \ge)\\) como orden | \\(+\\) | \\(0\\) | Base de los espacios métricos de Lawvere |
> | Núcleos de Markov finitos | Producto de distribuciones independientes | \\(\\{\star\\}\\) | Ver el Capítulo 11 |

En la última fila, el tensor de dos núcleos \\(f\colon X \rightsquigarrow Y\\) y \\(g\colon X' \rightsquigarrow Y'\\) es el núcleo \\(X \times X' \rightsquigarrow Y \times Y'\\) que actúa de manera **independiente** en cada coordenada: \\((f \otimes g)(y, y' \mid x, x') = f(y \mid x)\\, g(y' \mid x')\\). Con él se expresa la independencia local del Capítulo 11, aunque no directamente: todos los reactivos dependen de **la misma** clase \\(\theta\\), así que primero se copia la clase con la diagonal \\(\Theta \to \Theta^n\\) y después se aplica en paralelo un núcleo por reactivo, \\((f\_1 \otimes \cdots \otimes f\_n) \circ \mathrm{copia}\_\Theta\\). El Ejercicio 11 de la Parte VI muestra que esa copia no es natural.

---

## 2. Monoides en una categoría monoidal

> **Definición 12.4 (Monoide).**
> Un **monoide** en \\((\mathcal{V}, \otimes, I)\\) es un objeto \\(M\\) con flechas \\(m\colon M \otimes M \to M\\) y \\(e\colon I \to M\\) tales que
>
> \\[
> m \circ (m \otimes 1) = m \circ (1 \otimes m) \circ \alpha, \qquad m \circ (e \otimes 1) = \lambda, \qquad m \circ (1 \otimes e) = \rho.
> \\]

> **Ejemplo 12.5.**
>
> | Categoría monoidal | Sus monoides |
> | :--- | :--- |
> | \\((\mathbf{Set}, \times, \\{\star\\})\\) | Monoides usuales |
> | \\((\mathbf{Ab}, \otimes, \mathbb{Z})\\) | **Anillos**: la multiplicación bilineal es una flecha \\(R \otimes R \to R\\) |
> | \\((\mathbf{Vect}\_k, \otimes, k)\\) | **\\(k\\)-álgebras** asociativas con unidad |
> | \\((\mathbf{Top}, \times, \star)\\) | Monoides topológicos |
> | \\(([\mathcal{C}, \mathcal{C}], \circ, 1)\\) | **Mónadas sobre \\(\mathcal{C}\\)** |

La última fila merece un teorema.

> **Teorema 12.6 (Una mónada es un monoide en los endofuntores).**
> Las mónadas sobre \\(\mathcal{C}\\) son exactamente los monoides en la categoría monoidal estricta \\(([\mathcal{C}, \mathcal{C}], \circ, 1\_{\mathcal{C}})\\).
>
> *Demostración.* Un monoide en esa categoría es un objeto \\(T\\) (un endofuntor) con flechas \\(m\colon T \circ T \Rightarrow T\\) y \\(e\colon 1 \Rightarrow T\\) (transformaciones naturales). El tensor de dos flechas \\(\beta\colon S \Rightarrow S'\\) y \\(\gamma\colon R \Rightarrow R'\\) es su composición horizontal \\(\beta \gamma\colon SR \Rightarrow S'R'\\); en particular, \\(m \otimes 1\_T = mT\\) y \\(1\_T \otimes m = Tm\\). Como la categoría es estricta, los axiomas de monoide se leen
>
> \\[
> m \circ mT = m \circ Tm, \qquad m \circ eT = 1\_T = m \circ Te,
> \\]
>
> que son, letra por letra, los axiomas de mónada de la Definición 10.1 con \\(\mu = m\\) y \\(\eta = e\\). \\(\blacksquare\\)

La frase "una mónada es un monoide en la categoría de endofuntores" se volvió célebre como broma en la programación funcional, por su aparente oscuridad. Con lo visto hasta aquí, es una observación de una línea.

> **📝 Para pensar.** Un anillo es un monoide en \\(\mathbf{Ab}\\); una mónada, un monoide en los endofuntores. ¿Qué serían los "módulos" sobre una mónada? Compara con las álgebras de Eilenberg–Moore del Capítulo 10: ¿qué papel juega en ellas la acción \\(TA \to A\\)?

---

## 3. Funtores monoidales y simetría

> **Definición 12.7 (Funtor monoidal).**
> Un **funtor monoidal fuerte** \\(F\colon (\mathcal{V}, \otimes, I) \to (\mathcal{W}, \otimes, J)\\) es un funtor con isomorfismos naturales \\(FA \otimes FB \cong F(A \otimes B)\\) y \\(J \cong FI\\), compatibles con los asociadores y unitores. Si solo se piden flechas \\(FA \otimes FB \to F(A \otimes B)\\) y \\(J \to FI\\), no necesariamente invertibles, el funtor es **laxo**.

> **Ejemplo 12.8.**
> El espacio vectorial libre \\(k^{(-)}\colon (\mathbf{Set}, \times) \to (\mathbf{Vect}\_k, \otimes)\\) es monoidal fuerte: \\(k^{(X \times Y)} \cong k^{(X)} \otimes k^{(Y)}\\), porque los pares \\((x, y)\\) forman una base del producto tensorial.

> **Definición 12.9 (Simetría).**
> Una **categoría monoidal simétrica** es una categoría monoidal con isomorfismos naturales \\(s\_{A,B}\colon A \otimes B \to B \otimes A\\) que cumplen \\(s\_{B,A} \circ s\_{A,B} = 1\_{A \otimes B}\\) y un axioma de compatibilidad con \\(\alpha\\) (el **hexágono**).

\\(\mathbf{Set}\\), \\(\mathbf{Vect}\_k\\) y \\(\mathbf{Ab}\\) son simétricas, con \\(s(a, b) = (b, a)\\) y \\(s(u \otimes v) = v \otimes u\\). La categoría de endofuntores no lo es: \\(S \circ T\\) y \\(T \circ S\\) suelen ser distintos. El Capítulo 13 estudia qué pasa si se conserva el isomorfismo \\(s\\) pero se **abandona** la ecuación \\(s \circ s = 1\\). Esa sola omisión es la puerta a los nudos.

---

## 4. Diagramas de cuerdas

Las expresiones con \\(\otimes\\) y \\(\circ\\) se vuelven ilegibles pronto. Los **diagramas de cuerdas** las reemplazan por dibujos con estas convenciones:

- un **objeto** es una cuerda vertical, y la unidad \\(I\\) es la ausencia de cuerda;
- una **flecha** \\(f\colon A \to B\\) es una caja con la cuerda \\(A\\) entrando por abajo y la cuerda \\(B\\) saliendo por arriba;
- la **composición** \\(g \circ f\\) es apilar la caja \\(g\\) sobre la caja \\(f\\);
- el **producto tensorial** \\(f \otimes g\\) es poner las cajas lado a lado.

En un diagrama de cuerdas, la ley de intercambio \\((g \otimes g') \circ (f \otimes f') = (g \circ f) \otimes (g' \circ f')\\), que es la funtorialidad de \\(\otimes\\), se vuelve invisible: ambos lados son el mismo dibujo. El teorema de Joyal y Street (1991) garantiza que el razonamiento con diagramas es correcto: **dos expresiones son iguales por los axiomas de categoría monoidal si y solo si sus diagramas son isotópicos en el plano** mediante una isotopía **progresiva**, en la que ninguna cuerda se devuelve. Las cuerdas que se devuelven aparecen solo con los objetos duales de la Sección 5.

---

## 5. Objetos duales: la primera curva

> **Definición 12.10 (Dual).**
> Un objeto \\(A\\) de una categoría monoidal tiene un **dual** \\(A^{\ast}\\) si existen flechas
>
> \\[
> \mathrm{ev}\colon A^{\ast} \otimes A \to I, \qquad \mathrm{coev}\colon I \to A \otimes A^{\ast},
> \\]
>
> que cumplen las **identidades del zigzag** (omitiendo asociadores y unitores):
>
> \\[
> (1\_A \otimes \mathrm{ev}) \circ (\mathrm{coev} \otimes 1\_A) = 1\_A, \qquad (\mathrm{ev} \otimes 1\_{A^{\ast}}) \circ (1\_{A^{\ast}} \otimes \mathrm{coev}) = 1\_{A^{\ast}}.
> \\]

En diagramas de cuerdas, \\(\mathrm{coev}\\) es una **copa** (una cuerda que nace en forma de U) y \\(\mathrm{ev}\\) es una **tapa** (una cuerda que muere en forma de U invertida). La primera identidad del zigzag dice que **una cuerda en forma de S se puede estirar**:

<div style="text-align: center; margin: 20px 0;">
<svg viewBox="0 0 240 170" width="260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Identidad del zigzag: una cuerda en forma de S es igual a una cuerda recta">
<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">
<path d="M100 150 L100 65 A20 20 0 0 0 60 65 L60 105 A20 20 0 0 1 20 105 L20 20"/>
<path d="M190 150 L190 20"/>
</g>
<g fill="currentColor" font-family="serif" font-size="15">
<text x="80" y="38" text-anchor="middle">ev</text>
<text x="40" y="142" text-anchor="middle">coev</text>
<text x="145" y="92" text-anchor="middle">=</text>
<text x="108" y="160">A</text>
<text x="28" y="22">A</text>
<text x="198" y="160">A</text>
<text x="198" y="22">A</text>
</g>
</svg>
</div>

Esta es la primera vez que una ecuación algebraica coincide con un movimiento geométrico de una curva. No es todavía un movimiento de Reidemeister, porque no hay cruces: es una **isotopía plana**. En el Capítulo 13 se verá que estas isotopías, junto con los movimientos de Reidemeister, son las relaciones que definen los enredos.

> **Ejemplo 12.11 (Espacios de dimensión finita).**
> En \\(\mathbf{Vect}\_k\\), un espacio \\(V\\) tiene dual si y solo si es de dimensión finita. Para una base \\(e\_1, \dots, e\_n\\) con base dual \\(e^1, \dots, e^n\\):
>
> \\[
> \mathrm{ev}(\varphi \otimes v) = \varphi(v), \qquad \mathrm{coev}(1) = \sum\_i e\_i \otimes e^i.
> \\]
>
> El elemento \\(\sum\_i e\_i \otimes e^i\\) no depende de la base elegida. En una categoría simétrica, la **traza** de \\(f\colon V \to V\\) se define sin coordenadas como el compuesto
>
> \\[
> I \xrightarrow{\mathrm{coev}} V \otimes V^{\ast} \xrightarrow{f \otimes 1} V \otimes V^{\ast} \xrightarrow{s} V^{\ast} \otimes V \xrightarrow{\mathrm{ev}} I,
> \\]
>
> y la **dimensión** de \\(V\\) es la traza de la identidad. En diagramas, la traza es **cerrar la cuerda en un lazo**. Un lazo cerrado sin cajas es un número: la dimensión.

---

## 🔑 Lo que cristalizó

- Una **categoría monoidal** tiene un producto tensorial asociativo y unitario salvo isomorfismos coherentes; el **teorema de coherencia** permite omitir los paréntesis.
- Monoides en \\(\mathbf{Set}\\), \\(\mathbf{Ab}\\) y \\(\mathbf{Vect}\_k\\) son monoides, anillos y álgebras; en los endofuntores, son **mónadas**.
- Los **diagramas de cuerdas** representan cálculos monoidales; dos expresiones iguales corresponden a dibujos isotópicos.
- Los **objetos duales** introducen copas y tapas; la identidad del zigzag es estirar una cuerda, y la traza es cerrar un lazo.

## 🌉 Puente

En una categoría simétrica, cruzar dos cuerdas y volver a cruzarlas deja todo como estaba: \\(s \circ s = 1\\). ¿Y si los cruces tuvieran "arriba" y "abajo", como en el diagrama de un nudo? El Capítulo 13 abandona esa ecuación y llega a las trenzas, los enredos y los invariantes de nudos.
