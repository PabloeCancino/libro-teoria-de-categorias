# Soluciones de la Parte I

Soluciones completas de los ejercicios de nivel 1 y nivel 2 de la Parte I (Capítulos 1 a 3). Conviene intentar cada ejercicio antes de leer su solución.

---

## Nivel 1

### Ejercicio 1

*Verificar que \\(\mathbf{Rel}\\) es una categoría.*

Hay que comprobar tres cosas: que la composición está bien definida, que es asociativa y que la diagonal es neutra.

**Composición bien definida.** Si \\(R \subseteq A \times B\\) y \\(S \subseteq B \times C\\), la fórmula del Ejemplo 1.3 define un subconjunto de \\(A \times C\\), es decir, una flecha \\(A \to C\\).

**Asociatividad.** Sean \\(R\colon A \to B\\), \\(S\colon B \to C\\) y \\(T\colon C \to D\\). Para \\((a, d) \in A \times D\\):

\\[
(a,d) \in T \circ (S \circ R) \iff \exists c \in C, \ (a,c) \in S \circ R \text{ y } (c,d) \in T \iff \exists c \ \exists b, \ (a,b) \in R, \ (b,c) \in S, \ (c,d) \in T.
\\]

Del mismo modo,

\\[
(a,d) \in (T \circ S) \circ R \iff \exists b \in B, \ (a,b) \in R \text{ y } (b,d) \in T \circ S \iff \exists b \ \exists c, \ (a,b) \in R, \ (b,c) \in S, \ (c,d) \in T.
\\]

Las dos condiciones finales son la misma, porque dos cuantificadores existenciales conmutan. Luego \\(T \circ (S \circ R) = (T \circ S) \circ R\\).

**Unidad.** Sea \\(R\colon A \to B\\). Se tiene \\((a,b) \in R \circ \Delta\_A\\) si y solo si existe \\(a'\\) con \\((a, a') \in \Delta\_A\\) y \\((a', b) \in R\\). La primera condición fuerza \\(a' = a\\), así que la condición equivale a \\((a,b) \in R\\). Luego \\(R \circ \Delta\_A = R\\). De manera simétrica, \\((a,b) \in \Delta\_B \circ R\\) si y solo si existe \\(b'\\) con \\((a,b') \in R\\) y \\(b' = b\\), es decir, si y solo si \\((a,b) \in R\\). Luego \\(\Delta\_B \circ R = R\\). \\(\blacksquare\\)

**Idea clave:** la asociatividad de \\(\mathbf{Rel}\\) es la conmutatividad de los cuantificadores existenciales.

---

### Ejercicio 2

*En un preorden, \\(x \cong y\\) si y solo si \\(x \le y\\) y \\(y \le x\\); en un orden parcial los únicos isomorfismos son identidades.*

Si \\(x \cong y\\), existen flechas \\(x \to y\\) e \\(y \to x\\), es decir, \\(x \le y\\) y \\(y \le x\\).

Recíprocamente, supongamos \\(x \le y\\) y \\(y \le x\\), y sean \\(f\colon x \to y\\), \\(g\colon y \to x\\) las flechas correspondientes. Entonces \\(g \circ f\colon x \to x\\) y \\(1\_x\colon x \to x\\) son flechas paralelas. En un preorden hay a lo más una flecha \\(x \to x\\), así que \\(g \circ f = 1\_x\\). Del mismo modo, \\(f \circ g = 1\_y\\). Luego \\(f\\) es un isomorfismo.

Sea ahora \\(P\\) un orden parcial y \\(f\colon x \to y\\) un isomorfismo. Por lo anterior, \\(x \le y\\) e \\(y \le x\\), y la antisimetría da \\(x = y\\). Entonces \\(f\\) es una flecha \\(x \to x\\). La única flecha \\(x \to x\\) es \\(1\_x\\), así que \\(f = 1\_x\\). \\(\blacksquare\\)

---

### Ejercicio 3

*En \\(\mathbf{Grp}\\), un homomorfismo es monomorfismo si y solo si es inyectivo.*

Sea \\(f\colon G \to H\\) un homomorfismo.

**Inyectivo implica monomorfismo.** Sean \\(g, h\colon K \to G\\) homomorfismos con \\(f \circ g = f \circ h\\). Para todo \\(k \in K\\), \\(f(g(k)) = f(h(k))\\), y la inyectividad da \\(g(k) = h(k)\\). Así, \\(g\\) y \\(h\\) tienen la misma función subyacente. Dos homomorfismos con la misma función subyacente son iguales (el funtor olvidadizo es fiel, Ejemplo 2.14), luego \\(g = h\\).

**Monomorfismo implica inyectivo.** Primero, un hecho sobre \\(\mathbb{Z}\\). Para cada \\(a \in G\\), la función \\(\bar{a}\colon \mathbb{Z} \to G\\), \\(n \mapsto a^n\\), es un homomorfismo, porque \\(a^{m+n} = a^m a^n\\). Además es el único homomorfismo \\(\mathbb{Z} \to G\\) que envía \\(1\\) en \\(a\\): un homomorfismo \\(u\\) con \\(u(1) = a\\) cumple \\(u(n) = u(1 + \dots + 1) = a^n\\) para \\(n \gt 0\\), \\(u(0) = e\\) y \\(u(-n) = u(n)^{-1}\\).

Supongamos ahora que \\(f\\) es monomorfismo y que \\(f(a) = f(a')\\). Los homomorfismos \\(f \circ \bar{a}\\) y \\(f \circ \bar{a'}\\) envían \\(1\\) en \\(f(a) = f(a')\\). Por la unicidad recién probada, aplicada en \\(H\\), \\(f \circ \bar{a} = f \circ \bar{a'}\\). Como \\(f\\) es monomorfismo, \\(\bar{a} = \bar{a'}\\), y al evaluar en \\(1\\) se obtiene \\(a = a'\\). \\(\blacksquare\\)

*Otra prueba.* Sea \\(N = \ker f\\), con la inclusión \\(j\colon N \to G\\) y el homomorfismo trivial \\(e\colon N \to G\\). Ambos cumplen \\(f \circ j = f \circ e\\), porque los dos son triviales. Si \\(f\\) es monomorfismo, \\(j = e\\), es decir, \\(N = \\{e\\}\\), y \\(f\\) es inyectivo.

La solución seleccionada del archivo de ejercicios es correcta; aquí se añadió la verificación de que \\(n \mapsto a^n\\) es el único homomorfismo con \\(1 \mapsto a\\).

**Idea clave:** \\(\mathbb{Z}\\) desempeña en \\(\mathbf{Grp}\\) el papel de \\(\\{\star\\}\\) en \\(\mathbf{Set}\\): los homomorfismos \\(\mathbb{Z} \to G\\) son los elementos de \\(G\\).

---

### Ejercicio 4

*La potencia contravariante cumple \\(\mathcal{P}^{-}(g \circ f) = \mathcal{P}^{-}(f) \circ \mathcal{P}^{-}(g)\\).*

Sean \\(f\colon X \to Y\\) y \\(g\colon Y \to Z\\). Ambos lados son funciones \\(\mathcal{P}(Z) \to \mathcal{P}(X)\\). Sea \\(T \subseteq Z\\) y \\(x \in X\\). Entonces

\\[
x \in (g \circ f)^{-1}(T) \iff g(f(x)) \in T \iff f(x) \in g^{-1}(T) \iff x \in f^{-1}\big(g^{-1}(T)\big).
\\]

Luego \\(\mathcal{P}^{-}(g \circ f)(T) = \mathcal{P}^{-}(f)\big(\mathcal{P}^{-}(g)(T)\big)\\) para todo \\(T\\). Además, \\(1\_X^{-1}(S) = S\\), así que \\(\mathcal{P}^{-}(1\_X) = 1\_{\mathcal{P}(X)}\\). Con ambas propiedades, \\(\mathcal{P}^{-}\\) es un funtor \\(\mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}\\) (Definición 2.10). \\(\blacksquare\\)

---

### Ejercicio 5

*Entre funciones monótonas \\(f, g\colon P \to Q\\) hay a lo más una transformación natural \\(f \Rightarrow g\\), y la hay si y solo si \\(f(x) \le g(x)\\) para todo \\(x\\).*

Por el Ejemplo 2.7, \\(f\\) y \\(g\\) son funtores. Una transformación natural \\(\alpha\colon f \Rightarrow g\\) es una familia de flechas \\(\alpha\_x\colon f(x) \to g(x)\\) de \\(Q\\) que hace conmutar los cuadrados de naturalidad.

**A lo más una.** Para cada \\(x\\), entre \\(f(x)\\) y \\(g(x)\\) hay a lo más una flecha en \\(Q\\). Luego dos transformaciones \\(\alpha, \beta\colon f \Rightarrow g\\) tienen las mismas componentes, y \\(\alpha = \beta\\).

**Existencia.** Si existe \\(\alpha\\), su componente \\(\alpha\_x\\) es una flecha \\(f(x) \to g(x)\\), es decir, \\(f(x) \le g(x)\\). Recíprocamente, si \\(f(x) \le g(x)\\) para todo \\(x\\), sea \\(\alpha\_x\\) la única flecha \\(f(x) \to g(x)\\). Para \\(x \le y\\), los dos caminos del cuadrado de naturalidad, \\(g(x \le y) \circ \alpha\_x\\) y \\(\alpha\_y \circ f(x \le y)\\), son flechas \\(f(x) \to g(y)\\). En \\(Q\\) dos flechas paralelas coinciden, así que el cuadrado conmuta. \\(\blacksquare\\)

**Idea clave:** en un preorden todo diagrama conmuta; la naturalidad es gratuita y solo cuenta la existencia de las componentes.

---

## Nivel 2

### Ejercicio 6

*La composición de monomorfismos es monomorfismo; si \\(g \circ f\\) es monomorfismo, \\(f\\) lo es. Enunciar los duales.*

Sean \\(f\colon A \to B\\) y \\(g\colon B \to C\\).

**Composición.** Supongamos que \\(f\\) y \\(g\\) son monomorfismos, y sean \\(u, v\colon X \to A\\) con \\((g \circ f) \circ u = (g \circ f) \circ v\\). Por asociatividad, \\(g \circ (f \circ u) = g \circ (f \circ v)\\). Como \\(g\\) es monomorfismo, \\(f \circ u = f \circ v\\). Como \\(f\\) es monomorfismo, \\(u = v\\).

**Cancelación.** Supongamos que \\(g \circ f\\) es monomorfismo, y sean \\(u, v\colon X \to A\\) con \\(f \circ u = f \circ v\\). Al componer con \\(g\\) por la izquierda, \\((g \circ f) \circ u = (g \circ f) \circ v\\), y entonces \\(u = v\\). Luego \\(f\\) es monomorfismo. \\(\blacksquare\\)

Observe que en la cancelación no se pide nada a \\(g\\). En general \\(g\\) no tiene por qué ser monomorfismo: en \\(\mathbf{Set}\\), con \\(f\colon \\{0\\} \to \\{0,1\\}\\) la inclusión y \\(g\colon \\{0,1\\} \to \\{0\\}\\) la única función, \\(g \circ f = 1\\) es inyectiva y \\(g\\) no lo es.

**Duales.** Un epimorfismo de \\(\mathcal{C}\\) es un monomorfismo de \\(\mathcal{C}^{\mathrm{op}}\\), y \\((g \circ f)^{\mathrm{op}} = f^{\mathrm{op}} \circ g^{\mathrm{op}}\\). Aplicando lo anterior en \\(\mathcal{C}^{\mathrm{op}}\\):

- La composición de epimorfismos es un epimorfismo.
- Si \\(g \circ f\\) es un epimorfismo, entonces \\(g\\) es un epimorfismo.

Note que en el dual el factor que hereda la propiedad es el **último** en actuar, \\(g\\), y no \\(f\\).

---

### Ejercicio 7

*Epimorfismos no sobreyectivos en \\(\mathbf{Top}\\) y en la subcategoría de espacios de Hausdorff.*

**En \\(\mathbf{Top}\\) no existen: los epimorfismos son exactamente las funciones continuas sobreyectivas.**

Si \\(f\colon X \to Y\\) es continua y sobreyectiva, y \\(g \circ f = h \circ f\\) con \\(g, h\colon Y \to Z\\) continuas, entonces \\(g = h\\) como funciones, por la Proposición 1.13. Luego \\(f\\) es epimorfismo.

Recíprocamente, supongamos que \\(f\\) no es sobreyectiva y sea \\(y\_0 \in Y \setminus f(X)\\). Sea \\(S = \\{0, 1\\}\\) con la **topología indiscreta**, cuyos únicos abiertos son \\(\emptyset\\) y \\(S\\). Toda función \\(Y \to S\\) es continua, porque las preimágenes de \\(\emptyset\\) y \\(S\\) son \\(\emptyset\\) e \\(Y\\). Sean \\(g\\) la función constante \\(0\\) y \\(h\\) la función que vale \\(1\\) en \\(y\_0\\) y \\(0\\) en el resto. Ambas son continuas, \\(g \neq h\\) y \\(g \circ f = h \circ f\\), porque \\(y\_0\\) no está en la imagen de \\(f\\). Luego \\(f\\) no es epimorfismo. \\(\blacksquare\\)

El espacio de dos puntos indiscreto hace en \\(\mathbf{Top}\\) el papel que \\(\\{0,1\\}\\) hizo en \\(\mathbf{Set}\\): no impone ninguna restricción de continuidad.

**En la subcategoría plena \\(\mathbf{Haus}\\) de espacios de Hausdorff sí existen: la inclusión \\(i\colon \mathbb{Q} \to \mathbb{R}\\) es un epimorfismo no sobreyectivo.**

La inclusión es continua para la topología de subespacio, y \\(\mathbb{Q}\\) y \\(\mathbb{R}\\) son de Hausdorff. Sean \\(g, h\colon \mathbb{R} \to Y\\) continuas, con \\(Y\\) de Hausdorff, tales que \\(g \circ i = h \circ i\\), es decir, \\(g(q) = h(q)\\) para todo \\(q \in \mathbb{Q}\\).

Sea \\(E = \\{t \in \mathbb{R} \mid g(t) = h(t)\\}\\). Su complemento es abierto. En efecto, si \\(g(t) \neq h(t)\\), hay abiertos disjuntos \\(U \ni g(t)\\) y \\(V \ni h(t)\\), y \\(W = g^{-1}(U) \cap h^{-1}(V)\\) es un abierto que contiene a \\(t\\). Para \\(s \in W\\), \\(g(s) \in U\\) y \\(h(s) \in V\\), luego \\(g(s) \neq h(s)\\). Así, \\(E\\) es cerrado. Como \\(E \supseteq \mathbb{Q}\\) y \\(\mathbb{Q}\\) es denso, \\(E = \mathbb{R}\\), y \\(g = h\\). Luego \\(i\\) es epimorfismo en \\(\mathbf{Haus}\\).

No es sobreyectiva y, por lo tanto, no es isomorfismo. Tampoco es una retracción: si \\(i \circ s = 1\_{\mathbb{R}}\\), \\(i\\) sería sobreyectiva. \\(\blacksquare\\)

El argumento de \\(\mathbf{Top}\\) no se traslada porque el espacio indiscreto de dos puntos no es de Hausdorff. Al reducir la categoría se reducen los objetos de prueba, y con ellos la capacidad de distinguir flechas. En \\(\mathbf{Haus}\\) los epimorfismos son, de hecho, las funciones continuas de imagen densa; aquí solo se demostró la dirección que pide el ejercicio.

**Idea clave:** ser epimorfismo depende de cuántos objetos de prueba hay en la categoría.

---

### Ejercicio 8

*Toda transformación natural \\(\alpha\colon 1\_{\mathbf{Set}} \Rightarrow 1\_{\mathbf{Set}}\\) es la identidad.*

Sea \\(X\\) un conjunto y \\(x \in X\\). Sea \\(\bar{x}\colon \\{\star\\} \to X\\) la función con \\(\bar{x}(\star) = x\\). El cuadrado de naturalidad de \\(\alpha\\) en \\(\bar{x}\\) es

\\[
\require{AMScd}
\begin{CD}
\\{\star\\} @>{\alpha\_{\\{\star\\}}}>> \\{\star\\} \\\\
@V{\bar{x}}VV @VV{\bar{x}}V \\\\
X @>>{\alpha\_X}> X
\end{CD}
\\]

y dice \\(\alpha\_X \circ \bar{x} = \bar{x} \circ \alpha\_{\\{\star\\}}\\). La única función \\(\\{\star\\} \to \\{\star\\}\\) es la identidad, así que \\(\alpha\_{\\{\star\\}} = 1\\). Al evaluar en \\(\star\\):

\\[
\alpha\_X(x) = \alpha\_X(\bar{x}(\star)) = \bar{x}(\alpha\_{\\{\star\\}}(\star)) = \bar{x}(\star) = x.
\\]

Como \\(x\\) y \\(X\\) son arbitrarios, \\(\alpha\_X = 1\_X\\) para todo \\(X\\). \\(\blacksquare\\)

La solución seleccionada del archivo de ejercicios es correcta.

**Idea clave:** una transformación natural con dominio \\(1\_{\mathbf{Set}}\\) está determinada por su componente en \\(\\{\star\\}\\), porque los elementos son flechas desde \\(\\{\star\\}\\). Es un caso particular del lema de Yoneda (Capítulo 5).

---

### Ejercicio 9

*Las transformaciones naturales \\(1\_{\mathbf{B}G} \Rightarrow 1\_{\mathbf{B}G}\\) están en biyección con el centro de \\(G\\).*

La categoría \\(\mathbf{B}G\\) tiene un único objeto \\(\star\\), con \\(\mathbf{B}G(\star, \star) = G\\) y composición \\(g \circ h = gh\\) (Ejemplo 1.6). Una transformación natural \\(\alpha\colon 1 \Rightarrow 1\\) consta de una sola componente \\(\alpha\_\star\colon \star \to \star\\), es decir, de un elemento \\(z \in G\\). Para cada flecha \\(g\colon \star \to \star\\), el cuadrado de naturalidad es

\\[
\require{AMScd}
\begin{CD}
\star @>{z}>> \star \\\\
@V{g}VV @VV{g}V \\\\
\star @>>{z}> \star
\end{CD}
\\]

y dice \\(g \circ z = z \circ g\\), es decir, \\(gz = zg\\).

Por lo tanto, un elemento \\(z \in G\\) es la componente de una transformación natural si y solo si conmuta con todos los elementos de \\(G\\), es decir, si y solo si \\(z \in Z(G)\\). La asignación \\(\alpha \mapsto \alpha\_\star\\) es inyectiva, porque una transformación natural está determinada por sus componentes, y su imagen es \\(Z(G)\\). Es la biyección buscada. \\(\blacksquare\\)

Además, la composición de transformaciones corresponde al producto de \\(G\\): \\((\beta \cdot \alpha)\_\star = \beta\_\star \alpha\_\star\\). La biyección es, entonces, un isomorfismo entre el monoide de transformaciones naturales \\(1 \Rightarrow 1\\) y el grupo \\(Z(G)\\).

La solución seleccionada del archivo de ejercicios es correcta.

---

### Ejercicio 10

*El subgrupo conmutador define un funtor \\(\mathbf{Grp} \to \mathbf{Grp}\\) y las inclusiones \\([G,G] \to G\\) forman una transformación natural.*

Escriba \\([a,b] = aba^{-1}b^{-1}\\). El subgrupo \\([G,G]\\) es el generado por los conmutadores. Como \\([a,b]^{-1} = [b,a]\\), sus elementos son exactamente los productos finitos \\(c\_1 \cdots c\_r\\) de conmutadores (con \\(r = 0\\) para \\(e\\)).

**Acción sobre flechas.** Sea \\(f\colon G \to H\\) un homomorfismo. Entonces

\\[
f([a,b]) = f(a) f(b) f(a)^{-1} f(b)^{-1} = [f(a), f(b)],
\\]

y por lo tanto \\(f(c\_1 \cdots c\_r) = f(c\_1) \cdots f(c\_r)\\) es un producto de conmutadores de \\(H\\). Luego \\(f([G,G]) \subseteq [H,H]\\), y la restricción

\\[
[f]\colon [G,G] \to [H,H], \qquad c \mapsto f(c),
\\]

es un homomorfismo.

**Funtorialidad.** Para \\(f\colon G \to H\\) y \\(g\colon H \to K\\), las funciones \\([g \circ f]\\) y \\([g] \circ [f]\\) envían \\(c\\) en \\(g(f(c))\\), luego son iguales. La restricción de \\(1\_G\\) es \\(1\_{[G,G]}\\). Así, \\(G \mapsto [G,G]\\), \\(f \mapsto [f]\\) es un funtor \\(\mathbf{Grp} \to \mathbf{Grp}\\).

**Naturalidad.** Sea \\(j\_G\colon [G,G] \to G\\) la inclusión. Es una familia de flechas del funtor conmutador en el funtor identidad. Para \\(f\colon G \to H\\), el cuadrado

\\[
\require{AMScd}
\begin{CD}
[G,G] @>{j\_G}>> G \\\\
@V{[f]}VV @VV{f}V \\\\
[H,H] @>>{j\_H}> H
\end{CD}
\\]

conmuta: ambos caminos envían \\(c \in [G,G]\\) en \\(f(c)\\). Luego \\(j\colon [-,-] \Rightarrow 1\_{\mathbf{Grp}}\\) es natural. \\(\blacksquare\\)

Compare con el Ejemplo 2.15. El conmutador se define por una fórmula en los elementos, \\(aba^{-1}b^{-1}\\), que todo homomorfismo respeta. El centro se define por una condición universal, "conmuta con **todo** \\(g \in G\\)", y un homomorfismo no sobreyectivo no ve todos los elementos del codominio. Por eso el primero es funtorial y el segundo no.

**Idea clave:** una construcción definida por fórmulas que los homomorfismos preservan es funtorial; una definida por cuantificación universal sobre el objeto, en general no.
