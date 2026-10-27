# 11. Kleisli, monadicidad y mónadas de probabilidad

## Hilo conductor

El Capítulo 10 mostró que toda mónada proviene de una adjunción: la de su categoría de álgebras. Este capítulo presenta la otra construcción canónica, la **categoría de Kleisli**, cuyas flechas son "funciones con efectos": funciones parciales, relaciones, transiciones probabilísticas. Después se plantea cuándo una categoría es, esencialmente, una categoría de álgebras (**monadicidad**). El capítulo cierra con la mónada de distribuciones, donde la categoría de Kleisli resulta ser la de **núcleos de Markov**. Ahí se examina, con cuidado, qué ofrece este lenguaje a la estadística aplicada.

## Ideas previas que se cristalizan

- Una relación \\(R \subseteq X \times Y\\) es lo mismo que una función \\(X \to \mathcal{P}(Y)\\).
- Una función parcial de \\(X\\) en \\(Y\\) es una función \\(X \to Y + \\{\bot\\}\\).
- Una probabilidad condicional \\(P(y \mid x)\\) es una función que asigna a cada \\(x\\) una distribución sobre \\(Y\\).
- La ecuación de Chapman–Kolmogorov: las matrices de transición de una cadena de Markov se componen multiplicándose.
- La ley de probabilidad total: \\(P(y) = \sum\_x P(y \mid x) P(x)\\).

---

## 1. La categoría de Kleisli

> **Definición 11.1 (Categoría de Kleisli).**
> Sea \\((T, \eta, \mu)\\) una mónada sobre \\(\mathcal{C}\\). La **categoría de Kleisli** \\(\mathcal{C}\_T\\) tiene los mismos objetos que \\(\mathcal{C}\\). Una flecha \\(X \rightsquigarrow Y\\) en \\(\mathcal{C}\_T\\) es una flecha \\(f\colon X \to TY\\) de \\(\mathcal{C}\\). La composición de \\(f\colon X \to TY\\) y \\(g\colon Y \to TZ\\) es
>
> \\[
> g \circ\_T f = \mu\_Z \circ T(g) \circ f\colon X \to TZ,
> \\]
>
> y la identidad de \\(X\\) es \\(\eta\_X\colon X \to TX\\).

La composición se lee así: \\(f\\) produce una expresión en \\(Y\\); \\(T(g)\\) sustituye cada elemento de \\(Y\\) por una expresión en \\(Z\\); \\(\mu\\) aplana el resultado. Como cadena de flechas de \\(\mathcal{C}\\):

\\[
X \xrightarrow{\ \ f\ \ } TY \xrightarrow{\ T(g)\ } TTZ \xrightarrow{\ \mu\_Z\ } TZ.
\\]

Para la asociatividad, sean además \\(h\colon Z \to TW\\). Tras \\(T(g) \circ f\colon X \to TTZ\\), los dos compuestos \\(h \circ\_T (g \circ\_T f)\\) y \\((h \circ\_T g) \circ\_T f\\) recorren los dos bordes de este diagrama, desde \\(TTZ\\) hasta \\(TW\\):

\\[
\require{AMScd}
\begin{CD}
TTZ @>{TT(h)}>> TTTW @>{T(\mu\_W)}>> TTW \\\\
@V{\mu\_Z}VV @V{\mu\_{TW}}VV @VV{\mu\_W}V \\\\
TZ @>>{T(h)}> TTW @>>{\mu\_W}> TW
\end{CD}
\\]

El borde superior seguido de la derecha es \\((h \circ\_T g) \circ\_T f\\); la izquierda seguida del borde inferior es \\(h \circ\_T (g \circ\_T f)\\). El cuadrado izquierdo conmuta por la **naturalidad** de \\(\mu\\) y el derecho por la **asociatividad** de \\(\mu\\). Por lo tanto, los dos compuestos coinciden. Que \\(\mathcal{C}\_T\\) es una categoría se sigue directamente de las leyes de la mónada: la ley de unidad da la neutralidad de \\(\eta\\), y la asociatividad de \\(\mu\\), junto con su naturalidad, da la asociatividad de \\(\circ\_T\\) (Ejercicio 3 de la Parte V).

> **Ejemplo 11.2 (Relaciones).**
> En la categoría de Kleisli de \\(\mathcal{P}\\), una flecha \\(X \rightsquigarrow Y\\) es una función \\(f\colon X \to \mathcal{P}(Y)\\), es decir, una relación \\(R = \\{(x,y) \mid y \in f(x)\\}\\). La composición de Kleisli es
>
> \\[
> (g \circ\_{\mathcal{P}} f)(x) = \bigcup\_{y \in f(x)} g(y),
> \\]
>
> que es la composición de relaciones. Luego \\(\mathbf{Set}\_{\mathcal{P}} \cong \mathbf{Rel}\\), la categoría del Ejemplo 1.3.

> **Ejemplo 11.3 (Funciones parciales).**
> Para la mónada \\(X + \\{\bot\\}\\), una flecha de Kleisli es una función que puede no estar definida, y la composición se indefine en cuanto alguno de los pasos lo hace. La categoría de Kleisli es la de **conjuntos y funciones parciales**.

> **Ejemplo 11.4 (Matrices).**
> Para la mónada \\(V\\) de combinaciones lineales formales, una flecha de Kleisli \\(X \rightsquigarrow Y\\) entre conjuntos finitos asigna a cada \\(x\\) una combinación \\(\sum\_y a\_{yx}\\, y\\): es una matriz de tamaño \\(|Y| \times |X|\\). La composición de Kleisli es el producto de matrices. Restringida a conjuntos finitos, la categoría de Kleisli de \\(V\\) es equivalente a \\(\mathbf{Mat}\_k\\) (Ejemplo 1.4).

### Las dos adjunciones extremas

Hay una adjunción \\(F\_T \dashv U\_T\\) entre \\(\mathcal{C}\\) y \\(\mathcal{C}\_T\\): \\(F\_T\\) es la identidad en objetos y envía \\(f\colon X \to Y\\) a \\(\eta\_Y \circ f\\); \\(U\_T\\) envía \\(X\\) a \\(TX\\) y una flecha de Kleisli \\(g\colon X \to TY\\) a \\(\mu\_Y \circ T(g)\\). La mónada de esta adjunción es, otra vez, \\(T\\).

> **Teorema 11.5 (Kleisli y Eilenberg–Moore son los extremos).**
> Sea \\(T\\) una mónada sobre \\(\mathcal{C}\\). Considérese la categoría de todas las adjunciones \\(F \dashv G\\), con \\(F\colon \mathcal{C} \to \mathcal{D}\\), cuya mónada es \\(T\\), con funtores de comparación como flechas. En ella, la adjunción de Kleisli es **inicial** y la de Eilenberg–Moore es **terminal**.

En particular, hay un funtor de comparación \\(\mathcal{C}\_T \to \mathcal{C}^T\\), plenamente fiel, que identifica la categoría de Kleisli con la subcategoría plena de las **álgebras libres** \\((TX, \mu\_X)\\). La categoría de Kleisli es "la parte libre" de la teoría; la de Eilenberg–Moore, "la teoría completa".

---

## 2. Monadicidad

¿Cuándo una adjunción "es" la de Eilenberg–Moore de su mónada?

> **Definición 11.6 (Funtor monádico).**
> Un funtor \\(G\colon \mathcal{D} \to \mathcal{C}\\) con adjunto izquierdo \\(F\\) es **monádico** si el funtor de comparación \\(\mathcal{D} \to \mathcal{C}^{GF}\\), \\(Y \mapsto (GY, G\varepsilon\_Y)\\), es una equivalencia de categorías.

> **Ejemplo 11.7.**
>
> - Los olvidadizos de \\(\mathbf{Grp}\\), \\(\mathbf{Mon}\\), \\(\mathbf{Ring}\\) y \\(\mathbf{Vect}\_k\\) hacia \\(\mathbf{Set}\\) son monádicos: estas son **categorías algebraicas**.
> - \\(U\colon \mathbf{Top} \to \mathbf{Set}\\) **no** es monádico. Su adjunto izquierdo es la topología discreta, la mónada \\(UD\\) es la identidad, sus álgebras son simplemente los conjuntos, y \\(\mathbf{Top}\\) no es equivalente a \\(\mathbf{Set}\\). **La topología no es una teoría algebraica sobre los conjuntos.**
> - Un resultado sorprendente (Manes, 1969): los **espacios compactos de Hausdorff** sí son monádicos sobre \\(\mathbf{Set}\\). La mónada es la de **ultrafiltros**, y la estructura de álgebra asigna a cada ultrafiltro su único límite.

> **Teorema 11.8 (Teorema de monadicidad de Beck, enunciado).**
> Un funtor \\(G\colon \mathcal{D} \to \mathcal{C}\\) es monádico si y solo si (i) tiene adjunto izquierdo, (ii) refleja isomorfismos y (iii) \\(\mathcal{D}\\) tiene coecualizadores de los pares que \\(G\\) envía en pares "escindidos", y \\(G\\) los preserva.

La prueba (Mac Lane, Capítulo VI; Riehl, Capítulo 5) excede este libro. Lo importante es la lectura: una categoría es algebraica sobre \\(\mathcal{C}\\) cuando sus objetos se pueden presentar por **generadores y relaciones** a la manera de los grupos, y esos cocientes se comportan bien.

---

## 3. Mónadas de probabilidad

La mónada \\(\mathcal{D}\\) de distribuciones finitas (Ejemplo 10.7) admite variantes para espacios más generales. La **mónada de Giry**, introducida por Michèle Giry en 1982 a partir de ideas de Lawvere de 1962, actúa sobre espacios medibles y envía cada espacio a su espacio de medidas de probabilidad.

### A. La categoría de Kleisli: núcleos de Markov

> **Ejemplo 11.9 (Núcleos de Markov).**
> Una flecha de Kleisli \\(f\colon X \rightsquigarrow Y\\) para \\(\mathcal{D}\\) asigna a cada \\(x\\) una distribución \\(f(x)\\) sobre \\(Y\\). Se escribe \\(f(y \mid x)\\) para la probabilidad de \\(y\\) según \\(f(x)\\). Es un **núcleo de Markov**, o probabilidad condicional. La composición de Kleisli es
>
> \\[
> (g \circ\_{\mathcal{D}} f)(z \mid x) = \sum\_{y} g(z \mid y)\\, f(y \mid x),
> \\]
>
> que es la **ecuación de Chapman–Kolmogorov**. Para conjuntos finitos, \\(f\\) es una matriz estocástica (columnas que suman 1) y la composición es el producto de matrices.

Dos casos particulares tienen nombre propio en estadística:

- Una flecha \\(\\{\star\\} \rightsquigarrow X\\) es una **distribución** sobre \\(X\\).
- Componer una distribución \\(p\colon \\{\star\\} \rightsquigarrow X\\) con un núcleo \\(f\colon X \rightsquigarrow Y\\) da la **distribución marginal** de \\(Y\\): \\(\sum\_x f(y \mid x)\\, p(x)\\). Es la ley de probabilidad total, y en la definición de Kleisli es exactamente la multiplicación \\(\mu\\).

### B. Las álgebras: conjuntos convexos

Una \\(\mathcal{D}\\)-álgebra \\(a\colon \mathcal{D}(A) \to A\\) sabe tomar **promedios ponderados finitos** de elementos de \\(A\\) de manera coherente. Las \\(\mathcal{D}\\)-álgebras son los **conjuntos convexos abstractos**, resultado de Świrszcz (1974) expuesto en lenguaje moderno por Jacobs (2010). Ejemplos: subconjuntos convexos de \\(\mathbb{R}^n\\), con la combinación convexa usual; el intervalo \\([0,1]\\); el propio \\(\mathcal{D}(X)\\), con la mezcla de distribuciones. La "esperanza" de una distribución sobre un conjunto convexo es la estructura de álgebra.

### C. Categorías de Markov

Con antecedentes en trabajos de Golubtsov y de Cho y Jacobs, y sistematizada por Tobias Fritz en 2020, se desarrolla la **probabilidad sintética**: un enfoque axiomático en el que las propiedades esenciales de la categoría de núcleos de Markov se toman como axiomas de una **categoría de Markov**. En ese lenguaje se formulan y demuestran de manera abstracta (la teoría de la medida se usa una sola vez, para verificar que el modelo medible cumple los axiomas) resultados como la independencia condicional, la inversión bayesiana y versiones de los teoremas de suficiencia estadística. Los axiomas usan estructura **monoidal**: la capacidad de poner procesos "en paralelo" y de copiar información. Esa estructura es el tema del Capítulo 12.

---

## 4. Una lectura psicométrica, con sus límites

Este apartado propone una traducción, no un resultado.

Considérese un modelo de **clases latentes**: un conjunto finito \\(\Theta\\) de clases, un conjunto finito \\(R\\) de patrones de respuesta a un instrumento, una distribución previa \\(\pi\\) sobre las clases y probabilidades de respuesta condicionales a la clase. En el lenguaje de este capítulo:

| Noción estadística | Noción categórica |
| :--- | :--- |
| Distribución previa \\(\pi\\) sobre \\(\Theta\\) | Flecha de Kleisli \\(\\{\star\\} \rightsquigarrow \Theta\\) |
| Modelo de respuesta \\(P(r \mid \theta)\\) | Núcleo de Markov \\(\Theta \rightsquigarrow R\\) |
| Distribución marginal de los patrones | Composición de Kleisli \\(\\{\star\\} \rightsquigarrow \Theta \rightsquigarrow R\\) |
| Independencia local entre reactivos | Factorización del núcleo como copia de la clase seguida de un núcleo por reactivo en paralelo: \\((f\_1 \otimes \cdots \otimes f\_n) \circ \mathrm{copia}\_\Theta\\) (requiere el Capítulo 12) |
| Probabilidad posterior de la clase | Inversión bayesiana del núcleo |

**Lo que esta traducción aporta:** un lenguaje en el que la estructura de un modelo (qué depende de qué y cómo se componen las etapas) se dibuja y se verifica de manera uniforme, y en el que hipótesis como la independencia local tienen una formulación precisa y libre de coordenadas.

**Lo que no aporta, al menos hoy:** estimadores nuevos, ajustes de modelos, índices de confiabilidad ni decisiones de validez. Usar la probabilidad sintética para obtener resultados nuevos en psicometría sería trabajo de investigación original, y no se conoce todavía una aplicación de ese tipo con impacto práctico. Conviene tratar este puente como una **pregunta abierta**, no como una herramienta disponible.

> **📝 Para pensar.** La tabla anterior traduce, pero ¿simplifica algo? Elige un resultado psicométrico que conozcas bien (por ejemplo, la invariancia de los parámetros en teoría de respuesta al ítem) y pregúntate si tiene una formulación natural como propiedad de una flecha o de una composición. Si no la encuentras, eso también es información.

---

## 🔑 Lo que cristalizó

- La **categoría de Kleisli** tiene por flechas las funciones \\(X \to TY\\) con efectos; con \\(\mathcal{P}\\) da las relaciones, con elementos opcionales las funciones parciales, con combinaciones lineales las matrices.
- Kleisli y Eilenberg–Moore son la adjunción **inicial** y la **terminal** que producen una mónada dada.
- Un funtor es **monádico** si su categoría es la de álgebras de su mónada; los grupos y los espacios compactos de Hausdorff lo son sobre \\(\mathbf{Set}\\), los espacios topológicos no.
- Con la mónada de distribuciones, la categoría de Kleisli es la de **núcleos de Markov**, y su composición es la ley de probabilidad total.
- La traducción de modelos psicométricos a este lenguaje es posible y clarifica la estructura, pero su utilidad práctica es una pregunta abierta.

## 🌉 Puente

Para hablar de independencia, de procesos en paralelo o de copiar información, hace falta poder "multiplicar" objetos y flechas dentro de una categoría de manera más flexible que el producto cartesiano. La Parte VI introduce esa estructura, las **categorías monoidales**, y la lleva hasta los nudos.
