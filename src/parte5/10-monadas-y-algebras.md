# 10. Mónadas y sus álgebras

## Hilo conductor

Aquí llega el libro al tema de la plática que lo motivó. Una **mónada** es lo que queda de una adjunción cuando solo se mira una de las dos categorías. La idea apareció en 1958, cuando Roger Godement usó una "construcción estándar" para calcular cohomología de haces. En 1961 Peter Huber observó que toda adjunción produce una de estas construcciones. En 1965, de manera independiente, Heinrich Kleisli, y Samuel Eilenberg con John Moore, demostraron el recíproco: toda mónada proviene de una adjunción. Se les llamó primero "triples" o "construcciones estándar"; el nombre "mónada" se impuso más tarde.

La fuerza del concepto está en su **potencial unificador**: los monoides, los grupos, los espacios vectoriales y los retículos completos son, todos, álgebras sobre alguna mónada, y los operadores de cerradura son ellos mismos mónadas. Una mónada codifica **una teoría algebraica** y sus álgebras son **los modelos de esa teoría**.

## Ideas previas que se cristalizan

- Una lista de listas se "aplana" concatenando; una lista con un elemento es un elemento.
- Un monoide sabe multiplicar listas finitas de sus elementos, y el resultado no depende de cómo se agrupen.
- Una combinación lineal de combinaciones lineales es una combinación lineal.
- Un operador de cerradura (topológica, convexa, subgrupo generado) cumple \\(S \subseteq \overline{S}\\) y \\(\overline{\overline{S}} = \overline{S}\\).
- El unitario \\(x \mapsto \\{x\\}\\) y la unión \\(\mathcal{S} \mapsto \bigcup \mathcal{S}\\) son naturales (Ejemplo 3.5).

---

## 1. La definición

> **Definición 10.1 (Mónada).**
> Una **mónada** sobre una categoría \\(\mathcal{C}\\) es una terna \\((T, \eta, \mu)\\) formada por un funtor \\(T\colon \mathcal{C} \to \mathcal{C}\\) y dos transformaciones naturales
>
> \\[
> \eta\colon 1\_{\mathcal{C}} \Rightarrow T \quad \text{(unidad)}, \qquad \mu\colon TT \Rightarrow T \quad \text{(multiplicación)},
> \\]
>
> tales que conmutan los diagramas de **asociatividad** y **unidad**:
>
> \\[
> \require{AMScd}
> \begin{CD}
> TTT @>{T\mu}>> TT \\\\
> @V{\mu T}VV @VV{\mu}V \\\\
> TT @>>{\mu}> T
> \end{CD}
> \qquad\qquad
> \mu \circ T\eta = 1\_T = \mu \circ \eta T.
> \\]

Compare con la definición de monoide: una operación \\(m\colon M \times M \to M\\) asociativa, \\(m \circ (m \times 1) = m \circ (1 \times m)\\), y un neutro \\(e\\). La mónada tiene la misma forma, con la composición de funtores en el lugar del producto cartesiano. El Capítulo 12 hará precisa esta analogía: **una mónada es un monoide en la categoría de endofuntores**.

La lectura intuitiva es la siguiente. \\(TX\\) es el conjunto de **expresiones formales** construidas con elementos de \\(X\\). La unidad \\(\eta\_X\\) ve cada elemento como una expresión trivial. La multiplicación \\(\mu\_X\\) **aplana** una expresión de expresiones en una sola expresión. Los axiomas dicen que aplanar en dos pasos no depende del orden, y que aplanar una expresión trivial no cambia nada.

---

## 2. Ejemplos

> **Ejemplo 10.2 (La mónada de listas).**
> En \\(\mathbf{Set}\\), sea \\(L(X)\\) el conjunto de listas finitas de elementos de \\(X\\). Se definen \\(\eta\_X(x) = (x)\\), la lista de un elemento, y \\(\mu\_X\\) como la **concatenación de una lista de listas**:
>
> \\[
> \mu\_X\big((x\_1, x\_2), (), (x\_3)\big) = (x\_1, x\_2, x\_3).
> \\]
>
> La asociatividad dice que aplanar una lista de listas de listas de "adentro hacia afuera" o de "afuera hacia adentro" da lo mismo.

> **Ejemplo 10.3 (La mónada de conjunto potencia).**
> \\(\mathcal{P}\colon \mathbf{Set} \to \mathbf{Set}\\) con \\(\eta\_X(x) = \\{x\\}\\) y \\(\mu\_X(\mathcal{S}) = \bigcup \mathcal{S}\\). Una "expresión formal" en \\(X\\) es aquí un subconjunto, y aplanar es unir.

> **Ejemplo 10.4 (La mónada de elementos opcionales).**
> \\(T(X) = X + \\{\bot\\}\\), con \\(\eta\_X\\) la inclusión y \\(\mu\_X\\) la función que identifica los dos puntos agregados \\(\bot\\). Modela **cálculos que pueden fallar**: \\(\bot\\) representa el fallo, y fallar dentro de un fallo es fallar.

> **Ejemplo 10.5 (Combinaciones lineales formales).**
> Sea \\(V(X) = k^{(X)}\\), el conjunto de combinaciones lineales formales finitas \\(\sum a\_i x\_i\\). La unidad es \\(x \mapsto 1 \cdot x\\). La multiplicación toma una combinación de combinaciones y **distribuye**:
>
> \\[
> \mu\_X\Big(\sum\_i a\_i \big(\sum\_j b\_{ij} x\_j\big)\Big) = \sum\_j \Big(\sum\_i a\_i b\_{ij}\Big) x\_j.
> \\]

> **Ejemplo 10.6 (Mónadas sobre un orden parcial = operadores de cerradura).**
> Sea \\(P\\) un orden parcial visto como categoría. Una mónada sobre \\(P\\) es una función monótona \\(c\colon P \to P\\) con
>
> \\[
> x \le c(x) \quad \text{(unidad)}, \qquad c(c(x)) \le c(x) \quad \text{(multiplicación)}.
> \\]
>
> Las ecuaciones de la Definición 10.1 son automáticas, porque en un orden todo diagrama conmuta. Juntas, las dos desigualdades dan \\(c(c(x)) = c(x)\\). **Una mónada sobre un orden es un operador de cerradura.** Ejemplos en \\(\mathcal{P}(X)\\): la cerradura topológica, la envolvente convexa, el subgrupo generado, la cerradura deductiva de un conjunto de fórmulas.

> **Ejemplo 10.7 (Distribuciones finitas).**
> Sea \\(\mathcal{D}(X)\\) el conjunto de distribuciones de probabilidad de soporte finito sobre \\(X\\): funciones \\(p\colon X \to [0,1]\\) con soporte finito y \\(\sum\_x p(x) = 1\\). La unidad envía \\(x\\) a la distribución concentrada en \\(x\\) (la delta de Dirac \\(\delta\_x\\)). La multiplicación toma una distribución sobre distribuciones y la **promedia**:
>
> \\[
> \mu\_X(\Phi)(x) = \sum\_{p} \Phi(p)\\, p(x).
> \\]
>
> Es la ley de probabilidad total. Esta mónada es el punto de partida del Capítulo 11.

> **📝 Para pensar.** En todos los ejemplos, \\(\mu\\) "aplana dos niveles en uno". ¿Qué es un "segundo nivel" en la mónada de distribuciones? Piensa en un experimento de dos etapas: primero se elige una urna al azar, y luego una bola de esa urna.

---

## 3. Toda adjunción produce una mónada

> **Teorema 10.8.**
> Sea \\(F \dashv G\\), con \\(F\colon \mathcal{C} \to \mathcal{D}\\), unidad \\(\eta\\) y counidad \\(\varepsilon\\). Entonces
>
> \\[
> T = GF, \qquad \eta\colon 1 \Rightarrow GF, \qquad \mu = G\varepsilon F\colon GFGF \Rightarrow GF
> \\]
>
> es una mónada sobre \\(\mathcal{C}\\).
>
> *Demostración.* Las leyes de unidad son las identidades triangulares, compuestas con \\(G\\) o con \\(F\\):
>
> \\[
> \mu \circ \eta T = G\varepsilon F \circ \eta GF = (G\varepsilon \circ \eta G) F = 1\_{GF},
> \\]
>
> \\[
> \mu \circ T\eta = G\varepsilon F \circ GF\eta = G(\varepsilon F \circ F\eta) = 1\_{GF}.
> \\]
>
> La asociatividad \\(\mu \circ T\mu = \mu \circ \mu T\\) se reduce, al factorizar \\(G\\) a la izquierda y \\(F\\) a la derecha, a la igualdad \\(\varepsilon \circ FG\varepsilon = \varepsilon \circ \varepsilon FG\\) de transformaciones \\(FGFG \Rightarrow 1\\). Esta igualdad es la naturalidad de \\(\varepsilon\\) aplicada a las flechas \\(\varepsilon\_Y\\). \\(\blacksquare\\)

> **Ejemplo 10.9 (Mónadas conocidas a partir de adjunciones).**
>
> | Adjunción | Mónada \\(GF\\) en \\(\mathbf{Set}\\) |
> | :--- | :--- |
> | Monoide libre \\(\dashv\\) olvidadizo | Listas \\(L\\) |
> | Espacio vectorial libre \\(\dashv\\) olvidadizo | Combinaciones lineales formales \\(V\\) |
> | Grupo libre \\(\dashv\\) olvidadizo | Palabras reducidas |
> | \\(- \times B \dashv (-)^B\\) | \\(X \mapsto (X \times B)^B\\), la **mónada de estado** |

La mónada de estado es un ejemplo instructivo fuera del álgebra clásica. Un elemento de \\((X \times B)^B\\) es un cálculo que recibe un estado \\(b\\), produce un resultado en \\(X\\) y deja un estado nuevo. Las mónadas se usan así en programación funcional (Haskell) para modelar estado, excepciones, no determinismo y probabilidad: cada efecto computacional es una mónada.

---

## 4. Álgebras sobre una mónada

Si \\(TX\\) es el conjunto de expresiones formales, una **álgebra** es un conjunto que sabe **evaluar** esas expresiones de manera coherente.

> **Definición 10.10 (Álgebra de Eilenberg–Moore).**
> Una **\\(T\\)-álgebra** es un par \\((A, a)\\), con \\(A\\) un objeto de \\(\mathcal{C}\\) y \\(a\colon TA \to A\\) una flecha (la **estructura**), tal que
>
> \\[
> a \circ \eta\_A = 1\_A, \qquad a \circ T(a) = a \circ \mu\_A.
> \\]
>
> Un **morfismo de álgebras** \\((A, a) \to (B, b)\\) es una flecha \\(h\colon A \to B\\) con \\(h \circ a = b \circ T(h)\\). Las \\(T\\)-álgebras forman la **categoría de Eilenberg–Moore** \\(\mathcal{C}^T\\).

La primera ecuación dice que evaluar una expresión trivial devuelve el elemento. La segunda dice que evaluar por partes (primero las subexpresiones, luego el resultado) es lo mismo que aplanar y evaluar de una vez.

En diagramas, los axiomas de álgebra (izquierda y centro) y la condición de morfismo (derecha) son:

\\[
\require{AMScd}
\begin{CD}
A @>{\eta\_A}>> TA \\\\
@| @VV{a}V \\\\
A @= A
\end{CD}
\qquad
\begin{CD}
TTA @>{T(a)}>> TA \\\\
@V{\mu\_A}VV @VV{a}V \\\\
TA @>>{a}> A
\end{CD}
\qquad
\begin{CD}
TA @>{T(h)}>> TB \\\\
@V{a}VV @VV{b}V \\\\
A @>>{h}> B
\end{CD}
\\]

Compare el cuadrado central con el de asociatividad de la Definición 10.1: tiene la misma forma, con \\(a\\) en el lugar de \\(\mu\\). Un álgebra es "una mónada aplicada a un solo objeto".

> **Teorema 10.11 (Las álgebras de la mónada de listas son los monoides).**
> \\(\mathbf{Set}^L \cong \mathbf{Mon}\\).
>
> *Demostración.* Si \\((M, \cdot, e)\\) es un monoide, se define \\(a(x\_1, \dots, x\_n) = x\_1 \cdots x\_n\\), con \\(a() = e\\). La ecuación de unidad es \\(a(x) = x\\). La de asociatividad dice que multiplicar los productos de varias sublistas es lo mismo que multiplicar la lista concatenada, lo cual vale por la asociatividad y el neutro del monoide.
>
> Recíprocamente, si \\((M, a)\\) es una \\(L\\)-álgebra, se define \\(x \cdot y = a(x, y)\\) y \\(e = a()\\). La asociatividad se obtiene al evaluar la lista de listas \\(((x, y), (z))\\) de dos maneras:
>
> \\[
> (x \cdot y) \cdot z = a\big(a(x,y), a(z)\big) = a\big(L(a)((x,y),(z))\big) = a\big(\mu((x,y),(z))\big) = a(x, y, z),
> \\]
>
> y del mismo modo \\(x \cdot (y \cdot z) = a(x, y, z)\\). El neutro se obtiene con \\(((), (x))\\): \\(e \cdot x = a(a(), a(x)) = a(x) = x\\). Las dos construcciones son mutuamente inversas, y una función es un morfismo de álgebras si y solo si es un homomorfismo de monoides. \\(\blacksquare\\)

> **Ejemplo 10.12 (Más álgebras).**
>
> | Mónada | Sus álgebras |
> | :--- | :--- |
> | Listas \\(L\\) | Monoides |
> | Palabras reducidas (grupo libre) | Grupos |
> | Combinaciones lineales formales \\(V\\) | Espacios vectoriales sobre \\(k\\) |
> | Elementos opcionales \\(X + \\{\bot\\}\\) | Conjuntos con un punto distinguido |
> | Conjunto potencia \\(\mathcal{P}\\) | Retículos completos (con funciones que preservan supremos) |
> | Cerradura \\(c\\) en un orden | Los elementos cerrados, \\(c(x) = x\\) |
> | Distribuciones finitas \\(\mathcal{D}\\) | Conjuntos convexos abstractos (Capítulo 11) |

El caso de \\(\mathcal{P}\\) es notable. Una estructura \\(a\colon \mathcal{P}(A) \to A\\) asigna a cada subconjunto un "supremo". Si se define \\(x \le y\\) cuando \\(a(\\{x, y\\}) = y\\), se obtiene un orden parcial en el que \\(a(S)\\) es el supremo de \\(S\\), y todo subconjunto lo tiene. **La mónada de conjunto potencia es la teoría algebraica de los supremos arbitrarios.**

> **📝 Para pensar.** La tabla dice que "ser un grupo" o "ser un espacio vectorial" es tener una manera coherente de evaluar expresiones formales. ¿Qué gana esa descripción frente a la lista habitual de axiomas? ¿Qué teoría conocida **no** puede describirse así? *(Sugerencia: los campos, en los que \\(x^{-1}\\) solo existe si \\(x \neq 0\\).)*

---

## 5. Toda mónada proviene de una adjunción

> **Teorema 10.13 (Eilenberg–Moore).**
> Sea \\(T\\) una mónada sobre \\(\mathcal{C}\\). El funtor olvidadizo \\(U^T\colon \mathcal{C}^T \to \mathcal{C}\\), \\((A, a) \mapsto A\\), tiene un adjunto izquierdo
>
> \\[
> F^T\colon \mathcal{C} \to \mathcal{C}^T, \qquad X \mapsto (TX, \mu\_X),
> \\]
>
> que envía cada objeto a su **álgebra libre**. La mónada que produce la adjunción \\(F^T \dashv U^T\\) es \\(T\\).
>
> *Demostración.* Las leyes de la mónada dicen precisamente que \\((TX, \mu\_X)\\) es un álgebra. La biyección
>
> \\[
> \mathcal{C}^T\big((TX, \mu\_X), (A, a)\big) \cong \mathcal{C}(X, A)
> \\]
>
> envía un morfismo \\(g\\) a \\(g \circ \eta\_X\\), y una flecha \\(f\colon X \to A\\) a \\(a \circ T(f)\\). Que estas asignaciones son mutuamente inversas se comprueba con las leyes de álgebra y la naturalidad de \\(\eta\\) y \\(\mu\\). Finalmente, \\(U^T F^T = T\\), la unidad es \\(\eta\\) y \\(U^T \varepsilon F^T = \mu\\). \\(\blacksquare\\)

Así, la relación entre adjunciones y mónadas va en los dos sentidos: **toda adjunción produce una mónada, y toda mónada proviene de al menos una adjunción**. En general proviene de muchas. El Capítulo 11 muestra que, entre todas ellas, hay una mínima y una máxima.

---

## 🔑 Lo que cristalizó

- Una **mónada** es un endofuntor con unidad y multiplicación asociativas: una teoría de "expresiones formales que se aplanan".
- Las listas, el conjunto potencia, las combinaciones lineales formales, los elementos opcionales y las distribuciones finitas son mónadas; sobre un orden, las mónadas son los **operadores de cerradura**.
- Toda adjunción \\(F \dashv G\\) produce la mónada \\(GF\\).
- Las **álgebras** de una mónada son los modelos de la teoría: monoides, grupos, espacios vectoriales, retículos completos.
- Toda mónada proviene de la adjunción entre su categoría de álgebras y la categoría base.

## 🌉 Puente

La adjunción de Eilenberg–Moore no es la única que produce una mónada dada. El Capítulo 11 construye la otra extrema, la **categoría de Kleisli**, explica cuándo una categoría "es" una categoría de álgebras (monadicidad) y aplica todo a las mónadas de probabilidad.
