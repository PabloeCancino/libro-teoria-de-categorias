# 7. Existencia y preservación de límites

## Hilo conductor

El Capítulo 6 calculó límites caso por caso. Este capítulo da dos resultados generales. El primero es una **receta**: si una categoría tiene productos y ecualizadores, tiene todos los límites, y la receta dice cómo construirlos. El segundo es un **criterio de preservación**: los funtores hom preservan límites, y por eso cualquier funtor representable también los preserva. Con este criterio se responde una pregunta que el lector tal vez se haya hecho: ¿por qué el producto de dos grupos tiene como conjunto subyacente el producto cartesiano, mientras que su coproducto no tiene como conjunto subyacente la unión disjunta?

## Ideas previas que se cristalizan

- Una sucesión compatible de residuos módulo \\(p^n\\) es un elemento del producto \\(\prod\_n \mathbb{Z}/p^n\\) que satisface ecuaciones.
- El conjunto subyacente de un producto de grupos es el producto de los conjuntos subyacentes.
- El conjunto subyacente de un producto libre de grupos **no** es la unión disjunta.
- Una función que sale de un conjunto cociente es una función que respeta la relación.

---

## 1. Los límites se construyen con productos y ecualizadores

> **Definición 7.1 (Completa).**
> Una categoría es **completa** si todo diagrama \\(D\colon \mathcal{J} \to \mathcal{C}\\) con \\(\mathcal{J}\\) pequeña tiene límite, y **cocompleta** si todo diagrama así tiene colímite.

> **Teorema 7.2 (Límites a partir de productos y ecualizadores).**
> Si \\(\mathcal{C}\\) tiene todos los productos pequeños y todos los ecualizadores, entonces es completa.
>
> *Demostración.* Sea \\(D\colon \mathcal{J} \to \mathcal{C}\\). Se forman dos productos:
>
> \\[
> P = \prod\_{j \in \mathrm{Ob}(\mathcal{J})} D(j), \qquad Q = \prod\_{u\colon j \to k} D(k),
> \\]
>
> el segundo indexado por todas las flechas de \\(\mathcal{J}\\). Se definen \\(s, t\colon P \rightrightarrows Q\\) por sus componentes: para cada flecha \\(u\colon j \to k\\),
>
> \\[
> \pi\_u \circ s = D(u) \circ \pi\_j, \qquad \pi\_u \circ t = \pi\_k.
> \\]
>
> Sea \\(e\colon L \to P\\) el ecualizador de \\(s\\) y \\(t\\), y sea \\(\lambda\_j = \pi\_j \circ e\\). Entonces \\((L, (\lambda\_j))\\) es un cono, porque para cada \\(u\colon j \to k\\):
>
> \\[
> D(u) \circ \lambda\_j = \pi\_u \circ s \circ e = \pi\_u \circ t \circ e = \lambda\_k.
> \\]
>
> Es universal: si \\((X, (\mu\_j))\\) es un cono, la flecha \\(\langle \mu\_j \rangle\colon X \to P\\) cumple \\(s \circ \langle \mu\_j \rangle = t \circ \langle \mu\_j \rangle\\), porque sus componentes son \\(D(u) \circ \mu\_j\\) y \\(\mu\_k\\), que son iguales por ser un cono. Luego se factoriza de manera única por \\(e\\). Para la unicidad: si \\(h, h'\colon X \to L\\) factorizan el cono, entonces \\(\pi\_j \circ e \circ h = \pi\_j \circ e \circ h'\\) para todo \\(j\\); como las proyecciones del producto separan flechas, \\(e \circ h = e \circ h'\\), y como \\(e\\) es monomorfismo (Proposición 6.5), \\(h = h'\\). \\(\blacksquare\\)

La prueba traduce la intuición conjuntista: **un límite es el subconjunto del producto formado por las familias compatibles**. En \\(\mathbf{Set}\\),

\\[
\lim D = \\{(x\_j)\_j \in \textstyle\prod\_j D(j) \mid D(u)(x\_j) = x\_k \text{ para toda } u\colon j \to k\\}.
\\]

> **Corolario 7.3.**
> \\(\mathbf{Set}\\), \\(\mathbf{Grp}\\), \\(\mathbf{Ab}\\), \\(\mathbf{Ring}\\), \\(\mathbf{Vect}\_k\\) y \\(\mathbf{Top}\\) son completas. Por dualidad, una categoría con coproductos y coecualizadores es cocompleta, y todas las anteriores también lo son.

Hay versiones finitas: una categoría con objeto terminal y productos fibrados tiene todos los límites finitos, porque los productos binarios y los ecualizadores se construyen con productos fibrados (Ejercicio 8 de la Parte III).

> **Ejemplo 7.4 (Categorías a las que les faltan límites).**
>
> - **Campos:** no hay producto de \\(\mathbb{F}\_2\\) y \\(\mathbb{F}\_3\\), porque no hay ningún campo con homomorfismos hacia ambos (tendría que tener característica 2 y 3 a la vez).
> - **Conjuntos finitos:** tienen límites finitos, pero no todos los productos infinitos (por ejemplo, el producto de una cantidad numerable de copias de \\(\\{0, 1\\}\\)).
> - **Un orden parcial:** es completo como categoría si y solo si todo subconjunto tiene ínfimo, es decir, si es un **retículo completo**.

---

## 2. Preservación de límites

> **Definición 7.5 (Preservar límites).**
> Un funtor \\(F\colon \mathcal{C} \to \mathcal{D}\\) **preserva** el límite de \\(D\\) si, para todo cono límite \\((L, (\pi\_j))\\) de \\(D\\), el cono \\((FL, (F\pi\_j))\\) es un límite de \\(F \circ D\\). Se dice que \\(F\\) **preserva límites** si preserva todos los límites que existen en \\(\mathcal{C}\\).

> **Proposición 7.6 (Los funtores hom preservan límites).**
> Para todo objeto \\(X\\) de \\(\mathcal{C}\\), el funtor \\(\mathcal{C}(X, -)\colon \mathcal{C} \to \mathbf{Set}\\) preserva límites:
>
> \\[
> \mathcal{C}(X, \lim D) \cong \lim\_j \mathcal{C}(X, D(j)).
> \\]
>
> *Demostración.* Por la fórmula de los límites en \\(\mathbf{Set}\\), el lado derecho es el conjunto de familias \\((f\_j\colon X \to D(j))\_j\\) con \\(D(u) \circ f\_j = f\_k\\). Es decir, el conjunto de conos sobre \\(D\\) con vértice \\(X\\). La biyección con \\(\mathcal{C}(X, \lim D)\\) es **la definición misma de límite**. \\(\blacksquare\\)

> **Corolario 7.7.**
> Todo funtor representable \\(F \cong \mathcal{C}(A, -)\\) preserva límites.

Ahora se responde la pregunta inicial.

> **Ejemplo 7.8 (Por qué el olvidadizo de grupos preserva límites).**
> El funtor olvidadizo \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) es representable: \\(U \cong \mathbf{Grp}(\mathbb{Z}, -)\\) (Ejemplo 5.2). Por el Corolario 7.7, preserva todos los límites. Por eso **el conjunto subyacente de un producto, de un ecualizador o de un límite inverso de grupos se calcula como en \\(\mathbf{Set}\\)**. El mismo argumento vale para \\(\mathbf{Ring}\\) (representado por \\(\mathbb{Z}[x]\\)) y para \\(\mathbf{Top}\\) (representado por el punto).
>
> En cambio, \\(U\\) **no** preserva colímites. El coproducto \\(\mathbb{Z} \ast \mathbb{Z}\\) no es la unión disjunta de dos copias de \\(\mathbb{Z}\\): contiene, por ejemplo, la palabra \\(aba^{-1}b^{-1}\\), que no está en ninguna de las dos copias. Tampoco preserva el objeto inicial: el grupo trivial tiene un elemento y \\(\emptyset\\) ninguno.

El funtor hom contravariante tiene un comportamiento dual: **envía colímites en límites**,

\\[
\mathcal{C}(\mathrm{colim}\\, D, X) \cong \lim\_j \mathcal{C}(D(j), X).
\\]

Ejemplo: una función que sale de un conjunto cociente \\(B/\sim\\) es lo mismo que una función que sale de \\(B\\) y toma el mismo valor en elementos relacionados.

---

## 3. Crear límites

Hay una propiedad más fuerte que preservar.

> **Definición 7.9 (Crear límites).**
> \\(F\colon \mathcal{C} \to \mathcal{D}\\) **crea límites** si, para todo diagrama \\(D\\) en \\(\mathcal{C}\\) y todo cono límite \\((M, (\mu\_j))\\) de \\(F \circ D\\), existe un único cono \\((L, (\lambda\_j))\\) sobre \\(D\\) con \\(FL = M\\) y \\(F\lambda\_j = \mu\_j\\), y además ese cono es un límite de \\(D\\).

El olvidadizo \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) crea límites: dado el límite del diagrama de conjuntos subyacentes, existe una única estructura de grupo sobre él que hace de las proyecciones homomorfismos, y con esa estructura es el límite en \\(\mathbf{Grp}\\). Esto explica, de manera precisa, el procedimiento de siempre: **para calcular un límite de grupos, se calcula en \\(\mathbf{Set}\\) y se le da la operación componente a componente**. El olvidadizo \\(U\colon \mathbf{Top} \to \mathbf{Set}\\) preserva límites pero no los crea: sobre el mismo conjunto hay muchas topologías posibles, y solo una de ellas da el límite.

---

## 4. Límites en categorías de funtores

> **Proposición 7.10 (Los límites de funtores se calculan punto por punto).**
> Si \\(\mathcal{D}\\) es completa, también lo es \\([\mathcal{C}, \mathcal{D}]\\) para \\(\mathcal{C}\\) pequeña. El límite de un diagrama de funtores \\(j \mapsto F\_j\\) es el funtor \\(C \mapsto \lim\_j F\_j(C)\\).
>
> *Idea de la demostración.* Se define \\(L(C) = \lim\_j F\_j(C)\\). Una flecha \\(f\colon C \to C'\\) induce \\(L(f)\\) por la propiedad universal del límite en \\(C'\\). Las proyecciones son naturales por construcción y la universalidad se verifica objeto por objeto. \\(\blacksquare\\)

> **Corolario 7.11.**
> Toda categoría de prehaces \\([\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]\\) es completa y cocompleta. En particular, la categoría de \\(G\\)-conjuntos lo es, y sus límites y colímites se calculan sobre los conjuntos subyacentes.

Dos resultados más se enuncian sin prueba y se usarán solo como referencia:

- **Los límites conmutan con los límites:** si \\(D\colon \mathcal{I} \times \mathcal{J} \to \mathcal{C}\\), entonces \\(\lim\_i \lim\_j D(i,j) \cong \lim\_j \lim\_i D(i,j)\\).
- **Los colímites filtrados conmutan con los límites finitos en \\(\mathbf{Set}\\).** Es un resultado delicado, central en álgebra y geometría; véase Riehl, Capítulo 3.

> **📝 Para pensar.** Antes de este capítulo, ¿sabías **por qué** el producto de grupos "se hace en conjuntos" y el coproducto no? ¿Era un hecho memorizado o un hecho explicado? Busca otro funtor olvidadizo que no preserve algún límite. *(Sugerencia: la inclusión de los grupos abelianos de torsión en \\(\mathbf{Ab}\\), aplicada a un producto infinito como \\(\prod\_n \mathbb{Z}/n\\).)*

---

## 🔑 Lo que cristalizó

- **Productos más ecualizadores dan todos los límites**; la receta es "familias compatibles dentro del producto".
- Los **funtores hom** preservan límites por definición; por eso los representables los preservan.
- El olvidadizo de grupos preserva límites porque está representado por \\(\mathbb{Z}\\); no preserva coproductos.
- **Crear** límites es más fuerte que preservarlos y explica por qué los límites de estructuras algebraicas se calculan en conjuntos.
- En categorías de funtores, los límites y colímites se calculan **punto por punto**.

## 🌉 Puente

El olvidadizo \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) preserva límites, y además tiene un "compañero", el grupo libre, que va en sentido contrario. ¿Es casualidad? El Capítulo 8 introduce la relación precisa entre ambos, la **adjunción**, y el Capítulo 9 demuestra que todo funtor con un compañero a la izquierda preserva límites.
