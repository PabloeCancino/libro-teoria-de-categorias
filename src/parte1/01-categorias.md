# 1. Categorías: objetos, flechas y composición

## Hilo conductor

Un curso de álgebra estudia grupos y homomorfismos; uno de topología, espacios y funciones continuas; uno de álgebra lineal, espacios vectoriales y transformaciones lineales. En los tres casos hay **objetos**, hay **flechas** entre ellos, las flechas **se componen** y cada objeto tiene una flecha **identidad**. Este capítulo toma esa observación en serio: define la estructura común, la llama *categoría* y muestra que, además de describir áreas enteras, también describe objetos individuales como un grupo o un orden parcial.

## Ideas previas que se cristalizan

- La composición de funciones es asociativa y la función identidad es neutra.
- La composición de homomorfismos es un homomorfismo; la de funciones continuas, continua.
- Un orden parcial es reflexivo y transitivo.
- Un monoide tiene una operación asociativa con elemento neutro.

Las cuatro afirmaciones resultan ser **la misma afirmación** vista en contextos distintos.

---

## 1. La definición

> **Definición 1.1 (Categoría).**
> Una **categoría** \\(\mathcal{C}\\) consta de:
>
> 1. una clase \\(\mathrm{Ob}(\mathcal{C})\\) de **objetos**;
> 2. para cada par de objetos \\(A, B\\), un conjunto \\(\mathcal{C}(A,B)\\) de **flechas** (o **morfismos**) de \\(A\\) en \\(B\\); se escribe \\(f\colon A \to B\\) para \\(f \in \mathcal{C}(A,B)\\), y se dice que \\(A\\) es el **dominio** y \\(B\\) el **codominio** de \\(f\\);
> 3. para cada terna de objetos \\(A, B, C\\), una **ley de composición**
>
> \\[
> \mathcal{C}(B,C) \times \mathcal{C}(A,B) \to \mathcal{C}(A,C), \qquad (g, f) \mapsto g \circ f;
> \\]
>
> 4. para cada objeto \\(A\\), una flecha **identidad** \\(1\_A\colon A \to A\\).
>
> Estos datos deben cumplir dos axiomas:
>
> - **Asociatividad:** \\(h \circ (g \circ f) = (h \circ g) \circ f\\) para toda \\(f\colon A \to B\\), \\(g\colon B \to C\\), \\(h\colon C \to D\\).
> - **Unidad:** \\(f \circ 1\_A = f = 1\_B \circ f\\) para toda \\(f\colon A \to B\\).

La composición \\(g \circ f\\) solo está definida cuando el codominio de \\(f\\) coincide con el dominio de \\(g\\). Por eso una categoría es una estructura **parcial**: no cualquier par de flechas se compone.

Un **diagrama** es un dibujo de objetos y flechas. Se dice que **conmuta** si dos caminos cualesquiera con el mismo inicio y el mismo final dan la misma flecha compuesta. Por ejemplo, decir que el cuadrado

\\[
\require{AMScd}
\begin{CD}
A @>f>> B \\\\
@VhVV @VVgV \\\\
C @>>k> D
\end{CD}
\\]

conmuta significa exactamente que \\(g \circ f = k \circ h\\). Gran parte de la teoría consiste en afirmar que ciertos diagramas conmutan.

> **📝 Para pensar.** El axioma de asociatividad dice que en un camino de tres flechas no importa dónde se pongan los paréntesis. ¿Qué pasaría con la noción de "diagrama conmutativo" si la composición no fuera asociativa? ¿Tendría sentido hablar de "el" compuesto de un camino largo?

---

## 2. Categorías de estructuras

> **Ejemplo 1.2 (Las categorías de siempre).**
> En cada caso, la composición es la composición usual de funciones y la identidad es la función identidad.
>
> - \\(\mathbf{Set}\\): conjuntos y funciones.
> - \\(\mathbf{Grp}\\): grupos y homomorfismos. \\(\mathbf{Ab}\\): grupos abelianos y homomorfismos.
> - \\(\mathbf{Ring}\\): anillos con unidad y homomorfismos que envían \\(1\\) en \\(1\\).
> - \\(\mathbf{Vect}\_k\\): espacios vectoriales sobre un campo \\(k\\) y transformaciones lineales.
> - \\(\mathbf{Top}\\): espacios topológicos y funciones continuas.
> - \\(\mathbf{Pos}\\): conjuntos parcialmente ordenados y funciones monótonas (\\(x \le y \Rightarrow f(x) \le f(y)\\)).

Verificar que cada una es una categoría se reduce a dos hechos ya conocidos: la composición de dos morfismos de la estructura es otro morfismo de la estructura, y la identidad es un morfismo de la estructura. La asociatividad y la unidad se heredan de las funciones.

Hay categorías cuyas flechas **no son funciones**.

> **Ejemplo 1.3 (Relaciones).**
> La categoría \\(\mathbf{Rel}\\) tiene por objetos los conjuntos y por flechas \\(A \to B\\) las relaciones \\(R \subseteq A \times B\\). La composición de \\(R\colon A \to B\\) y \\(S\colon B \to C\\) es
>
> \\[
> S \circ R = \\{(a, c) \in A \times C \mid \exists b \in B, \ (a,b) \in R \text{ y } (b,c) \in S\\},
> \\]
>
> y la identidad de \\(A\\) es la diagonal \\(\Delta\_A = \\{(a,a) \mid a \in A\\}\\).

> **Ejemplo 1.4 (Matrices).**
> Sea \\(k\\) un campo. La categoría \\(\mathbf{Mat}\_k\\) tiene por objetos los números naturales. Una flecha \\(n \to m\\) es una matriz de tamaño \\(m \times n\\) con entradas en \\(k\\). La composición es el producto de matrices y la identidad de \\(n\\) es la matriz identidad \\(I\_n\\). La asociatividad de la composición es la asociatividad del producto de matrices.

El Ejemplo 1.4 es instructivo: los objetos son números, que no tienen "elementos" relevantes. Toda la información está en las flechas. Esta idea reaparecerá en el lema de Yoneda.

---

## 3. Estructuras que son categorías

Una categoría también puede ser **un solo objeto matemático** visto de otra manera.

> **Ejemplo 1.5 (Un orden parcial es una categoría).**
> Sea \\((P, \le)\\) un conjunto parcialmente ordenado. Se define una categoría con objetos los elementos de \\(P\\) y con **exactamente una flecha** \\(x \to y\\) si \\(x \le y\\), y ninguna en otro caso.
>
> - La **reflexividad** \\(x \le x\\) da la identidad \\(1\_x\\).
> - La **transitividad** (\\(x \le y\\) y \\(y \le z\\) implican \\(x \le z\\)) da la composición.
> - La asociatividad y la unidad son automáticas: entre dos objetos hay a lo más una flecha, así que dos flechas paralelas siempre coinciden.

Una categoría en la que entre dos objetos hay a lo más una flecha se llama **preorden**. Un orden parcial es un preorden con la propiedad adicional de la antisimetría.

> **Ejemplo 1.6 (Un monoide es una categoría con un objeto).**
> Sea \\((M, \cdot, e)\\) un monoide. Se define una categoría \\(\mathbf{B}M\\) con un único objeto \\(\star\\), con \\(\mathbf{B}M(\star, \star) = M\\), con composición \\(g \circ f = g \cdot f\\) y con identidad \\(1\_\star = e\\).
>
> Recíprocamente, si \\(\mathcal{C}\\) tiene un único objeto \\(\star\\), entonces \\(\mathcal{C}(\star,\star)\\) con la composición es un monoide. **Monoides y categorías con un objeto son lo mismo.**

> **Ejemplo 1.7 (Grupos y grupoides).**
> Un grupo \\(G\\) es un monoide en el que todo elemento es invertible. Visto como categoría \\(\mathbf{B}G\\), es una categoría con un objeto en la que **toda flecha es un isomorfismo** (Definición 1.10). Una categoría con cualquier número de objetos en la que toda flecha es un isomorfismo se llama **grupoide**. Ejemplo clave en topología: el **grupoide fundamental** de un espacio \\(X\\), cuyos objetos son los puntos de \\(X\\) y cuyas flechas son las clases de homotopía de caminos.

> **Ejemplo 1.8 (Categorías pequeñas con nombre).**
>
> - \\(\mathbf{0}\\): la categoría vacía.
> - \\(\mathbf{1}\\): un objeto y solo su identidad.
> - \\(\mathbf{2}\\): dos objetos \\(0, 1\\) y una única flecha no identidad \\(0 \to 1\\). Es el orden \\(\\{0 \le 1\\}\\) visto como categoría.
> - Una **categoría discreta** sobre un conjunto \\(S\\): los objetos son los elementos de \\(S\\) y las únicas flechas son las identidades.

> **📝 Para pensar.** En el Ejemplo 1.5, la flecha \\(x \to y\\) "no es nada": es solo el hecho \\(x \le y\\). En el Ejemplo 1.6, los objetos "no son nada": solo hay uno. Los preórdenes son categorías en las que solo importan los objetos; los monoides, categorías en las que solo importan las flechas. ¿Dónde ubicarías a \\(\mathbf{Set}\\) en ese espectro?

---

## 4. Construcciones con categorías

> **Definición 1.9 (Categoría opuesta).**
> Dada una categoría \\(\mathcal{C}\\), su **opuesta** \\(\mathcal{C}^{\mathrm{op}}\\) tiene los mismos objetos y una flecha \\(f^{\mathrm{op}}\colon B \to A\\) por cada flecha \\(f\colon A \to B\\) de \\(\mathcal{C}\\). La composición se define por \\(f^{\mathrm{op}} \circ g^{\mathrm{op}} = (g \circ f)^{\mathrm{op}}\\).

La categoría opuesta produce el **principio de dualidad**: toda definición y todo teorema de la teoría tiene un dual, obtenido al invertir todas las flechas. Si un enunciado vale en toda categoría, su dual también vale en toda categoría, porque es el enunciado original aplicado a \\(\mathcal{C}^{\mathrm{op}}\\). Cada resultado del libro, por lo tanto, se demuestra una sola vez y viene acompañado de su dual sin costo.

Otras construcciones útiles:

- **Producto de categorías.** \\(\mathcal{C} \times \mathcal{D}\\) tiene por objetos los pares \\((C, D)\\) y por flechas los pares \\((f, g)\\), con composición componente a componente.
- **Categoría rebanada.** Dado un objeto \\(X\\) de \\(\mathcal{C}\\), la categoría \\(\mathcal{C}/X\\) tiene por objetos las flechas \\(p\colon A \to X\\). Una flecha de \\(p\colon A \to X\\) a \\(q\colon B \to X\\) es una flecha \\(h\colon A \to B\\) tal que \\(q \circ h = p\\).

La categoría rebanada \\(\mathbf{Set}/I\\) merece atención. Un objeto es una función \\(p\colon A \to I\\), es decir, una **familia de conjuntos indexada por \\(I\\)**: las fibras \\(A\_i = p^{-1}(i)\\). Una flecha es una familia de funciones \\(A\_i \to B\_i\\), una para cada índice. Las familias indexadas, conocidas desde la teoría de conjuntos, son una categoría rebanada.

---

## 5. Flechas especiales

### A. Isomorfismos

> **Definición 1.10 (Isomorfismo).**
> Una flecha \\(f\colon A \to B\\) es un **isomorfismo** si existe \\(g\colon B \to A\\) tal que \\(g \circ f = 1\_A\\) y \\(f \circ g = 1\_B\\). En ese caso, \\(A\\) y \\(B\\) son **isomorfos**, y se escribe \\(A \cong B\\).

> **Proposición 1.11.**
> Si \\(f\\) es un isomorfismo, la flecha \\(g\\) de la Definición 1.10 es única. Se llama la **inversa** de \\(f\\) y se denota \\(f^{-1}\\).
>
> *Demostración.* Si \\(g\\) y \\(g'\\) son inversas de \\(f\\), entonces
>
> \\[
> g = g \circ 1\_B = g \circ (f \circ g') = (g \circ f) \circ g' = 1\_A \circ g' = g'.
> \\]
>
> \\(\blacksquare\\)

Es la misma demostración de la unicidad del inverso en un grupo. Ahora funciona en cualquier categoría porque solo usa la asociatividad y la unidad.

Los isomorfismos de cada categoría son los "isomorfismos de siempre": biyecciones en \\(\mathbf{Set}\\), isomorfismos de grupos en \\(\mathbf{Grp}\\), homeomorfismos en \\(\mathbf{Top}\\). La diferencia es instructiva: en \\(\mathbf{Grp}\\), todo homomorfismo biyectivo es un isomorfismo, pero en \\(\mathbf{Top}\\) no. La identidad de \\(\mathbb{R}\\) con la topología discreta en \\(\mathbb{R}\\) con la usual es continua y biyectiva, pero su inversa no es continua. **Ser isomorfismo depende de la categoría, no solo de la función.**

### B. Monomorfismos y epimorfismos

La inyectividad y la sobreyectividad hablan de elementos. Para trasladarlas a cualquier categoría hay que expresarlas solo con flechas.

> **Definición 1.12 (Monomorfismo y epimorfismo).**
> Una flecha \\(f\colon A \to B\\) es un **monomorfismo** si para todo par de flechas \\(g, h\colon X \to A\\),
>
> \\[
> f \circ g = f \circ h \ \Longrightarrow \ g = h.
> \\]
>
> Dualmente, \\(f\\) es un **epimorfismo** si para todo par \\(g, h\colon B \to Y\\), la igualdad \\(g \circ f = h \circ f\\) implica \\(g = h\\).

Un monomorfismo es una flecha que se puede **cancelar por la izquierda**; un epimorfismo, una que se puede cancelar por la derecha. Por el principio de dualidad, un epimorfismo de \\(\mathcal{C}\\) es un monomorfismo de \\(\mathcal{C}^{\mathrm{op}}\\).

> **Proposición 1.13.**
> En \\(\mathbf{Set}\\), los monomorfismos son las funciones inyectivas y los epimorfismos son las funciones sobreyectivas.
>
> *Demostración (monomorfismos).* Si \\(f\\) es inyectiva y \\(f \circ g = f \circ h\\), entonces \\(f(g(x)) = f(h(x))\\) para todo \\(x\\), y la inyectividad da \\(g(x) = h(x)\\). Recíprocamente, supongamos que \\(f\\) es un monomorfismo y que \\(f(a) = f(a')\\). Sea \\(X = \\{\star\\}\\) un conjunto con un elemento y sean \\(g, h\colon X \to A\\) dadas por \\(g(\star) = a\\) y \\(h(\star) = a'\\). Entonces \\(f \circ g = f \circ h\\), luego \\(g = h\\) y \\(a = a'\\).
>
> *Demostración (epimorfismos).* Si \\(f\\) es sobreyectiva y \\(g \circ f = h \circ f\\), todo \\(b \in B\\) es de la forma \\(f(a)\\), y \\(g(b) = g(f(a)) = h(f(a)) = h(b)\\). Recíprocamente, si \\(f\\) no es sobreyectiva, sea \\(b\_0 \notin f(A)\\). Las funciones \\(g, h\colon B \to \\{0,1\\}\\), con \\(g\\) constante igual a \\(0\\) y \\(h\\) igual a \\(0\\) salvo en \\(b\_0\\), donde vale \\(1\\), cumplen \\(g \circ f = h \circ f\\) y \\(g \neq h\\). Luego \\(f\\) no es epimorfismo. \\(\blacksquare\\)

Observe el papel del conjunto con un elemento en la primera parte: **los elementos de \\(A\\) son las flechas \\(\\{\star\\} \to A\\)**. Esta observación es el germen del Capítulo 5.

En otras categorías, los epimorfismos pueden no ser sobreyectivos.

> **Ejemplo 1.14 (Un epimorfismo no sobreyectivo).**
> En \\(\mathbf{Ring}\\), la inclusión \\(i\colon \mathbb{Z} \to \mathbb{Q}\\) es un epimorfismo. Sean \\(f, g\colon \mathbb{Q} \to R\\) homomorfismos de anillos que coinciden en \\(\mathbb{Z}\\). Para \\(n \neq 0\\),
>
> \\[
> f(1/n) = f(1/n)\\, g(n)\\, g(1/n) = f(1/n)\\, f(n)\\, g(1/n) = f(1)\\, g(1/n) = g(1/n),
> \\]
>
> donde se usó \\(g(n) g(1/n) = g(1) = 1\\) y \\(g(n) = f(n)\\). Como \\(f(m/n) = f(m) f(1/n)\\), se sigue \\(f = g\\). Sin embargo, \\(i\\) no es sobreyectiva, y tampoco es un isomorfismo.

El Ejemplo 1.14 muestra además que **monomorfismo y epimorfismo a la vez no implica isomorfismo**: \\(i\\) es inyectiva, luego monomorfismo, y es epimorfismo, pero no tiene inversa.

### C. Secciones y retracciones

> **Definición 1.15 (Sección y retracción).**
> Si \\(r \circ s = 1\_A\\) con \\(s\colon A \to B\\) y \\(r\colon B \to A\\), se dice que \\(s\\) es una **sección** (o monomorfismo escindido) y que \\(r\\) es una **retracción** (o epimorfismo escindido).

> **Proposición 1.16.**
> Toda sección es un monomorfismo y toda retracción es un epimorfismo. Una flecha es un isomorfismo si y solo si es a la vez monomorfismo y retracción.
>
> *Demostración.* Si \\(r \circ s = 1\_A\\) y \\(s \circ g = s \circ h\\), al componer con \\(r\\) por la izquierda se obtiene \\(g = h\\). El caso de la retracción es dual. Para la segunda afirmación, si \\(f\\) es monomorfismo y existe \\(s\\) con \\(f \circ s = 1\_B\\), entonces \\(f \circ (s \circ f) = (f \circ s) \circ f = f = f \circ 1\_A\\), y al cancelar \\(f\\) queda \\(s \circ f = 1\_A\\). El recíproco es inmediato. \\(\blacksquare\\)

En \\(\mathbf{Set}\\), toda función sobreyectiva es una retracción, y esta afirmación es equivalente al **axioma de elección**: escoger una sección es escoger un elemento en cada fibra.

---

## 🔑 Lo que cristalizó

- Una **categoría** es una colección de objetos y flechas con composición asociativa e identidades.
- Áreas enteras son categorías (\\(\mathbf{Set}\\), \\(\mathbf{Grp}\\), \\(\mathbf{Top}\\)), pero también lo son objetos individuales: un orden parcial es una categoría con a lo más una flecha entre objetos; un monoide, una categoría con un objeto.
- Las nociones de **isomorfismo, monomorfismo y epimorfismo** se definen solo con flechas, y su comportamiento depende de la categoría.
- El **principio de dualidad** duplica cada resultado sin costo adicional.

## 🌉 Puente

Hasta aquí se estudió una categoría a la vez. Pero las categorías se relacionan entre sí: a cada grupo le corresponde su conjunto subyacente; a cada espacio, su grupo fundamental. El Capítulo 2 define las flechas entre categorías.
