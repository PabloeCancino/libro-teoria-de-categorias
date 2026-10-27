# 3. Transformaciones naturales y equivalencias

## Hilo conductor

Todo espacio vectorial de dimensión finita \\(V\\) es isomorfo a su dual \\(V^{\ast}\\) y también a su doble dual \\(V^{\ast\ast}\\). Sin embargo, los matemáticos dicen que el segundo isomorfismo es "canónico" y el primero no: para construir \\(V \cong V^{\ast}\\) hay que elegir una base, mientras que \\(V \to V^{\ast\ast}\\), \\(v \mapsto (\varphi \mapsto \varphi(v))\\), no requiere elecciones. Samuel Eilenberg y Saunders Mac Lane se toparon con esa diferencia en su trabajo sobre extensiones de grupos y homología. En 1942 publicaron una nota, "Natural isomorphisms in group theory", que ya trataba los isomorfismos naturales, y en 1945 el artículo "General theory of natural equivalences", donde definieron en general categoría, funtor y transformación natural. La teoría de categorías nació, así, para dar sentido preciso a la palabra "natural". La noción que buscaban es la de **transformación natural**, el tema de este capítulo.

## Ideas previas que se cristalizan

- La evaluación \\(V \to V^{\ast\ast}\\) se define igual para todos los espacios a la vez.
- El cociente \\(G \to G/[G,G]\\) se define igual para todos los grupos a la vez.
- El determinante de una matriz con entradas en un anillo conmutativo se calcula con la misma fórmula en cualquier anillo.
- Un homomorfismo de \\(G\\)-conjuntos (función equivariante) conmuta con la acción.

---

## 1. La definición

> **Definición 3.1 (Transformación natural).**
> Sean \\(F, G\colon \mathcal{C} \to \mathcal{D}\\) funtores. Una **transformación natural** \\(\alpha\colon F \Rightarrow G\\) es una familia de flechas de \\(\mathcal{D}\\)
>
> \\[
> \alpha\_A\colon FA \to GA, \qquad A \in \mathrm{Ob}(\mathcal{C}),
> \\]
>
> llamadas **componentes**, tales que para toda flecha \\(f\colon A \to B\\) de \\(\mathcal{C}\\) el siguiente **cuadrado de naturalidad** conmuta:
>
> \\[
> \require{AMScd}
> \begin{CD}
> FA @>{\alpha\_A}>> GA \\\\
> @V{F(f)}VV @VV{G(f)}V \\\\
> FB @>>{\alpha\_B}> GB
> \end{CD}
> \\]
>
> Es decir, \\(G(f) \circ \alpha\_A = \alpha\_B \circ F(f)\\). Si cada componente es un isomorfismo, \\(\alpha\\) es un **isomorfismo natural** y se escribe \\(F \cong G\\).

La naturalidad dice que \\(\alpha\\) se define "de manera uniforme": transformar primero con \\(F(f)\\) y después aplicar \\(\alpha\\) da lo mismo que aplicar \\(\alpha\\) y después transformar con \\(G(f)\\). Una construcción que dependa de elecciones arbitrarias, como una base, típicamente rompe ese cuadrado.

---

## 2. Ejemplos

> **Ejemplo 3.2 (El doble dual).**
> Sea \\(\mathrm{ev}\_V\colon V \to V^{\ast\ast}\\) dada por \\(\mathrm{ev}\_V(v)(\varphi) = \varphi(v)\\). Para \\(T\colon V \to W\\) lineal, la naturalidad pide \\(T^{\ast\ast} \circ \mathrm{ev}\_V = \mathrm{ev}\_W \circ T\\). Al evaluar ambos lados en \\(v\\) y luego en \\(\psi \in W^{\ast}\\):
>
> \\[
> (T^{\ast\ast}(\mathrm{ev}\_V v))(\psi) = (\mathrm{ev}\_V v)(\psi \circ T) = \psi(Tv) = (\mathrm{ev}\_W(Tv))(\psi).
> \\]
>
> Luego \\(\mathrm{ev}\colon 1 \Rightarrow (-)^{\ast\ast}\\) es natural. En la subcategoría de espacios de dimensión finita es un isomorfismo natural.

En contraste, un "isomorfismo natural \\(V \cong V^{\ast}\\)" ni siquiera tiene sentido como transformación natural: el funtor identidad es covariante y el dual es contravariante, así que no hay un cuadrado que pedir. La teoría no solo distingue lo canónico de lo que no lo es: explica por qué la pregunta está mal planteada.

> **Ejemplo 3.3 (Abelianización).**
> Para cada grupo \\(G\\), sea \\(q\_G\colon G \to G^{\mathrm{ab}} = G/[G,G]\\) el cociente. Un homomorfismo \\(f\colon G \to H\\) envía conmutadores en conmutadores, así que induce \\(f^{\mathrm{ab}}\colon G^{\mathrm{ab}} \to H^{\mathrm{ab}}\\) con \\(f^{\mathrm{ab}} \circ q\_G = q\_H \circ f\\). Esta igualdad es el cuadrado de naturalidad: \\(q\\) es una transformación natural del funtor identidad de \\(\mathbf{Grp}\\) en el funtor de abelianización (seguido de la inclusión \\(\mathbf{Ab} \to \mathbf{Grp}\\)).

> **Ejemplo 3.4 (El determinante).**
> Sea \\(\mathbf{CRing}\\) la categoría de anillos conmutativos. Hay dos funtores \\(\mathbf{CRing} \to \mathbf{Grp}\\): \\(GL\_n\\), que envía \\(R\\) al grupo de matrices invertibles \\(n \times n\\) sobre \\(R\\), y \\((-)^{\times}\\), que envía \\(R\\) a su grupo de unidades. El determinante \\(\det\_R\colon GL\_n(R) \to R^{\times}\\) es un homomorfismo para cada \\(R\\). Si \\(\varphi\colon R \to S\\) es un homomorfismo de anillos, entonces \\(\det(\varphi(A)) = \varphi(\det A)\\), donde \\(\varphi(A)\\) aplica \\(\varphi\\) entrada por entrada. La razón es que el determinante es un polinomio con coeficientes enteros en las entradas. Así, \\(\det\colon GL\_n \Rightarrow (-)^{\times}\\) es natural.

> **Ejemplo 3.5 (Unitario y unión).**
> En \\(\mathbf{Set}\\), la función \\(\eta\_X\colon X \to \mathcal{P}(X)\\), \\(x \mapsto \\{x\\}\\), es natural de la identidad en \\(\mathcal{P}\\): para \\(f\colon X \to Y\\), \\(f(\\{x\\}) = \\{f(x)\\}\\). También es natural la unión \\(\mu\_X\colon \mathcal{P}(\mathcal{P}(X)) \to \mathcal{P}(X)\\), \\(\mathcal{S} \mapsto \bigcup \mathcal{S}\\). Estas dos transformaciones volverán en el Capítulo 10: son la **unidad** y la **multiplicación** de la mónada de conjunto potencia.

> **Ejemplo 3.6 (Funciones equivariantes).**
> Si \\(X, Y\colon \mathbf{B}G \to \mathbf{Set}\\) son \\(G\\)-conjuntos (Ejemplo 2.8), una transformación natural \\(\alpha\colon X \Rightarrow Y\\) tiene una sola componente \\(\alpha\_\star\\), y la naturalidad dice \\(\alpha\_\star(g \cdot x) = g \cdot \alpha\_\star(x)\\). Las transformaciones naturales entre \\(G\\)-conjuntos son las **funciones equivariantes**.

> **📝 Para pensar.** Busca un ejemplo de familia de funciones \\(\alpha\_X\colon X \to X\\), una para cada conjunto, que **no** sea natural. ¿Qué tienes que elegir para definirla? ¿Puedes demostrar que toda transformación natural del funtor identidad de \\(\mathbf{Set}\\) en sí mismo es la identidad?

---

## 3. Categorías de funtores

Las transformaciones naturales se componen componente por componente: si \\(\alpha\colon F \Rightarrow G\\) y \\(\beta\colon G \Rightarrow H\\), se define \\((\beta \cdot \alpha)\_A = \beta\_A \circ \alpha\_A\\). Al pegar los dos cuadrados de naturalidad se ve que el compuesto es natural. La identidad \\(1\_F\\) tiene componentes \\(1\_{FA}\\).

> **Definición 3.7 (Categoría de funtores).**
> Si \\(\mathcal{C}\\) es pequeña, la **categoría de funtores** \\([\mathcal{C}, \mathcal{D}]\\) tiene por objetos los funtores \\(\mathcal{C} \to \mathcal{D}\\) y por flechas las transformaciones naturales, con la composición recién descrita.

Varias categorías conocidas son categorías de funtores:

- \\([\mathbf{B}G, \mathbf{Set}]\\) es la categoría de \\(G\\)-conjuntos y funciones equivariantes.
- \\([\mathbf{B}G, \mathbf{Vect}\_k]\\) es la categoría de representaciones de \\(G\\).
- \\([\mathbf{2}, \mathcal{C}]\\) es la **categoría de flechas** de \\(\mathcal{C}\\): sus objetos son las flechas de \\(\mathcal{C}\\) y sus morfismos, los cuadrados conmutativos.
- La categoría de **prehaces** \\(\widehat{\mathcal{C}} = [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]\\), protagonista del Capítulo 5.

> **Proposición 3.8.**
> Una transformación natural \\(\alpha\colon F \Rightarrow G\\) es un isomorfismo en \\([\mathcal{C}, \mathcal{D}]\\) si y solo si cada componente \\(\alpha\_A\\) es un isomorfismo en \\(\mathcal{D}\\).
>
> *Demostración.* Si \\(\alpha\\) tiene inversa \\(\beta\\) en la categoría de funtores, entonces \\(\beta\_A \circ \alpha\_A = 1\\) y \\(\alpha\_A \circ \beta\_A = 1\\) componente por componente. Recíprocamente, si cada \\(\alpha\_A\\) es invertible, se define \\(\beta\_A = \alpha\_A^{-1}\\) y solo falta ver que \\(\beta\\) es natural. A partir de \\(G(f) \circ \alpha\_A = \alpha\_B \circ F(f)\\), se compone con \\(\alpha\_B^{-1}\\) por la izquierda y con \\(\alpha\_A^{-1}\\) por la derecha:
>
> \\[
> \alpha\_B^{-1} \circ G(f) = F(f) \circ \alpha\_A^{-1},
> \\]
>
> que es el cuadrado de naturalidad de \\(\beta\\). \\(\blacksquare\\)

### Composición con funtores

Hay una operación adicional que será indispensable para las mónadas. Si \\(\alpha\colon F \Rightarrow G\\) con \\(F, G\colon \mathcal{C} \to \mathcal{D}\\), y \\(H\colon \mathcal{D} \to \mathcal{E}\\), \\(K\colon \mathcal{B} \to \mathcal{C}\\) son funtores, se definen:

- \\(H\alpha\colon HF \Rightarrow HG\\), con componentes \\((H\alpha)\_A = H(\alpha\_A)\\);
- \\(\alpha K\colon FK \Rightarrow GK\\), con componentes \\((\alpha K)\_B = \alpha\_{KB}\\).

Estas operaciones se llaman **composición por un lado** (en inglés, *whiskering*). Con ellas se escribirán, en el Capítulo 10, expresiones como \\(T\eta\\) y \\(\eta T\\).

---

## 4. Equivalencia de categorías

¿Cuándo dos categorías son "la misma"? Pedir un isomorfismo de categorías (funtores mutuamente inversos) es demasiado estricto: obliga a que los objetos correspondan uno a uno, cuando en matemáticas los objetos isomorfos son intercambiables.

> **Definición 3.9 (Equivalencia).**
> Un funtor \\(F\colon \mathcal{C} \to \mathcal{D}\\) es una **equivalencia de categorías** si existen un funtor \\(G\colon \mathcal{D} \to \mathcal{C}\\) e isomorfismos naturales \\(G F \cong 1\_{\mathcal{C}}\\) y \\(F G \cong 1\_{\mathcal{D}}\\). Se escribe \\(\mathcal{C} \simeq \mathcal{D}\\).

> **Definición 3.10 (Esencialmente sobreyectivo).**
> \\(F\\) es **esencialmente sobreyectivo** si todo objeto \\(D\\) de \\(\mathcal{D}\\) es isomorfo a \\(FC\\) para algún \\(C\\).

> **Teorema 3.11.**
> Un funtor es una equivalencia si y solo si es plenamente fiel y esencialmente sobreyectivo.
>
> *Idea de la demostración.* La dirección "solo si" es directa. Para la otra, se elige, para cada \\(D\\), un objeto \\(GD\\) y un isomorfismo \\(\varepsilon\_D\colon F(GD) \to D\\). Esto usa el axioma de elección sobre la clase de objetos. Para \\(g\colon D \to D'\\), la flecha \\(\varepsilon\_{D'}^{-1} \circ g \circ \varepsilon\_D\colon FGD \to FGD'\\) proviene de una única flecha \\(G(g)\colon GD \to GD'\\), porque \\(F\\) es plenamente fiel. Se verifica que \\(G\\) es un funtor y que \\(\varepsilon\\) y el isomorfismo \\(1 \cong GF\\) obtenido son naturales. Los detalles están en Riehl, sección 1.5, y en Leinster, sección 1.3. \\(\blacksquare\\)

> **Ejemplo 3.12 (El álgebra lineal es el cálculo matricial).**
> Sea \\(\mathbf{FinVect}\_k\\) la categoría de espacios vectoriales de dimensión finita. El funtor \\(\mathbf{Mat}\_k \to \mathbf{FinVect}\_k\\) que envía \\(n\\) a \\(k^n\\) y cada matriz a la transformación lineal que define es plenamente fiel (las transformaciones \\(k^n \to k^m\\) son las matrices \\(m \times n\\)) y esencialmente sobreyectivo (todo espacio de dimensión \\(n\\) es isomorfo a \\(k^n\\)). Luego \\(\mathbf{Mat}\_k \simeq \mathbf{FinVect}\_k\\).
>
> La equivalencia inversa requiere **elegir una base** de cada espacio. Lo que el álgebra lineal elemental hace de manera implícita, escoger bases para trabajar con matrices, es exactamente la construcción del funtor inverso en el Teorema 3.11.

> **Ejemplo 3.13 (Grupoides conexos).**
> Si \\(X\\) es un espacio arco-conexo y \\(x\_0 \in X\\), la inclusión \\(\mathbf{B}\pi\_1(X, x\_0) \to \Pi\_1(X)\\) del grupo fundamental en el grupoide fundamental es una equivalencia. Es plenamente fiel por definición, y esencialmente sobreyectiva porque cualquier punto se conecta con \\(x\_0\\) por un camino. Esto explica por qué "el" grupo fundamental de un espacio arco-conexo no depende del punto base salvo isomorfismo, aunque ese isomorfismo no sea canónico.

> **📝 Para pensar.** \\(\mathbf{Mat}\_k\\) tiene un objeto por cada dimensión; \\(\mathbf{FinVect}\_k\\) tiene una cantidad enorme de objetos. Son equivalentes pero no isomorfas. ¿Qué propiedades de una categoría deberían conservarse bajo equivalencia? ¿Cuál de estas lo hace: "tiene exactamente un objeto de cada dimensión" o "todo monomorfismo es una sección"?

---

## 🔑 Lo que cristalizó

- Una **transformación natural** es una familia de flechas compatible con todos los morfismos. Precisa la idea informal de "construcción canónica".
- Funtores y transformaciones naturales forman **categorías de funtores**. Las acciones de grupo, las representaciones y los prehaces viven ahí.
- Un isomorfismo natural es una transformación natural con todas sus componentes invertibles.
- La noción correcta de "misma categoría" es la **equivalencia**: plenamente fiel y esencialmente sobreyectivo.

## 🌉 Puente

Con categorías, funtores y transformaciones naturales, el lenguaje está completo. La Parte II lo usa para responder una pregunta de fondo: ¿cómo se caracteriza un objeto solo por sus flechas, sin mirar sus elementos?
