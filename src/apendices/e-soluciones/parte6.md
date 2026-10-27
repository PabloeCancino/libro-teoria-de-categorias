# Soluciones de la Parte VI

Soluciones completas de los ejercicios de nivel 1 y 2 de la Parte VI (categorías monoidales, trenzadas y nudos). Conviene intentar cada ejercicio antes de leer su solución.

---

## Nivel 1

### Ejercicio 1

*\\((\mathbf{Set}, \sqcup, \emptyset)\\) es una categoría monoidal. ¿Es simétrica?*

**Datos.** Se toma la unión disjunta concreta \\(A \sqcup B = (A \times \\{1\\}) \cup (B \times \\{2\\})\\), y \\(f \sqcup g\\) actúa como \\(f\\) en la primera parte y como \\(g\\) en la segunda. Esto define un funtor \\(\sqcup\colon \mathbf{Set} \times \mathbf{Set} \to \mathbf{Set}\\), que es el coproducto del Ejemplo 4.8. Los isomorfismos estructurales son:

- \\(\alpha\_{A,B,C}\colon (A \sqcup B) \sqcup C \to A \sqcup (B \sqcup C)\\), con \\(((a,1),1) \mapsto (a,1)\\), \\(((b,2),1) \mapsto ((b,1),2)\\) y \\((c,2) \mapsto ((c,2),2)\\);
- \\(\lambda\_A\colon \emptyset \sqcup A \to A\\), con \\((a, 2) \mapsto a\\), y \\(\rho\_A\colon A \sqcup \emptyset \to A\\), con \\((a, 1) \mapsto a\\).

Son biyecciones, y son naturales: por ejemplo, \\(\alpha \circ ((f \sqcup g) \sqcup h)\\) y \\((f \sqcup (g \sqcup h)) \circ \alpha\\) aplican \\(f\\), \\(g\\) o \\(h\\) según la parte y colocan el resultado en la misma parte.

**Coherencia.** Sea \\(W\\) un objeto construido a partir de \\(A\_1, \dots, A\_n\\) y de copias de \\(\emptyset\\) con \\(\sqcup\\) y algún paréntesis. Cada elemento de \\(W\\) está en exactamente una de las partes \\(A\_i\\). Así, \\(W\\) tiene una **etiqueta** canónica \\(W \to \coprod\_i A\_i\\), \\(w \mapsto (i, a)\\), que es una biyección. Las copias de \\(\emptyset\\) no aportan elementos. Cada una de las flechas \\(\alpha\\), \\(\lambda\\), \\(\rho\\), sus inversas y sus uniones disjuntas con identidades **conserva la etiqueta**: envía el elemento \\(a\\) de la parte \\(A\_i\\) al mismo \\(a\\), en la parte \\(A\_i\\) del codominio. Por lo tanto, también la conserva cualquier composición de ellas. Dos funciones \\(W \to W'\\) que conservan la etiqueta son iguales, porque las dos etiquetas son biyecciones.

Los dos lados del pentágono son funciones \\(((A \sqcup B) \sqcup C) \sqcup D \to A \sqcup (B \sqcup (C \sqcup D))\\) que conservan la etiqueta, así que son iguales. Los dos lados del triángulo son funciones \\((A \sqcup \emptyset) \sqcup B \to A \sqcup B\\) que conservan la etiqueta, así que también son iguales. Luego \\((\mathbf{Set}, \sqcup, \emptyset)\\) es monoidal.

**Simetría.** Sea \\(s\_{A,B}\colon A \sqcup B \to B \sqcup A\\), con \\((a,1) \mapsto (a,2)\\) y \\((b,2) \mapsto (b,1)\\). Es natural y \\(s\_{B,A} \circ s\_{A,B} = 1\\). También conserva la etiqueta (ahora como función \\(A \sqcup B \to B \sqcup A\\), con el sumando \\(A\\) colocado en otro lugar). Los hexágonos de la Definición 13.1 comparan funciones \\(A \sqcup (B \sqcup C) \to (B \sqcup C) \sqcup A\\), y sus análogos, construidas con \\(s\\), \\(\alpha\\) e identidades. Todas envían cada elemento de \\(A\\), \\(B\\) o \\(C\\) a sí mismo, en su sumando. Por el mismo argumento, coinciden. **Sí, es simétrica.** \\(\blacksquare\\)

El argumento vale en cualquier categoría con coproductos finitos y objeto inicial. Las flechas estructurales son las que da la propiedad universal (Definición 4.7), y dos flechas que salen de un coproducto y coinciden en cada inclusión son iguales.

---

### Ejercicio 2

*En \\((\mathbf{Set}, \times, \\{\star\\})\\) todo conjunto es un comonoide de manera única, con la diagonal y la función a \\(\\{\star\\}\\).*

Un **comonoide** es la noción dual de la Definición 12.4: un objeto \\(X\\) con flechas \\(d\colon X \to X \otimes X\\) (comultiplicación) y \\(u\colon X \to I\\) (counidad) tales que

\\[
\alpha \circ (d \otimes 1) \circ d = (1 \otimes d) \circ d, \qquad (u \otimes 1) \circ d = \lambda^{-1}, \qquad (1 \otimes u) \circ d = \rho^{-1}.
\\]

**Existencia.** Sean \\(d(x) = (x, x)\\) y \\(u(x) = \star\\). La coasociatividad se cumple porque los dos lados envían \\(x\\) a \\((x, (x, x))\\). Las leyes de counidad se cumplen porque \\((u \times 1)(d(x)) = (\star, x) = \lambda^{-1}(x)\\) y \\((1 \times u)(d(x)) = (x, \star) = \rho^{-1}(x)\\).

**Unicidad.** Como \\(\\{\star\\}\\) es terminal, la única función \\(X \to \\{\star\\}\\) es \\(u\\). Sea \\(d\\) una comultiplicación cualquiera, \\(d(x) = (d\_1(x), d\_2(x))\\). La primera ley de counidad dice \\((\star, d\_2(x)) = (\star, x)\\), así que \\(d\_2 = 1\_X\\). La segunda dice \\((d\_1(x), \star) = (x, \star)\\), así que \\(d\_1 = 1\_X\\). Luego \\(d\\) es la diagonal. \\(\blacksquare\\)

**Interpretación.** En una categoría cartesiana, \\(d\\) **copia** un dato y \\(u\\) lo **borra**, y ninguna otra estructura de comonoide es posible. Copiar y borrar no es gratuito en general. En \\((\mathbf{Vect}\_k, \otimes, k)\\), en cambio, un espacio admite en general muchas estructuras de coálgebra, y la función \\(v \mapsto v \otimes v\\) no es lineal, así que no hay una copia canónica. Esta es la versión algebraica del principio de "no clonación" de la mecánica cuántica. En las categorías de Markov del Capítulo 11, la copia existe, pero no es natural (Ejercicio 11).

---

### Ejercicio 3

*Ecuación de Yang–Baxter para el intercambio \\(s(u \otimes v) = v \otimes u\\) en \\(\mathbf{Vect}\_k\\).*

Las composiciones se leen de derecha a izquierda. El lado izquierdo \\((s \otimes 1)(1 \otimes s)(s \otimes 1)\\) aplica sucesivamente

\\[
u \otimes v \otimes w \quad\mapsto\quad v \otimes u \otimes w \quad\mapsto\quad v \otimes w \otimes u \quad\mapsto\quad w \otimes v \otimes u.
\\]

El lado derecho \\((1 \otimes s)(s \otimes 1)(1 \otimes s)\\) aplica

\\[
u \otimes v \otimes w \quad\mapsto\quad u \otimes w \otimes v \quad\mapsto\quad w \otimes u \otimes v \quad\mapsto\quad w \otimes v \otimes u.
\\]

Los dos lados son lineales y coinciden en los tensores puros \\(u \otimes v \otimes w\\), que generan \\(V \otimes V \otimes V\\). Luego son iguales. \\(\blacksquare\\)

Esto es la Proposición 13.2 en la categoría simétrica \\(\mathbf{Vect}\_k\\), con \\(c = s\\) y \\(A = B = C = V\\). Los dos lados realizan la permutación que invierte el orden, escrita de dos maneras como producto de transposiciones adyacentes.

---

### Ejercicio 4

*Dibujar \\(\sigma\_1 \sigma\_2 \sigma\_1\\) y \\(\sigma\_2 \sigma\_1 \sigma\_2\\) como diagramas de cuerdas y ver que son isotópicos.*

Con la convención del Capítulo 12, la composición se apila de abajo hacia arriba, y \\(\sigma\_i\\) cruza la hebra en la posición \\(i\\) **por encima** de la que está en la posición \\(i+1\\) (Definición 13.3). Como las dos palabras son palíndromos, el orden de lectura no importa.

<div style="text-align: center; margin: 20px 0;">
<svg viewBox="0 0 320 250" width="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Las trenzas sigma1 sigma2 sigma1 y sigma2 sigma1 sigma2, leídas de abajo hacia arriba">
<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">
<path d="M30 210 L70 150"/>
<path d="M70 210 L56 189"/>
<path d="M44 171 L30 150"/>
<path d="M110 210 L110 150"/>
<path d="M70 150 L110 90"/>
<path d="M110 150 L96 129"/>
<path d="M84 111 L70 90"/>
<path d="M30 150 L30 90"/>
<path d="M30 90 L70 30"/>
<path d="M70 90 L56 69"/>
<path d="M44 51 L30 30"/>
<path d="M110 90 L110 30"/>
<path d="M240 210 L280 150"/>
<path d="M280 210 L266 189"/>
<path d="M254 171 L240 150"/>
<path d="M200 210 L200 150"/>
<path d="M200 150 L240 90"/>
<path d="M240 150 L226 129"/>
<path d="M214 111 L200 90"/>
<path d="M280 150 L280 90"/>
<path d="M240 90 L280 30"/>
<path d="M280 90 L266 69"/>
<path d="M254 51 L240 30"/>
<path d="M200 90 L200 30"/>
</g>
<g fill="currentColor" font-family="serif" font-size="15">
<text x="70" y="240" text-anchor="middle">σ₁σ₂σ₁</text>
<text x="240" y="240" text-anchor="middle">σ₂σ₁σ₂</text>
<text x="155" y="125" text-anchor="middle">=</text>
<text x="30" y="226" text-anchor="middle" font-size="12">1</text>
<text x="70" y="226" text-anchor="middle" font-size="12">2</text>
<text x="110" y="226" text-anchor="middle" font-size="12">3</text>
<text x="200" y="226" text-anchor="middle" font-size="12">1</text>
<text x="240" y="226" text-anchor="middle" font-size="12">2</text>
<text x="280" y="226" text-anchor="middle" font-size="12">3</text>
</g>
</svg>
</div>

**Seguimiento de las hebras.** Se llaman \\(a\\), \\(b\\), \\(c\\) las hebras que empiezan en las posiciones 1, 2, 3.

- En \\(\sigma\_1 \sigma\_2 \sigma\_1\\): \\(a\\) pasa sobre \\(b\\), luego sobre \\(c\\), y termina en la posición 3. Después \\(b\\), que ahora está en la posición 1, pasa sobre \\(c\\). El resultado: \\(a\\) termina en 3, \\(b\\) en 2 y \\(c\\) en 1.
- En \\(\sigma\_2 \sigma\_1 \sigma\_2\\): \\(b\\) pasa sobre \\(c\\); luego \\(a\\) pasa sobre \\(c\\); luego \\(a\\) pasa sobre \\(b\\). Las posiciones finales son las mismas.

En ambas trenzas, cada par de hebras se cruza exactamente una vez. En cada cruce pasa por encima la hebra que empezó más a la izquierda: \\(a\\) sobre \\(b\\), \\(a\\) sobre \\(c\\) y \\(b\\) sobre \\(c\\).

**La isotopía.** Esto permite colocar cada hebra en su propio "piso": \\(a\\) en el plano más cercano al observador, \\(b\\) en el intermedio y \\(c\\) en el más lejano, todos paralelos al plano del dibujo. Esta asignación es compatible con los tres cruces, porque en cada uno pasa por encima la hebra del piso más cercano. Dentro de su piso, cada hebra es una curva monótona en la altura que une su posición inicial con la final. Hebras en pisos distintos nunca se tocan. Cualquier deformación de cada hebra dentro de su piso, con extremos fijos y altura monótona, es una isotopía de trenzas. Las dos trenzas son de esta forma, con las mismas posiciones inicial y final de cada hebra. La deformación lineal de cada hebra en su piso lleva una en la otra. Visualmente, la hebra \\(a\\), que está arriba de todo, se desliza por encima del cruce entre \\(b\\) y \\(c\\): **es el tercer movimiento de Reidemeister.** \\(\blacksquare\\)

En términos algebraicos, la igualdad es la Proposición 13.2 en la categoría de trenzas, con \\(A = B = C = 1\\).

---

### Ejercicio 5

*La dimensión de \\(k^n\\) con la fórmula del Ejemplo 12.11.*

Sea \\(e\_1, \dots, e\_n\\) la base canónica, con base dual \\(e^1, \dots, e^n\\). La traza de \\(1\_V\\) es el compuesto \\(\mathrm{ev} \circ s \circ (1 \otimes 1) \circ \mathrm{coev}\colon k \to k\\). En \\(1 \in k\\):

\\[
1 \quad\mapsto\quad \sum\_{i=1}^n e\_i \otimes e^i \quad\mapsto\quad \sum\_{i=1}^n e^i \otimes e\_i \quad\mapsto\quad \sum\_{i=1}^n e^i(e\_i) = \sum\_{i=1}^n 1 = n \cdot 1\_k.
\\]

Luego \\(\dim(k^n) = n \cdot 1\_k\\). \\(\blacksquare\\)

La dimensión categórica es un **elemento del campo**, no un número natural. En característica \\(p\\), el espacio \\(k^p\\) tiene dimensión categórica \\(0\\). Con esa salvedad, la solución seleccionada del final de la Parte VI es correcta. El mismo cálculo con \\(f\\) en lugar de \\(1\_V\\) da \\(\sum\_i e^i(f(e\_i)) = \sum\_i f\_{ii}\\): la traza usual de la matriz de \\(f\\).

---

## Nivel 2

### Ejercicio 6

*Un monoide en \\((\mathbf{Ab}, \otimes, \mathbb{Z})\\) es lo mismo que un anillo.*

**La propiedad que se usa.** El producto tensorial \\(A \otimes B\\) de grupos abelianos viene con una función bilineal \\(A \times B \to A \otimes B\\), \\((a, b) \mapsto a \otimes b\\), que es **universal**. Para toda función bilineal \\(\beta\colon A \times B \to C\\) existe un único homomorfismo \\(\hat\beta\colon A \otimes B \to C\\) con \\(\hat\beta(a \otimes b) = \beta(a, b)\\). En particular, los tensores puros \\(a \otimes b\\) generan \\(A \otimes B\\). Así, dos homomorfismos que salen de \\(A \otimes B\\) y coinciden en ellos son iguales. Lo mismo vale para \\((A \otimes B) \otimes C\\) y los elementos \\((a \otimes b) \otimes c\\). Los isomorfismos estructurales son \\(\alpha((a \otimes b) \otimes c) = a \otimes (b \otimes c)\\), \\(\lambda(n \otimes a) = na\\) y \\(\rho(a \otimes n) = na\\).

**De monoide a anillo.** Sea \\((R, m, e)\\) un monoide en \\(\mathbf{Ab}\\). Se define \\(ab = m(a \otimes b)\\) y \\(1\_R = e(1)\\). La multiplicación es bilineal, porque \\(m\\) es aditiva y \\(\otimes\\) es bilineal: esto da las dos leyes distributivas. Al evaluar los axiomas de la Definición 12.4 en generadores:

\\[
m(m \otimes 1)((a \otimes b) \otimes c) = (ab)c, \qquad m(1 \otimes m)\alpha((a \otimes b) \otimes c) = a(bc),
\\]

\\[
m(e \otimes 1)(n \otimes a) = (n 1\_R) a = n(1\_R a), \qquad \lambda(n \otimes a) = na.
\\]

Así, la asociatividad del monoide da \\((ab)c = a(bc)\\). La ley \\(m \circ (e \otimes 1) = \lambda\\) en \\(n = 1\\) da \\(1\_R a = a\\). Del mismo modo, \\(m \circ (1 \otimes e) = \rho\\) da \\(a 1\_R = a\\). Luego \\(R\\) es un anillo (asociativo, con unidad, no necesariamente conmutativo).

**De anillo a monoide.** Si \\(R\\) es un anillo, la multiplicación \\(R \times R \to R\\) es bilineal. Por la propiedad universal define \\(m\colon R \otimes R \to R\\) con \\(m(a \otimes b) = ab\\). Se define \\(e\colon \mathbb{Z} \to R\\) por \\(e(n) = n 1\_R\\). Los axiomas de monoide son igualdades entre homomorfismos que salen de \\((R \otimes R) \otimes R\\), \\(\mathbb{Z} \otimes R\\) y \\(R \otimes \mathbb{Z}\\). Por las cuentas anteriores, coinciden en los generadores, así que se cumplen.

Las dos construcciones son mutuamente inversas: \\(m\\) está determinada por sus valores \\(m(a \otimes b)\\), y \\(e\\) por \\(e(1)\\). Además, un homomorfismo de monoides \\(h\colon R \to S\\) en \\(\mathbf{Ab}\\), es decir, uno con \\(h \circ m = m \circ (h \otimes h)\\) y \\(h \circ e = e\\), es exactamente un homomorfismo de anillos. \\(\blacksquare\\)

**Idea clave:** la bilinealidad de la multiplicación se traduce, por la propiedad universal del producto tensorial, en que la multiplicación sea una sola flecha \\(R \otimes R \to R\\) de \\(\mathbf{Ab}\\).

---

### Ejercicio 7

*En una categoría monoidal simétrica, \\(\mathrm{tr}(g \circ f) = \mathrm{tr}(f \circ g)\\) para \\(f\colon A \to B\\) y \\(g\colon B \to A\\), con \\(A\\) y \\(B\\) dualizables.*

Se omiten asociadores y unitores (Teorema 12.2). Para \\(h\colon A \to A\\), la traza del Ejemplo 12.11 es

\\[
\mathrm{tr}(h) = \mathrm{ev}\_A \circ s\_{A, A^{\ast}} \circ (h \otimes 1\_{A^{\ast}}) \circ \mathrm{coev}\_A.
\\]

**La idea en diagramas de cuerdas.** \\(\mathrm{tr}(g \circ f)\\) es un lazo cerrado sobre el que están las cajas \\(f\\) y, encima, \\(g\\). El lazo sube por la cuerda \\(A\\), pasa por \\(f\\), sigue como cuerda \\(B\\), pasa por \\(g\\), vuelve a ser \\(A\\) y se cierra con la tapa \\(\mathrm{ev}\\) y la copa \\(\mathrm{coev}\\), con un cruce \\(s\\) entre ellas. La caja \\(g\\) se desliza a lo largo del lazo: pasa por la tapa, baja por la cuerda dual (donde se convierte en su **transpuesta** \\(g^{\ast}\\)), cruza por \\(s\\), pasa por la copa y reaparece **debajo** de \\(f\\). El dibujo resultante es \\(\mathrm{tr}(f \circ g)\\). Cada paso del deslizamiento es una igualdad entre flechas. Se demuestran a continuación.

**La transpuesta.** Para \\(g\colon B \to A\\) se define \\(g^{\ast}\colon A^{\ast} \to B^{\ast}\\) como

\\[
g^{\ast} = (\mathrm{ev}\_A \otimes 1\_{B^{\ast}}) \circ (1\_{A^{\ast}} \otimes g \otimes 1\_{B^{\ast}}) \circ (1\_{A^{\ast}} \otimes \mathrm{coev}\_B).
\\]

En el dibujo, es la caja \\(g\\) con una copa debajo a la derecha y una tapa encima a la izquierda: una cuerda en zigzag que atraviesa \\(g\\) al revés.

**Lema (deslizar por la tapa).** \\(\mathrm{ev}\_A \circ (1\_{A^{\ast}} \otimes g) = \mathrm{ev}\_B \circ (g^{\ast} \otimes 1\_B)\colon A^{\ast} \otimes B \to I\\).

*Prueba.* Se sustituye \\(g^{\ast}\\). Como \\(\mathrm{ev}\_B \circ (\mathrm{ev}\_A \otimes 1\_{B^{\ast}} \otimes 1\_B) = \mathrm{ev}\_A \circ (1\_{A^{\ast}} \otimes 1\_A \otimes \mathrm{ev}\_B)\\) (ambos son \\(\mathrm{ev}\_A \otimes \mathrm{ev}\_B\\)), y por la ley de intercambio,

\\[
\mathrm{ev}\_B \circ (g^{\ast} \otimes 1\_B) = \mathrm{ev}\_A \circ (1\_{A^{\ast}} \otimes g) \circ \Big(1\_{A^{\ast}} \otimes \big[(1\_B \otimes \mathrm{ev}\_B) \circ (\mathrm{coev}\_B \otimes 1\_B)\big]\Big) = \mathrm{ev}\_A \circ (1\_{A^{\ast}} \otimes g),
\\]

por la primera identidad del zigzag para \\(B\\) (Definición 12.10). \\(\square\\)

**Lema (deslizar por la copa).** \\((1\_A \otimes g^{\ast}) \circ \mathrm{coev}\_A = (g \otimes 1\_{B^{\ast}}) \circ \mathrm{coev}\_B\colon I \to A \otimes B^{\ast}\\).

*Prueba.* Se sustituye \\(g^{\ast}\\). Por la ley de intercambio, \\((1 \otimes 1 \otimes \mathrm{coev}\_B) \circ \mathrm{coev}\_A = \mathrm{coev}\_A \otimes \mathrm{coev}\_B = (\mathrm{coev}\_A \otimes 1 \otimes 1) \circ \mathrm{coev}\_B\\), y la caja \\(g\\) conmuta con \\(\mathrm{coev}\_A\\) del mismo modo. Así,

\\[
(1\_A \otimes g^{\ast}) \circ \mathrm{coev}\_A = \Big(\big[(1\_A \otimes \mathrm{ev}\_A) \circ (\mathrm{coev}\_A \otimes 1\_A)\big] \otimes 1\_{B^{\ast}}\Big) \circ (g \otimes 1\_{B^{\ast}}) \circ \mathrm{coev}\_B = (g \otimes 1\_{B^{\ast}}) \circ \mathrm{coev}\_B,
\\]

por la primera identidad del zigzag para \\(A\\). \\(\square\\)

**La cuenta.** Se parte de \\(\mathrm{tr}(g \circ f) = \mathrm{ev}\_A \circ s\_{A,A^{\ast}} \circ (g \otimes 1) \circ (f \otimes 1) \circ \mathrm{coev}\_A\\).

1. Por la naturalidad de \\(s\\), \\(s\_{A,A^{\ast}} \circ (g \otimes 1\_{A^{\ast}}) = (1\_{A^{\ast}} \otimes g) \circ s\_{B,A^{\ast}}\\).
2. Por el lema de la tapa, \\(\mathrm{ev}\_A \circ (1\_{A^{\ast}} \otimes g) = \mathrm{ev}\_B \circ (g^{\ast} \otimes 1\_B)\\).
3. Por la naturalidad de \\(s\\), \\((g^{\ast} \otimes 1\_B) \circ s\_{B,A^{\ast}} = s\_{B,B^{\ast}} \circ (1\_B \otimes g^{\ast})\\).
4. Por la ley de intercambio, \\((1\_B \otimes g^{\ast}) \circ (f \otimes 1\_{A^{\ast}}) = (f \otimes 1\_{B^{\ast}}) \circ (1\_A \otimes g^{\ast})\\).
5. Por el lema de la copa, \\((1\_A \otimes g^{\ast}) \circ \mathrm{coev}\_A = (g \otimes 1\_{B^{\ast}}) \circ \mathrm{coev}\_B\\).

Al encadenar los cinco pasos:

\\[
\mathrm{tr}(g \circ f) = \mathrm{ev}\_B \circ s\_{B,B^{\ast}} \circ (f \otimes 1\_{B^{\ast}}) \circ (g \otimes 1\_{B^{\ast}}) \circ \mathrm{coev}\_B = \mathrm{tr}(f \circ g). \qquad \blacksquare
\\]

La simetría solo se usó a través de la naturalidad de \\(s\\). La ecuación \\(s \circ s = 1\\) no hizo falta. Por eso la misma cuenta funciona en una categoría trenzada, con \\(c\\) en lugar de \\(s\\). En ese caso el lazo de la traza tiene un cruce consigo mismo (un rizo), lo que anticipa la corrección por el marco del Capítulo 13.

**Idea clave:** una caja se puede deslizar alrededor de un lazo cerrado; al pasar por la parte que baja, se convierte en su transpuesta.

---

### Ejercicio 8

*La matriz \\(R(e\_i \otimes e\_j) = q^{[i = j]}\\, e\_j \otimes e\_i\\) en \\(V = k^2\\): Yang–Baxter, representación de \\(B\_3\\) y si \\(R^2 \neq 1\\).*

Aquí \\([i = j]\\) vale 1 si \\(i = j\\) y 0 si no. Así, \\(R = s \circ D\\), con \\(s\\) el intercambio y \\(D(e\_i \otimes e\_j) = q^{[i=j]}\\, e\_i \otimes e\_j\\) diagonal.

**Yang–Baxter: sí.** Cada aplicación de \\(R \otimes 1\\) o de \\(1 \otimes R\\) intercambia dos índices adyacentes y multiplica por \\(q\\) si son iguales. Sobre \\(e\_i \otimes e\_j \otimes e\_k\\), leyendo de derecha a izquierda:

- \\((R \otimes 1)(1 \otimes R)(R \otimes 1)\\): compara \\(i, j\\) y da \\((j, i, k)\\); compara \\(i, k\\) y da \\((j, k, i)\\); compara \\(j, k\\) y da \\((k, j, i)\\).
- \\((1 \otimes R)(R \otimes 1)(1 \otimes R)\\): compara \\(j, k\\) y da \\((i, k, j)\\); compara \\(i, k\\) y da \\((k, i, j)\\); compara \\(i, j\\) y da \\((k, j, i)\\).

Ambos lados envían \\(e\_i \otimes e\_j \otimes e\_k\\) a

\\[
q^{[i=j] + [i=k] + [j=k]}\\; e\_k \otimes e\_j \otimes e\_i,
\\]

porque cada lado compara una vez cada par de índices. Como coinciden en una base, son iguales. El argumento vale para cualquier \\(R = s \circ D\\) con \\(D\\) diagonal y de pesos no nulos. \\(R\\) es invertible porque \\(q \neq 0\\): \\(R^{-1}(e\_i \otimes e\_j) = q^{-[i=j]}\\, e\_j \otimes e\_i\\).

**La representación de \\(B\_3\\).** Como \\(B\_3\\) tiene la sola relación \\(\sigma\_1 \sigma\_2 \sigma\_1 = \sigma\_2 \sigma\_1 \sigma\_2\\) (no hay índices con \\(|i - j| \ge 2\\)), la ecuación de Yang–Baxter y la invertibilidad de \\(R\\) dan un homomorfismo

\\[
\rho\colon B\_3 \to GL(V \otimes V \otimes V) \cong GL\_8(k), \qquad \rho(\sigma\_1) = R \otimes 1, \quad \rho(\sigma\_2) = 1 \otimes R,
\\]

como en el Corolario 13.6. Las dos matrices permutan los índices de la base, así que conservan el **contenido** (cuántos índices valen 1 y cuántos 2). Por lo tanto, \\(V^{\otimes 3}\\) se descompone en subespacios invariantes:

- \\(\langle e\_1 \otimes e\_1 \otimes e\_1 \rangle\\) y \\(\langle e\_2 \otimes e\_2 \otimes e\_2 \rangle\\): en cada uno, \\(\sigma\_1\\) y \\(\sigma\_2\\) actúan por \\(q\\);
- el subespacio de contenido \\(\\{1,1,2\\}\\), con base \\(e\_1 e\_1 e\_2,\\ e\_1 e\_2 e\_1,\\ e\_2 e\_1 e\_1\\) (omitiendo los \\(\otimes\\)), donde
\\[
\rho(\sigma\_1) = \begin{pmatrix} q & 0 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 1 & 0 \end{pmatrix}, \qquad \rho(\sigma\_2) = \begin{pmatrix} 0 & 1 & 0 \\\\ 1 & 0 & 0 \\\\ 0 & 0 & q \end{pmatrix};
\\]
- el subespacio de contenido \\(\\{1,2,2\\}\\), con las mismas matrices después de intercambiar los papeles de \\(e\_1\\) y \\(e\_2\\).

Es una representación **monomial**: cada trenza permuta las "palabras" \\(e\_{i\_1} e\_{i\_2} e\_{i\_3}\\) y las multiplica por una potencia de \\(q\\).

**¿Genuinamente trenzada?** \\(R^2(e\_i \otimes e\_i) = q^2\\, e\_i \otimes e\_i\\), y \\(R^2(e\_i \otimes e\_j) = e\_i \otimes e\_j\\) si \\(i \neq j\\). Luego \\(R^2 = 1\\) si y solo si \\(q^2 = 1\\). Para \\(q = 1\\), \\(R = s\\). Para \\(q = -1\\), \\(R \neq s\\) pero \\(R^2 = 1\\), y la representación se factoriza por \\(S\_3\\). Para \\(q \neq \pm 1\\), \\(R^2 \neq 1\\), así que \\(\rho(\sigma\_1^2) \neq 1\\) y la representación **no** se factoriza por el grupo simétrico \\(S\_3\\). En ese sentido es genuinamente trenzada. Los valores propios de \\(R\\) son \\(q\\) (doble, en \\(e\_1 \otimes e\_1\\) y \\(e\_2 \otimes e\_2\\)), \\(1\\) y \\(-1\\) (en \\(e\_1 \otimes e\_2 \pm e\_2 \otimes e\_1\\)). \\(\blacksquare\\)

Esta representación es de todos modos pobre para la teoría de nudos. Una trenza pura actúa por un escalar en cada palabra, de modo que \\(\rho\\) restringida a las trenzas puras es abeliana: solo "ve" cuántas veces se enroscan entre sí hebras con el mismo índice. Para obtener el polinomio de Jones hace falta una matriz R no monomial, como la de \\(U\_q(\mathfrak{sl}\_2)\\).

---

### Ejercicio 9

*Corchete de Kauffman y \\(X\\) del enlace de Hopf; comparación con dos círculos separados.*

**Convenciones.** Son las del Capítulo 13:

- \\(\langle \bigcirc \rangle = 1\\) y \\(\langle D \sqcup \bigcirc \rangle = \delta \langle D \rangle\\), con \\(\delta = -A^2 - A^{-2}\\). Por lo tanto, un **estado** (una elección de suavizado en cada cruce) con \\(a\\) suavizados de tipo A, \\(b\\) de tipo B y \\(k\\) círculos aporta \\(A^{a-b} \delta^{k-1}\\).
- El suavizado A une las dos regiones que barre la hebra superior al girar en sentido antihorario hasta la inferior. Para el cruce \\(\sigma\_1\\) (la hebra de la izquierda pasa por encima, Definición 13.3), esas regiones son la de arriba y la de abajo. Así, el suavizado A de \\(\sigma\_1\\) es el de **dos hebras paralelas** (la identidad), y el suavizado B es \\(e = \mathrm{coev} \circ \mathrm{ev}\\). Es la regla del Capítulo 13: \\(\sigma\_1 \mapsto A \cdot 1 + A^{-1} e\\).
- **Torsión:** un cruce orientado tiene signo \\(+1\\) si, con las dos hebras subiendo, la superior va de abajo a la izquierda hacia arriba a la derecha (cruce "derecho"). Tiene signo \\(-1\\) en el caso contrario. Así, \\(\sigma\_1\\) con las dos hebras hacia arriba tiene signo \\(+1\\). Con esta convención, \\(X(L) = (-A^3)^{-w(D)} \langle D \rangle\\) es invariante bajo el primer movimiento: un rizo positivo tiene corchete \\(-A^3\\) y torsión \\(+1\\), así que \\(X = 1\\).

**El diagrama.** El diagrama estándar del enlace de Hopf es la cerradura de la trenza \\(\sigma\_1^2\\): dos hebras que se cruzan dos veces, con los extremos superiores unidos a los inferiores por arcos exteriores. En un estado, cada cruce se reemplaza por \\(1\\) (suavizado A) o por \\(e\\) (suavizado B), y se cierra. La cerradura de \\(1\\) en dos hebras son dos círculos. Como \\(e \circ e = \delta\\, e\\) (en \\(e \circ e\\) aparece un círculo interior), la cerradura de \\(e^j\\) consta de \\(j - 1\\) círculos interiores más la cerradura de \\(e\\), que es un círculo. En total, \\(j\\) círculos.

| Estado | Peso | Círculos | Contribución |
| :--- | :--- | :--- | :--- |
| AA | \\(A^{2}\\) | 2 | \\(A^{2} \delta\\) |
| AB | \\(A^{0}\\) | 1 | \\(1\\) |
| BA | \\(A^{0}\\) | 1 | \\(1\\) |
| BB | \\(A^{-2}\\) | 2 | \\(A^{-2} \delta\\) |

\\[
\langle \text{Hopf} \rangle = A^2 \delta + 2 + A^{-2} \delta = (-A^4 - 1) + 2 + (-1 - A^{-4}) = -A^4 - A^{-4}.
\\]

**La torsión y \\(X\\).** Si las dos componentes se orientan hacia arriba en la trenza, los dos cruces son \\(\sigma\_1\\) con signo \\(+1\\), y \\(w = 2\\):

\\[
X(\text{Hopf}^{+}) = (-A^3)^{-2} (-A^4 - A^{-4}) = -A^{-2} - A^{-10}.
\\]

Si se invierte la orientación de una componente, en cada cruce cambia el sentido de exactamente una hebra, así que cambia el signo. Entonces \\(w = -2\\) y

\\[
X(\text{Hopf}^{-}) = (-A^3)^{2} (-A^4 - A^{-4}) = -A^{2} - A^{10}.
\\]

Con \\(A = t^{-1/4}\\), estos valores son \\(V = -t^{1/2} - t^{5/2}\\) y \\(V = -t^{-1/2} - t^{-5/2}\\), respectivamente.

**Comparación.** El diagrama de dos círculos separados no tiene cruces: tiene un solo estado, con dos círculos, así que \\(\langle \bigcirc \sqcup \bigcirc \rangle = \delta = -A^2 - A^{-2}\\). Su torsión es \\(0\\), y \\(X = \delta\\). Como \\(X\\) es un invariante de enlaces orientados, y \\(-A^{-2} - A^{-10}\\) y \\(-A^2 - A^{10}\\) son distintos de \\(-A^2 - A^{-2}\\), **el enlace de Hopf no es isotópico al enlace trivial de dos componentes, con ninguna orientación**. \\(\blacksquare\\)

Hay que comparar \\(X\\), no \\(\langle \cdot \rangle\\). El corchete por sí solo depende del diagrama: cambia por un factor \\(-A^{\pm 3}\\) con cada rizo.

La guía del final de la Parte VI es correcta: los valores \\(\langle \text{Hopf} \rangle = -A^4 - A^{-4}\\), \\(X = -A^{-2} - A^{-10}\\) para \\(w = 2\\) y \\(X = -A^{2} - A^{10}\\) para \\(w = -2\\) coinciden con los de esta solución. Todos los polinomios de los Ejercicios 9 y 10 se verificaron además con un programa que enumera los \\(2^n\\) estados a partir de un código del diagrama. El mismo programa confirmó que un rizo de cualquier signo da \\(X = 1\\).

---

### Ejercicio 10

*Corchete de Kauffman del trébol con tres cruces; \\(X\\) distingue el trébol de su imagen especular.*

**El diagrama.** El diagrama estándar del trébol, con tres cruces, es la cerradura de la trenza \\(\sigma\_1^3\\). Las convenciones son las del Ejercicio 9. Un estado con \\(j \ge 1\\) suavizados de tipo B tiene \\(j\\) círculos, y el estado AAA tiene \\(2\\).

| Estados | Número | Peso | Círculos | Contribución total |
| :--- | :--- | :--- | :--- | :--- |
| AAA | 1 | \\(A^{3}\\) | 2 | \\(A^{3} \delta\\) |
| AAB, ABA, BAA | 3 | \\(A^{1}\\) | 1 | \\(3A\\) |
| ABB, BAB, BBA | 3 | \\(A^{-1}\\) | 2 | \\(3A^{-1} \delta\\) |
| BBB | 1 | \\(A^{-3}\\) | 3 | \\(A^{-3} \delta^2\\) |

Con \\(\delta = -A^2 - A^{-2}\\) y \\(\delta^2 = A^4 + 2 + A^{-4}\\):

\\[
\begin{aligned}
\langle D \rangle &= A^3 \delta + 3A + 3A^{-1} \delta + A^{-3} \delta^2 \\\\
&= (-A^5 - A) + 3A + (-3A - 3A^{-3}) + (A + 2A^{-3} + A^{-7}) \\\\
&= -A^5 - A^{-3} + A^{-7}.
\end{aligned}
\\]

**La torsión.** El trébol es un nudo. Invertir su orientación invierte las dos hebras en cada cruce, y eso no cambia el signo. Con las dos hebras de la trenza hacia arriba, los tres cruces son \\(\sigma\_1\\), de signo \\(+1\\). Luego \\(w(D) = 3\\) con cualquier orientación, y

\\[
X(K) = (-A^3)^{-3} \langle D \rangle = -A^{-9}\big(-A^5 - A^{-3} + A^{-7}\big) = A^{-4} + A^{-12} - A^{-16}.
\\]

Con \\(A = t^{-1/4}\\) se obtiene \\(V\_K(t) = t + t^3 - t^4\\), el polinomio de Jones del trébol **derecho**, que es el que se obtuvo aquí.

**La imagen especular.** La imagen especular \\(D^{\ast}\\) se obtiene al cambiar cada cruce: es la cerradura de \\(\sigma\_1^{-3}\\). Al cambiar un cruce, las regiones A pasan a ser las B; en la regla de Temperley–Lieb, \\(\sigma\_1^{-1} \mapsto A^{-1} \cdot 1 + A\\, e\\). Por eso, en general,

\\[
\langle D^{\ast} \rangle(A) = \langle D \rangle(A^{-1}), \qquad w(D^{\ast}) = -w(D), \qquad X(K^{\ast})(A) = X(K)(A^{-1}).
\\]

Aquí:

\\[
\langle D^{\ast} \rangle = A^{7} - A^{3} - A^{-5}, \qquad w(D^{\ast}) = -3, \qquad X(K^{\ast}) = (-A^3)^{3} \langle D^{\ast} \rangle = A^{4} + A^{12} - A^{16}.
\\]

**Distinción.** \\(X(K) = A^{-4} + A^{-12} - A^{-16}\\) y \\(X(K^{\ast}) = A^{4} + A^{12} - A^{16}\\) son polinomios de Laurent distintos: el primero solo tiene potencias negativas y el segundo solo positivas. Como \\(X\\) es un invariante de isotopía (Capítulo 13) y, para nudos, no depende de la orientación, **el trébol no es isotópico a su imagen especular**: es un nudo quiral. \\(\blacksquare\\)

El valor de \\(\langle D \rangle\\), la torsión, los dos valores de \\(X\\) y su desigualdad se verificaron con el programa de enumeración de estados mencionado en el Ejercicio 9. La convención de signo usada es la de la mano derecha descrita en el Ejercicio 9. Con la convención opuesta, el trébol y su imagen intercambiarían sus valores de \\(X\\), pero seguirían siendo distintos.

**Idea clave:** el espejo cambia \\(A\\) por \\(A^{-1}\\). Un enlace cuyo \\(X\\) no es simétrico bajo ese cambio es necesariamente quiral. (El recíproco es falso: hay nudos quirales con \\(X\\) simétrico.)
