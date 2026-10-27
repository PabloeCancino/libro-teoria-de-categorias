# Epílogo. Seudo-mónadas y dimensiones superiores

## Hilo conductor

El libro empezó con una plática sobre mónadas que terminaba en las **seudo-mónadas**, "versiones más recientes en categorías de dimensiones más altas". Este epílogo no demuestra teoremas: traza el mapa para que esa última parte de la plática sea legible, y señala por dónde continuar.

---

## 1. Flechas entre flechas: las 2-categorías

A lo largo del libro, \\(\mathbf{Cat}\\) tuvo tres niveles: categorías, funtores entre ellas y transformaciones naturales entre funtores. Las mónadas usaron los tres a la vez: un endofuntor \\(T\\) (nivel 1) con transformaciones \\(\eta\\) y \\(\mu\\) (nivel 2). Esa estructura de tres niveles tiene nombre.

> **Definición E.1 (2-categoría, en forma breve).**
> Una **2-categoría** tiene **objetos**, **1-celdas** entre objetos y **2-celdas** entre 1-celdas paralelas. Las 2-celdas se componen de dos maneras, **vertical** y **horizontal**, y ambas composiciones satisfacen una ley de intercambio. El ejemplo modelo es \\(\mathbf{Cat}\\), con las dos composiciones de transformaciones naturales del Capítulo 3.

Si la composición de 1-celdas solo es asociativa y unitaria **salvo 2-celdas invertibles coherentes**, se habla de una **bicategoría**. Una categoría monoidal es exactamente una bicategoría con un solo objeto: el pentágono del Capítulo 12 es la coherencia del asociador.

## 2. La teoría formal de mónadas

En 1972 Ross Street observó que la definición de mónada solo usa la estructura de 2-categoría de \\(\mathbf{Cat}\\). Por lo tanto tiene sentido en **cualquier** 2-categoría (o bicategoría) \\(\mathcal{K}\\): una mónada en \\(\mathcal{K}\\) es un objeto \\(A\\), una 1-celda \\(t\colon A \to A\\) y 2-celdas \\(\eta\colon 1 \Rightarrow t\\), \\(\mu\colon tt \Rightarrow t\\) con las leyes de siempre.

El ejemplo más sorprendente se debe a Bénabou (1967). En la bicategoría de **espanes** de conjuntos, una 1-celda de \\(A\\) en \\(A\\) es un diagrama \\(A \leftarrow M \rightarrow A\\). Una mónada en esa bicategoría es un conjunto \\(A\\) de "objetos", un conjunto \\(M\\) de "flechas" con dominio y codominio, una "identidad" para cada objeto y una "composición" asociativa. Es decir:

> **Una categoría pequeña es una mónada en la bicategoría de espanes.**

El concepto con el que empezó el libro, categoría, resulta ser un caso del concepto al que llega, mónada. Es un buen ejemplo del **potencial unificador** que anunciaba el resumen de la plática.

## 3. 2-mónadas y sus álgebras

Una **2-mónada** es una mónada sobre \\(\mathbf{Cat}\\) que respeta también las transformaciones naturales. Su teoría fue desarrollada por Blackwell, Kelly y Power (1989). La novedad está en las álgebras: además de las álgebras **estrictas**, con \\(a \circ T(a) = a \circ \mu\\), aparecen las **seudo-álgebras**, en las que esas ecuaciones se cumplen solo salvo isomorfismos coherentes, y las **álgebras laxas**, en las que basta una 2-celda en un sentido.

> **Ejemplo E.2 (Categorías monoidales como seudo-álgebras).**
> Sea \\(T\\) la 2-mónada en \\(\mathbf{Cat}\\) que envía una categoría \\(\mathcal{C}\\) a la categoría de listas finitas de sus objetos, \\(T\mathcal{C} = \coprod\_{n \ge 0} \mathcal{C}^n\\). Sus álgebras **estrictas** son las categorías monoidales **estrictas**. Sus **seudo-álgebras** son las categorías monoidales "no sesgadas", con un producto \\(n\\)-ario para cada \\(n\\); estas son equivalentes a las categorías monoidales **generales** del Capítulo 12.

El ejemplo explica el Capítulo 12 desde arriba: el asociador \\(\alpha\\) y los unitores son los isomorfismos que hacen de una categoría una seudo-álgebra, y el pentágono es su condición de coherencia. Así como la mónada de listas codifica la teoría de los monoides (Teorema 10.11), la 2-mónada de listas codifica la teoría de las categorías monoidales.

## 4. Seudo-mónadas

El último paso es debilitar **la propia mónada**: que las leyes de asociatividad y unidad de \\(\mu\\) y \\(\eta\\) se cumplan solo salvo modificaciones invertibles coherentes. El resultado es una **seudo-mónada**. Su teoría requiere un nivel más, el de las tricategorías o las categorías de Gray, y se desarrolló en la década de 1990. Entre los trabajos fundacionales están los del propio Francisco Marmolejo, sobre las leyes distributivas entre seudo-mónadas (1999) y sobre las doctrinas de tipo Kock–Zöberlein, y el trabajo de Stephen Lack sobre la coherencia de las seudo-mónadas (2000).

Un ejemplo guía: la construcción que envía una categoría pequeña a su categoría de prehaces, \\(\mathcal{C} \mapsto [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]\\), es la **cocompletación libre** de \\(\mathcal{C}\\) (el encaje de Yoneda del Capítulo 5 es su unidad). Se comporta como una seudo-mónada, con una salvedad de tamaño: la categoría de prehaces no es pequeña. Esa salvedad llevó a la noción de **seudo-mónada relativa** (Fiore, Gambino, Hyland y Winskel, 2018).

---

## 5. Guía para escuchar la plática

Con el libro terminado, la plática "Mónadas" del Dr. Francisco Marmolejo (IM-UNAM, 8 de octubre de 2026) se puede seguir en tres bloques:

| Bloque de la plática | Dónde se preparó | Qué escuchar |
| :--- | :--- | :--- |
| Orígenes a mediados del siglo XX | Capítulo 10, Sección 1 | Godement, Huber, Kleisli, Eilenberg–Moore |
| Ejemplos y categorías de álgebras | Capítulos 10 y 11 | Qué teorías codifica cada mónada; Kleisli frente a Eilenberg–Moore; monadicidad |
| Dimensiones superiores | Este epílogo | Seudo-álgebras, seudo-mónadas y la coherencia |

Tres preguntas para llevar a la plática:

1. ¿Qué ejemplos de mónadas elige el ponente para mostrar el "potencial unificador", y cuáles de ellos no están en este libro?
2. ¿En qué momento aparece la necesidad de debilitar las ecuaciones a isomorfismos? ¿Es por razones técnicas o porque los ejemplos naturales lo exigen?
3. ¿Qué gana una teoría de nudos o una teoría de modelos estadísticos al pasar a dimensión superior, si es que gana algo?

---

## 6. Por dónde continuar

- **Teoría de 2-categorías:** Johnson y Yau, *2-Dimensional Categories* (Oxford, 2021); Lack, "A 2-categories companion" (2010), [libre en arXiv](https://arxiv.org/abs/math/0702535).
- **Mónadas formales y seudo-mónadas:** Street, "The formal theory of monads" (1972); Lack, "A coherent approach to pseudomonads" (2000); Marmolejo, "Distributive laws for pseudomonads" (1999), [de acceso libre en TAC](https://www.maths.tcd.ie/EMIS/journals/TAC/volumes/1999/n5/5-05abs.html).
- **Categorías de dimensión infinita:** Riehl y Verity, *Elements of ∞-Category Theory* (Cambridge, 2022), con [versión libre de la autora](https://math.jhu.edu/~eriehl/elements.pdf).
- **Categorías trenzadas e invariantes cuánticos:** Kassel, *Quantum Groups* (Springer, 1995); Turaev, *Quantum Invariants of Knots and 3-Manifolds* (De Gruyter).
- **Probabilidad categórica:** Fritz, "A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics" (2020), [libre en arXiv](https://arxiv.org/abs/1908.07021).

Las referencias completas y comentadas están en el [Apéndice D](../apendices/d-bibliografia.md).
