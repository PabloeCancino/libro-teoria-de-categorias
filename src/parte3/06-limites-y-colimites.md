# 6. Diagramas, conos, límites y colímites

## Hilo conductor

El núcleo de un homomorfismo, el conjunto de soluciones de una ecuación \\(f(x) = g(x)\\), la imagen inversa de un subconjunto, la intersección de dos subconjuntos y los enteros \\(p\\)-ádicos parecen construcciones sin relación. Este capítulo muestra que todas son **límites**: objetos universales sobre un diagrama. Del lado dual, el conjunto cociente, el grupo cociente, la topología cociente, el pegado de espacios y la unión de una cadena creciente son **colímites**. El producto del Capítulo 4 es el caso más sencillo de límite; ahora se generaliza a diagramas de cualquier forma.

## Ideas previas que se cristalizan

- El núcleo \\(\ker f = \\{g \in G \mid f(g) = e\\}\\) y el ecualizador \\(\\{x \mid f(x) = g(x)\\}\\).
- La imagen inversa \\(f^{-1}(B')\\) de un subconjunto y la intersección \\(B' \cap B''\\).
- Los enteros \\(p\\)-ádicos como sucesiones compatibles de residuos módulo \\(p^n\\).
- El conjunto cociente \\(A/\sim\\), el grupo cociente \\(G/N\\) y la topología cociente.
- La esfera \\(S^2\\) obtenida al pegar dos discos por su frontera.

---

## 1. Diagramas y conos

> **Definición 6.1 (Diagrama).**
> Sea \\(\mathcal{J}\\) una categoría pequeña. Un **diagrama de forma \\(\mathcal{J}\\)** en \\(\mathcal{C}\\) es un funtor \\(D\colon \mathcal{J} \to \mathcal{C}\\).

La categoría \\(\mathcal{J}\\) es el "molde": dice cuántos objetos hay y qué flechas los conectan. Las formas que más se usan son:

| Forma \\(\mathcal{J}\\) | Dibujo | Límite | Colímite |
| :--- | :--- | :--- | :--- |
| Discreta con dos objetos | \\(\bullet \quad \bullet\\) | Producto | Coproducto |
| Par paralelo | \\(\bullet \rightrightarrows \bullet\\) | Ecualizador | Coecualizador |
| Coespán | \\(\bullet \to \bullet \leftarrow \bullet\\) | Producto fibrado (*pullback*) | Trivial: el objeto central |
| Espán | \\(\bullet \leftarrow \bullet \to \bullet\\) | Trivial: el objeto central | Suma amalgamada (*pushout*) |
| Cadena \\(\omega^{\mathrm{op}}\\) | \\(\cdots \to \bullet \to \bullet \to \bullet\\) | Límite inverso | Trivial: el último objeto |
| Cadena \\(\omega\\) | \\(\bullet \to \bullet \to \bullet \to \cdots\\) | Trivial: el primer objeto | Límite directo |
| Vacía | (ninguno) | Objeto terminal | Objeto inicial |

> **Definición 6.2 (Cono y límite).**
> Un **cono** sobre \\(D\colon \mathcal{J} \to \mathcal{C}\\) es un objeto \\(X\\) (el **vértice**) con flechas \\(\lambda\_j\colon X \to D(j)\\), una por cada objeto \\(j\\) de \\(\mathcal{J}\\), tales que para toda flecha \\(u\colon j \to k\\) de \\(\mathcal{J}\\) se cumple
>
> \\[
> D(u) \circ \lambda\_j = \lambda\_k.
> \\]
>
> Es decir, para cada flecha \\(u\\) del molde, el triángulo
>
> \\[
> \begin{array}{ccc}
> & X & \\\\
> {\scriptstyle \lambda\_j} \swarrow & & \searrow {\scriptstyle \lambda\_k} \\\\
> D(j) & \xrightarrow[\ D(u)\ ]{} & D(k)
> \end{array}
> \\]
>
> conmuta. El vértice \\(X\\) "mira" todo el diagrama de manera compatible.
>
> Un **límite** de \\(D\\) es un cono \\((L, (\pi\_j))\\) universal: para todo cono \\((X, (\lambda\_j))\\) existe una única flecha \\(h\colon X \to L\\) con \\(\pi\_j \circ h = \lambda\_j\\) para todo \\(j\\). Se escribe \\(L = \lim D\\).

Como con el producto, la propiedad universal se condensa en una biyección natural en \\(X\\):

\\[
\mathcal{C}(X, \lim D) \cong \mathrm{Cono}(X, D).
\\]

Es decir, **el límite es el objeto que representa al funtor de conos** (Capítulo 5), y por eso es único salvo isomorfismo único. Si se denota \\(\Delta X\colon \mathcal{J} \to \mathcal{C}\\) el diagrama constante con valor \\(X\\), un cono con vértice \\(X\\) es exactamente una transformación natural \\(\Delta X \Rightarrow D\\). Esta reformulación se usará en los Ejercicios 5 y 6 de la Parte IV.

---

## 2. Ecualizadores

> **Definición 6.3 (Ecualizador).**
> El **ecualizador** de dos flechas \\(f, g\colon A \rightrightarrows B\\) es una flecha \\(e\colon E \to A\\) con \\(f \circ e = g \circ e\\), universal: toda \\(h\colon X \to A\\) con \\(f \circ h = g \circ h\\) se factoriza de manera única como \\(h = e \circ \bar{h}\\).

> **Ejemplo 6.4.**
>
> - **\\(\mathbf{Set}\\):** \\(E = \\{a \in A \mid f(a) = g(a)\\}\\) con la inclusión. **El conjunto solución de una ecuación es un ecualizador.**
> - **\\(\mathbf{Grp}\\):** el mismo conjunto, que es un subgrupo. El **núcleo** de \\(f\colon G \to H\\) es el ecualizador de \\(f\\) y del homomorfismo trivial.
> - **\\(\mathbf{Top}\\):** el mismo conjunto con la **topología de subespacio**. Una vez más, la propiedad universal elige la topología.
> - **\\(\mathbf{Vect}\_k\\):** el núcleo de \\(f - g\\).

> **Proposición 6.5.**
> Todo ecualizador es un monomorfismo.
>
> *Demostración.* Si \\(e \circ x = e \circ y\\), la flecha \\(h = e \circ x\\) iguala a \\(f\\) y \\(g\\), y tanto \\(x\\) como \\(y\\) la factorizan por \\(e\\). Por la unicidad de la factorización, \\(x = y\\). \\(\blacksquare\\)

---

## 3. Productos fibrados

> **Definición 6.6 (Producto fibrado).**
> El **producto fibrado** de \\(f\colon A \to C\\) y \\(g\colon B \to C\\) es un objeto \\(P = A \times\_C B\\) con flechas \\(p\_1\colon P \to A\\), \\(p\_2\colon P \to B\\) tales que el cuadrado
>
> \\[
> \require{AMScd}
> \begin{CD}
> P @>{p\_2}>> B \\\\
> @V{p\_1}VV @VV{g}V \\\\
> A @>>{f}> C
> \end{CD}
> \\]
>
> conmuta, y que es universal entre los cuadrados conmutativos con esos lados \\(f\\) y \\(g\\).

> **Ejemplo 6.7 (Productos fibrados en \\(\mathbf{Set}\\)).**
> \\(A \times\_C B = \\{(a, b) \in A \times B \mid f(a) = g(b)\\}\\). Tres casos particulares muestran su alcance:
>
> - **Imagen inversa.** Si \\(g\\) es la inclusión de \\(C' \subseteq C\\), el producto fibrado es \\(f^{-1}(C')\\).
> - **Intersección.** Si \\(f\\) y \\(g\\) son inclusiones de subconjuntos de \\(C\\), el producto fibrado es \\(A \cap B\\).
> - **Fibra.** Si \\(B = \\{\star\\}\\) y \\(g(\star) = c\\), el producto fibrado es la fibra \\(f^{-1}(c)\\).

El producto fibrado es la **construcción de "cambio de base"** en geometría y topología: el pullback de un haz o de un recubrimiento a lo largo de una función continua.

---

## 4. Límites inversos

> **Ejemplo 6.8 (Los enteros \\(p\\)-ádicos).**
> Sea \\(p\\) primo y considérese el diagrama de anillos
>
> \\[
> \cdots \to \mathbb{Z}/p^3 \to \mathbb{Z}/p^2 \to \mathbb{Z}/p
> \\]
>
> con las reducciones como flechas. Su límite es
>
> \\[
> \mathbb{Z}\_p = \lim\_n \mathbb{Z}/p^n = \\{(a\_n)\_{n \ge 1} \mid a\_n \in \mathbb{Z}/p^n, \ a\_{n+1} \equiv a\_n \ (\mathrm{mod}\ p^n)\\},
> \\]
>
> el anillo de los **enteros \\(p\\)-ádicos**. Del mismo modo, el anillo de series formales es \\(k[[x]] = \lim\_n k[x]/(x^n)\\).

---

## 5. Colímites

Al invertir las flechas se obtienen los **cocones** (flechas \\(D(j) \to X\\) compatibles) y los **colímites**: cocones iniciales. Se escribe \\(\mathrm{colim}\\, D\\).

> **Ejemplo 6.9 (Coecualizadores: los cocientes).**
>
> - **\\(\mathbf{Set}\\):** el coecualizador de \\(f, g\colon A \rightrightarrows B\\) es \\(B/\sim\\), donde \\(\sim\\) es la **relación de equivalencia generada** por \\(f(a) \sim g(a)\\). Todo conjunto cociente por una relación de equivalencia \\(R \subseteq B \times B\\) es el coecualizador de las dos proyecciones \\(R \rightrightarrows B\\).
> - **\\(\mathbf{Grp}\\):** el cociente de \\(B\\) por el **subgrupo normal generado** por los elementos \\(f(a) g(a)^{-1}\\). Las presentaciones por generadores y relaciones son coecualizadores.
> - **\\(\mathbf{Top}\\):** el conjunto cociente con la **topología cociente**.

> **Ejemplo 6.10 (Sumas amalgamadas: el pegado).**
> La suma amalgamada (*pushout*) de \\(f\colon C \to A\\) y \\(g\colon C \to B\\) en \\(\mathbf{Set}\\) es la unión disjunta \\(A \sqcup B\\) cociente por \\(f(c) \sim g(c)\\). En \\(\mathbf{Top}\\):
>
> - pegar dos discos \\(D^2\\) a lo largo de su frontera \\(S^1\\) da la esfera \\(S^2\\);
> - pegar una celda \\(D^n\\) a un espacio \\(X\\) a lo largo de una función \\(S^{n-1} \to X\\) es la construcción básica de los **complejos CW**.
>
> En \\(\mathbf{Grp}\\), la suma amalgamada es el **producto libre amalgamado** \\(A \ast\_C B\\). El teorema de Seifert–van Kampen dice que, bajo sus hipótesis, el grupo fundamental **envía la suma amalgamada de espacios a la suma amalgamada de grupos**.

> **Ejemplo 6.11 (Límites directos).**
>
> - La unión de una cadena creciente de conjuntos \\(A\_0 \subseteq A\_1 \subseteq \cdots\\) es su colímite.
> - El colímite de \\(\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z} \xrightarrow{\times 3} \mathbb{Z} \xrightarrow{\times 4} \cdots\\) en \\(\mathbf{Ab}\\) es isomorfo a \\(\mathbb{Q}\\): la \\(n\\)-ésima copia de \\(\mathbb{Z}\\) corresponde a las fracciones con denominador \\(n!\\).
> - El grupo de Prüfer \\(\mathbb{Z}(p^\infty)\\) es el colímite de \\(\mathbb{Z}/p \to \mathbb{Z}/p^2 \to \mathbb{Z}/p^3 \to \cdots\\), con las inclusiones \\(a \mapsto pa\\).

> **📝 Para pensar.** Los límites en \\(\mathbf{Set}\\) son subconjuntos de productos (se imponen ecuaciones); los colímites son cocientes de coproductos (se identifican elementos). ¿Cuál de las dos operaciones te resulta más difícil de calcular a mano en \\(\mathbf{Grp}\\), y por qué? Piensa en la dificultad del problema de la palabra para grupos presentados por generadores y relaciones.

---

## 🔑 Lo que cristalizó

- Un **diagrama** es un funtor desde una categoría pequeña; un **cono** es una familia compatible de flechas hacia el diagrama.
- Un **límite** es un cono terminal; representa el funtor de conos. Productos, ecualizadores, núcleos, productos fibrados, imágenes inversas, intersecciones y enteros \\(p\\)-ádicos son límites.
- Un **colímite** es el dual. Coproductos, cocientes, presentaciones, pegados y uniones de cadenas son colímites.
- En las categorías de estructuras, la propiedad universal **elige** la estructura correcta: topología de subespacio, cociente o producto.

## 🌉 Puente

Quedan tres preguntas. ¿Cuándo existen todos los límites de una categoría? ¿Hay una receta para construirlos? ¿Qué funtores los preservan? El Capítulo 7 responde las tres, y la última prepara el terreno para las adjunciones.
