# 13. Categorías trenzadas, trenzas y nudos

## Hilo conductor

En una categoría simétrica, intercambiar dos factores dos veces es no hacer nada. En el espacio de tres dimensiones, en cambio, dos hebras que se cruzan dos veces pueden quedar enlazadas, según cuál pase por encima. Este capítulo conserva el isomorfismo de intercambio pero abandona la ecuación \\(s \circ s = 1\\). El resultado es una **categoría monoidal trenzada**. La categoría de trenzas resulta ser la categoría trenzada **libre** sobre un objeto, y la de enredos, la categoría **de listón** libre. De ahí sale un método general para construir invariantes de nudos: elegir una categoría trenzada con duales y un objeto en ella. Es la culminación del libro y el punto de contacto con la teoría de nudos.

## Ideas previas que se cristalizan

- El grupo de trenzas \\(B\_n\\) y su presentación de Artin.
- Los movimientos de Reidemeister: un diagrama determina el nudo salvo estos movimientos.
- El corchete de Kauffman y el polinomio de Jones.
- La ecuación de Yang–Baxter de la mecánica estadística.
- Los diagramas de cuerdas y las identidades del zigzag (Capítulo 12).

---

## 1. La definición

> **Definición 13.1 (Categoría monoidal trenzada).**
> Una **categoría monoidal trenzada** es una categoría monoidal con isomorfismos naturales
>
> \\[
> c\_{A,B}\colon A \otimes B \to B \otimes A,
> \\]
>
> llamados **trenzado**, que satisfacen dos **axiomas del hexágono**. Escritos omitiendo los asociadores:
>
> \\[
> c\_{A, B \otimes C} = (1\_B \otimes c\_{A,C}) \circ (c\_{A,B} \otimes 1\_C), \qquad c\_{A \otimes B, C} = (c\_{A,C} \otimes 1\_B) \circ (1\_A \otimes c\_{B,C}).
> \\]
>
> Si además \\(c\_{B,A} \circ c\_{A,B} = 1\_{A \otimes B}\\) para todos \\(A, B\\), la categoría es **simétrica**.

Los hexágonos dicen que cruzar \\(A\\) sobre un bloque \\(B \otimes C\\) es cruzarlo sobre \\(B\\) y luego sobre \\(C\\). En diagramas de cuerdas, \\(c\_{A,B}\\) se dibuja como un **cruce**, con la cuerda \\(A\\) pasando por encima, y \\(c\_{B,A}^{-1}\colon A \otimes B \to B \otimes A\\) como el cruce opuesto, con la cuerda \\(A\\) por debajo.

<div style="text-align: center; margin: 20px 0;">
<svg viewBox="0 0 300 192" width="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="El trenzado c(A,B) y el cruce inverso c(B,A) a la menos uno">
<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">
<path d="M30 150 L90 30"/>
<path d="M90 150 L68 106"/>
<path d="M52 74 L30 30"/>
<path d="M270 150 L210 30"/>
<path d="M210 150 L232 106"/>
<path d="M248 74 L270 30"/>
</g>
<g fill="currentColor" font-family="serif" font-size="15">
<text x="60" y="187" text-anchor="middle">c(A,B)</text>
<text x="240" y="187" text-anchor="middle">c(B,A)⁻¹</text>
<text x="18" y="158">A</text>
<text x="96" y="158">B</text>
<text x="198" y="158">A</text>
<text x="276" y="158">B</text>
</g>
</svg>
</div>

En el dibujo de la izquierda, la cuerda que sale de \\(A\\) pasa por encima. En el de la derecha pasa por debajo.

> **Proposición 13.2 (Ecuación de Yang–Baxter).**
> En toda categoría trenzada, las dos flechas \\(A \otimes B \otimes C \to C \otimes B \otimes A\\) siguientes son iguales:
>
> \\[
> (c\_{B,C} \otimes 1\_A) \circ (1\_B \otimes c\_{A,C}) \circ (c\_{A,B} \otimes 1\_C) = (1\_C \otimes c\_{A,B}) \circ (c\_{A,C} \otimes 1\_B) \circ (1\_A \otimes c\_{B,C}).
> \\]
>
> *Demostración.* La naturalidad de \\(c\_{-,C}\\) respecto de la flecha \\(c\_{A,B}\colon A \otimes B \to B \otimes A\\) dice
>
> \\[
> c\_{B \otimes A, C} \circ (c\_{A,B} \otimes 1\_C) = (1\_C \otimes c\_{A,B}) \circ c\_{A \otimes B, C}.
> \\]
>
> Al sustituir el segundo hexágono en ambos lados, \\(c\_{B \otimes A, C} = (c\_{B,C} \otimes 1\_A) \circ (1\_B \otimes c\_{A,C})\\) y \\(c\_{A \otimes B, C} = (c\_{A,C} \otimes 1\_B) \circ (1\_A \otimes c\_{B,C})\\), se obtiene exactamente la ecuación buscada. \\(\blacksquare\\)

En diagramas de cuerdas, la ecuación de Yang–Baxter dice que una hebra puede deslizarse por encima de un cruce de otras dos. **Es el tercer movimiento de Reidemeister.** Que los cruces sean invertibles, \\(c \circ c^{-1} = 1\\), es el **segundo movimiento**.

---

## 2. La categoría de trenzas

> **Definición 13.3 (Grupo de trenzas).**
> El **grupo de trenzas** \\(B\_n\\) tiene la presentación de Artin con generadores \\(\sigma\_1, \dots, \sigma\_{n-1}\\) y relaciones
>
> \\[
> \sigma\_i \sigma\_{i+1} \sigma\_i = \sigma\_{i+1} \sigma\_i \sigma\_{i+1}, \qquad \sigma\_i \sigma\_j = \sigma\_j \sigma\_i \ \text{ si } |i - j| \ge 2.
> \\]
>
> El generador \\(\sigma\_i\\) es el cruce de las hebras \\(i\\) e \\(i+1\\), con la hebra \\(i\\) por encima.

> **Definición 13.4 (Categoría de trenzas).**
> La **categoría de trenzas** \\(\mathbb{B}\\) tiene por objetos los números naturales. Hay flechas \\(n \to m\\) solo si \\(n = m\\), y en ese caso son los elementos de \\(B\_n\\), con la composición del grupo. El producto tensorial pone trenzas **lado a lado**: \\(n \otimes m = n + m\\), y \\(B\_n \times B\_m \to B\_{n+m}\\). El trenzado \\(c\_{n,m}\\) es la trenza en la que las \\(n\\) primeras hebras cruzan, en bloque, por encima de las \\(m\\) siguientes.

> **Teorema 13.5 (Joyal–Street).**
> \\(\mathbb{B}\\) es la **categoría monoidal trenzada libre sobre un objeto**. Para toda categoría trenzada \\(\mathcal{V}\\) y todo objeto \\(A\\), existe un funtor monoidal trenzado \\(\mathbb{B} \to \mathcal{V}\\) que envía \\(1\\) a \\(A\\), y es único salvo isomorfismo.

El teorema tiene la forma de una flecha universal (Capítulo 4): \\(\mathbb{B}\\) es el objeto libre, y \\(1\\) es su generador. La consecuencia concreta es un mecanismo para producir representaciones.

> **Corolario 13.6.**
> Para todo objeto \\(A\\) de una categoría trenzada, la asignación
>
> \\[
> \sigma\_i \mapsto 1\_{A^{\otimes (i-1)}} \otimes c\_{A,A} \otimes 1\_{A^{\otimes (n-i-1)}}
> \\]
>
> define un homomorfismo de \\(B\_n\\) en el grupo de automorfismos de \\(A^{\otimes n}\\). La relación de Artin \\(\sigma\_i \sigma\_{i+1} \sigma\_i = \sigma\_{i+1} \sigma\_i \sigma\_{i+1}\\) se cumple por la Proposición 13.2.

---

## 3. Matrices R

En \\(\mathbf{Vect}\_k\\) con su simetría usual, el Corolario 13.6 solo produce representaciones que se factorizan por el grupo simétrico, porque \\(c \circ c = 1\\). Para obtener representaciones genuinas del grupo de trenzas hace falta una **matriz R**: un isomorfismo lineal \\(R\colon V \otimes V \to V \otimes V\\) que cumple la ecuación de Yang–Baxter

\\[
(R \otimes 1)(1 \otimes R)(R \otimes 1) = (1 \otimes R)(R \otimes 1)(1 \otimes R).
\\]

Las matrices R aparecieron en la mecánica estadística (modelos exactamente solubles de Baxter) y en la teoría cuántica de dispersión. Desde la década de 1980 se obtienen de manera sistemática a partir de los **grupos cuánticos** de Drinfeld y Jimbo, cuyas categorías de representaciones son trenzadas. Cada matriz R da representaciones de todos los grupos de trenzas a la vez.

---

## 4. Enredos e invariantes de nudos

Las trenzas solo permiten hebras que suben. Para obtener nudos cerrados hacen falta las copas y tapas del Capítulo 12.

> **Definición 13.7 (Enredos).**
> Un **enredo** es una colección de arcos y lazos encajados en \\(\mathbb{R}^2 \times [0,1]\\), cuyos extremos están en las caras inferior y superior. La categoría de enredos tiene por objetos las sucesiones finitas de puntos (con orientación, en la versión orientada) y por flechas los enredos salvo isotopía. La composición apila enredos; el tensor los pone lado a lado.

Todo enredo se descompone en piezas elementales: **cruces** (\\(c\\) y \\(c^{-1}\\)), **copas** (\\(\mathrm{coev}\\)) y **tapas** (\\(\mathrm{ev}\\)). Dos descomposiciones dan el mismo enredo si y solo si se pasa de una a otra por isotopías planas (las identidades del zigzag) y por los movimientos de Reidemeister.

Un **nudo** o **enlace** es un enredo sin extremos: una flecha \\(\emptyset \to \emptyset\\), es decir, un endomorfismo de la unidad \\(I\\).

> **Teorema 13.8 (Enredos libres: Shum, Turaev, Freyd–Yetter).**
> La categoría de enredos orientados **enmarcados** es la **categoría de listón libre** sobre un objeto.

Una **categoría de listón** (*ribbon*) es una categoría trenzada con duales y con un **giro** \\(\theta\_A\colon A \to A\\) compatible con el trenzado. El giro codifica la torsión de una banda, y por eso aparecen los enredos enmarcados: el primer movimiento de Reidemeister cambia el marco, y solo se recupera la invariancia completa después de una corrección.

El Teorema 13.8 convierte la construcción de invariantes en un procedimiento:

1. elegir una categoría de listón \\(\mathcal{V}\\) y un objeto \\(A\\) en ella;
2. el funtor libre envía cada nudo, que es una flecha \\(I \to I\\), a una flecha \\(I \to I\\) de \\(\mathcal{V}\\);
3. si \\(\mathcal{V}\\) es una categoría de representaciones, \\(\mathrm{End}(I) = k\\), y el resultado es **un número**, invariante bajo isotopía (salvo la corrección por el marco).

Este es el método de **Reshetikhin y Turaev** (1990–1991). Con las representaciones del grupo cuántico \\(U\_q(\mathfrak{sl}\_2)\\) y su representación de dimensión 2, el invariante es, salvo normalización, el **polinomio de Jones**.

### El corchete de Kauffman como funtor

El polinomio de Jones admite una presentación elemental, debida a Kauffman, que ilustra el procedimiento sin grupos cuánticos. Las reglas del **corchete** de un diagrama \\(D\\) son:

- \\(\langle \bigcirc \rangle = 1\\);
- \\(\langle D \sqcup \bigcirc \rangle = \delta \langle D \rangle\\), con \\(\delta = -A^2 - A^{-2}\\);
- en cada cruce, \\(\langle \text{cruce} \rangle = A \langle \text{suavizado }A \rangle + A^{-1} \langle \text{suavizado }B \rangle\\).

En lenguaje categórico, estas reglas definen un funtor monoidal desde los enredos no orientados **enmarcados** (o, equivalentemente, desde los diagramas módulo isotopía plana y los movimientos II y III) hacia la **categoría de Temperley–Lieb**, cuyas flechas son combinaciones lineales de diagramas planos sin cruces. El cruce se envía a \\(A\\) por el diagrama de dos hebras paralelas más \\(A^{-1}\\) por el diagrama \\(\mathrm{coev} \circ \mathrm{ev}\\), en el que las dos hebras de abajo se unen entre sí y las dos de arriba también. Un lazo cerrado se envía a \\(\delta\\): la **dimensión** del Capítulo 12. Por eso el valor del funtor en un enlace \\(L\\) es \\(\delta \langle L \rangle\\); la regla \\(\langle \bigcirc \rangle = 1\\) es solo una normalización, que divide entre \\(\delta\\).

El corchete es invariante bajo los movimientos II y III, pero no bajo el I: un rizo multiplica el corchete por \\(-A^{\pm 3}\\). Se corrige con la **torsión** (*writhe*) \\(w(D)\\), la suma de los signos de los cruces de un diagrama orientado:

\\[
X(L) = (-A^{3})^{-w(D)} \langle D \rangle.
\\]

\\(X(L)\\) es un invariante del enlace orientado \\(L\\), y al sustituir \\(A = t^{-1/4}\\) se obtiene el polinomio de Jones \\(V\_L(t)\\). La corrección por la torsión es, en el lenguaje del Teorema 13.8, la corrección por el marco.

> **📝 Para pensar.** El polinomio de Jones se descubrió en 1984 por una vía analítica (álgebras de von Neumann), no por la vía categórica de este capítulo. La vía categórica llegó después y explicó por qué existía. ¿Qué te dice esa historia sobre el papel de la teoría de categorías en el descubrimiento matemático: produce resultados, o los ordena y los generaliza una vez obtenidos? ¿Hay contraejemplos?

---

## 5. Una pregunta para quien construye invariantes

Un invariante que proviene de un funtor desde la categoría de enredos se puede **calcular por pedazos**: se corta el diagrama en piezas elementales, se evalúa cada pieza y se compone. Esa propiedad (la funtorialidad respecto de cortar y pegar) es fuerte y no la tiene cualquier invariante. El número de cruces mínimo, por ejemplo, no se calcula así.

Para quien trabaja con un marco combinatorio propio de invariantes de nudos, la pregunta categórica natural es: **¿mi invariante es funtorial respecto de alguna categoría de enredos?** Si lo es, el Teorema 13.8 sugiere buscar la categoría de listón que lo produce; si no lo es, conviene saber exactamente qué parte del corte y pegado falla. El Ejercicio 12 de la Parte VI propone hacer este análisis.

---

## 🔑 Lo que cristalizó

- Una **categoría trenzada** tiene isomorfismos de intercambio que cumplen los hexágonos pero no necesariamente \\(c \circ c = 1\\).
- La **ecuación de Yang–Baxter** se sigue de los axiomas; es el tercer movimiento de Reidemeister.
- La **categoría de trenzas** es la categoría trenzada libre sobre un objeto; cada objeto de una categoría trenzada da representaciones de los grupos de trenzas.
- La **categoría de enredos enmarcados** es la categoría de listón libre; elegir una categoría de listón y un objeto produce un invariante de nudos (Reshetikhin–Turaev).
- El **corchete de Kauffman** es un funtor hacia la categoría de Temperley–Lieb; corregido por la torsión, da el polinomio de Jones.

## 🌉 Puente

Las mónadas viven en la categoría de endofuntores, que tiene flechas entre flechas: las transformaciones naturales. ¿Qué pasa con las mónadas cuando las ecuaciones entre flechas se reemplazan por isomorfismos coherentes, como en el paso de las categorías monoidales estrictas a las generales? El Epílogo responde: aparecen las **seudo-mónadas**, el tema final de la plática que motivó este libro.
