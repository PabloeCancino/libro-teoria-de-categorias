# Soluciones de la Parte IV

Soluciones completas de los ejercicios de nivel 1 y 2 de los capítulos 8 y 9 (adjunciones, límites y equivalencias). Conviene intentar cada ejercicio antes de leer su solución.

Varios ejercicios usan la versión dual del Teorema 8.10. Se enuncia y se justifica una vez.

**Teorema 8.10 dual.** Un funtor \\(F\colon \mathcal{C} \to \mathcal{D}\\) tiene adjunto derecho si y solo si para cada objeto \\(Y\\) de \\(\mathcal{D}\\) existen un objeto \\(GY\\) de \\(\mathcal{C}\\) y una flecha \\(\varepsilon\_Y\colon F(GY) \to Y\\) tales que para todo \\(X\\) y toda \\(g\colon FX \to Y\\) hay una única \\(h\colon X \to GY\\) con \\(\varepsilon\_Y \circ F(h) = g\\). En tal caso \\(G\\) se extiende de manera única a un funtor con \\(F \dashv G\\) y counidad \\(\varepsilon\\).

*Justificación.* Al escribir \\(F \dashv G\\) en las categorías opuestas, \\(\mathcal{D}(FX, Y) \cong \mathcal{C}(X, GY)\\) se lee \\(\mathcal{D}^{\mathrm{op}}(Y, F^{\mathrm{op}} X) \cong \mathcal{C}^{\mathrm{op}}(G^{\mathrm{op}} Y, X)\\); es decir, \\(F \dashv G\\) equivale a \\(G^{\mathrm{op}} \dashv F^{\mathrm{op}}\\). La condición enunciada es, traducida a \\(\mathcal{D}^{\mathrm{op}}\\), que \\((GY, \varepsilon\_Y)\\) es una flecha universal de \\(Y\\) a \\(F^{\mathrm{op}}\\). Se aplica el Teorema 8.10 a \\(F^{\mathrm{op}}\\). \\(\blacksquare\\)

---

## Nivel 1

### Ejercicio 1

*Unidad y counidad de \\(k^{(-)} \dashv U\\); identidades triangulares.*

Para un conjunto \\(S\\), se escribe \\(e\_s\\) (\\(s \in S\\)) para la base canónica de \\(k^{(S)}\\). Sea \\(F = k^{(-)}\\).

**Unidad.** \\(\eta\_X\colon X \to U(k^{(X)})\\), \\(x \mapsto e\_x\\): la inclusión de la base (Ejemplo 4.10).

**Counidad.** \\(\varepsilon\_W\colon k^{(UW)} \to W\\) es la única transformación lineal con \\(\varepsilon\_W(e\_w) = w\\):

\\[
\varepsilon\_W\Big(\textstyle\sum\_i \lambda\_i e\_{w\_i}\Big) = \sum\_i \lambda\_i w\_i.
\\]

Toma una combinación lineal **formal** de vectores de \\(W\\) y la **evalúa** en \\(W\\). Hay que distinguir \\(e\_w \in k^{(UW)}\\) de \\(w \in W\\): por ejemplo, \\(e\_{w + w'} \neq e\_w + e\_{w'}\\) en \\(k^{(UW)}\\), aunque ambos tienen la misma imagen bajo \\(\varepsilon\_W\\).

Ambas son las transpuestas de las identidades (Definición 8.8): \\(\eta\_X\\) es la restricción de \\(1\_{FX}\\) a la base, y \\(\varepsilon\_W\\) es la extensión lineal de \\(1\_{UW}\\).

**Primera identidad: \\(\varepsilon\_{FX} \circ F(\eta\_X) = 1\_{FX}\\).** Ambos lados son lineales de \\(k^{(X)}\\) en \\(k^{(X)}\\), así que basta compararlos en la base. \\(F(\eta\_X)\\) envía \\(e\_x\\) a \\(e\_{\eta\_X(x)} = e\_{e\_x}\\), un vector básico de \\(k^{(U k^{(X)})}\\), y \\(\varepsilon\_{FX}\\) lo evalúa:

\\[
e\_x \longmapsto e\_{e\_x} \longmapsto e\_x.
\\]

**Segunda identidad: \\(U(\varepsilon\_W) \circ \eta\_{UW} = 1\_{UW}\\).** Para \\(w \in W\\):

\\[
w \longmapsto e\_w \longmapsto \varepsilon\_W(e\_w) = w.
\\]

\\(\blacksquare\\)

Naturalidad, por completitud: para \\(f\colon X \to Y\\), \\(F(f)(e\_x) = e\_{f(x)}\\), así que \\(UF(f) \circ \eta\_X = \eta\_Y \circ f\\); para \\(T\colon W \to W'\\) lineal, \\(T \circ \varepsilon\_W\\) y \\(\varepsilon\_{W'} \circ FU(T)\\) envían \\(e\_w\\) a \\(T(w)\\).

---

### Ejercicio 2

*\\(D \dashv U \dashv I\\); ¿tiene \\(D\\) adjunto izquierdo?, ¿tiene \\(I\\) adjunto derecho?*

**\\(D \dashv U\\).** Para un conjunto \\(X\\) y un espacio \\(Y\\), toda función \\(X \to UY\\) es continua como función \\(DX \to Y\\), porque en \\(DX\\) todo subconjunto es abierto. Luego \\(\mathbf{Top}(DX, Y) = \mathbf{Set}(X, UY)\\) como conjuntos de funciones, y la biyección es la identidad. Es natural: para \\(k\colon X' \to X\\) y \\(h\colon Y \to Y'\\), las funciones subyacentes de \\(D(k)\\) y \\(U(h)\\) son \\(k\\) y \\(h\\), así que \\(h \circ g \circ D(k)\\) y \\(U(h) \circ g \circ k\\) son la misma función.

**\\(U \dashv I\\).** Para un espacio \\(X\\) y un conjunto \\(Z\\), toda función \\(UX \to Z\\) es continua como función \\(X \to IZ\\), porque los únicos abiertos de \\(IZ\\) son \\(\emptyset\\) y \\(Z\\), cuyas imágenes inversas son \\(\emptyset\\) y \\(X\\). Luego \\(\mathbf{Set}(UX, Z) = \mathbf{Top}(X, IZ)\\), con la misma naturalidad. \\(\blacksquare\\)

**\\(D\\) no tiene adjunto izquierdo.** Si lo tuviera, \\(D\\) sería adjunto derecho y preservaría límites (Teorema 9.2). Sea \\(X\_n = \\{0, 1\\}\\) para \\(n \in \mathbb{N}\\) y \\(X = \prod\_n X\_n\\) en \\(\mathbf{Set}\\). Si \\((DX, (D\pi\_n))\\) fuera un producto de los \\(DX\_n\\) en \\(\mathbf{Top}\\), el cono formado por el producto topológico \\(\prod\_n DX\_n\\) y sus proyecciones se factorizaría por una función continua \\(u\colon \prod\_n DX\_n \to DX\\) con \\(\pi\_n \circ u = \pi\_n\\) para todo \\(n\\). Entonces \\(u\\) es la identidad del conjunto \\(X\\), y su continuidad diría que todo subconjunto de \\(\prod\_n DX\_n\\) es abierto. Pero en la topología producto todo abierto básico no vacío deja libres infinitas coordenadas, y es infinito; ningún punto es abierto. Contradicción.

**\\(I\\) no tiene adjunto derecho.** Si lo tuviera, \\(I\\) preservaría colímites. Sea \\(\\{0, 1\\} = \\{0\\} \sqcup \\{1\\}\\) en \\(\mathbf{Set}\\). Si \\(I\\{0, 1\\}\\) con las inclusiones fuera un coproducto de dos espacios de un punto, el coproducto topológico (la unión disjunta, que es el espacio discreto de dos puntos) se recibiría con una función continua \\(u\colon I\\{0, 1\\} \to D\\{0, 1\\}\\) compatible con las inclusiones, es decir, la identidad. Pero \\(\\{0\\}\\) es abierto en el discreto y no en el indiscreto. Contradicción.

Observe que \\(D\\) sí preserva los límites finitos (un producto finito o un subespacio de discretos es discreto) e \\(I\\) preserva el objeto inicial (\\(I\emptyset = \emptyset\\)). Hay que buscar el límite o colímite adecuado: productos infinitos en un caso, coproductos en el otro.

---

### Ejercicio 3

*\\(f^{-1}(T) \subseteq S\\) si y solo si \\(T \subseteq \forall\_f(S)\\).*

Sean \\(S \subseteq X\\), \\(T \subseteq Y\\), y recuérdese \\(\forall\_f(S) = \\{y \mid \forall x, \ f(x) = y \Rightarrow x \in S\\}\\).

(\\(\Rightarrow\\)) Sea \\(y \in T\\) y sea \\(x\\) con \\(f(x) = y\\). Entonces \\(x \in f^{-1}(T) \subseteq S\\). Luego \\(y \in \forall\_f(S)\\).

(\\(\Leftarrow\\)) Sea \\(x \in f^{-1}(T)\\). Entonces \\(f(x) \in T \subseteq \forall\_f(S)\\). Al aplicar la definición de \\(\forall\_f(S)\\) al elemento \\(f(x)\\) y al propio \\(x\\), que cumple \\(f(x) = f(x)\\), se obtiene \\(x \in S\\). \\(\blacksquare\\)

Las dos funciones son monótonas (si \\(S \subseteq S'\\), entonces \\(\forall\_f(S) \subseteq \forall\_f(S')\\), y lo mismo para \\(f^{-1}\\)), así que son funtores entre los órdenes y la equivalencia probada es la adjunción \\(f^{-1} \dashv \forall\_f\\). Observe que todo \\(y \notin f(X)\\) pertenece a \\(\forall\_f(S)\\) por vacuidad: "todas las \\(x\\) sobre \\(y\\) están en \\(S\\)" es cierto si no hay ninguna.

---

### Ejercicio 4

*Comparar \\((A \sqcup A') \times B\\) con \\((A \times B) \sqcup (A' \times B)\\).*

Se usa el modelo \\(A \sqcup A' = (\\{0\\} \times A) \cup (\\{1\\} \times A')\\). Entonces

\\[
(A \sqcup A') \times B = \\{((0, a), b)\\} \cup \\{((1, a'), b)\\}, \qquad (A \times B) \sqcup (A' \times B) = \\{(0, (a, b))\\} \cup \\{(1, (a', b))\\},
\\]

con \\(a \in A\\), \\(a' \in A'\\), \\(b \in B\\). La función

\\[
\theta\colon (A \times B) \sqcup (A' \times B) \to (A \sqcup A') \times B, \qquad (i, (x, b)) \mapsto ((i, x), b),
\\]

es una biyección, con inversa evidente. Es la flecha canónica \\([\iota\_1 \times 1\_B, \ \iota\_2 \times 1\_B]\\).

**Lo que dice la tabla.** El Teorema 9.2 afirma algo más preciso: \\((A \sqcup A') \times B\\), con las flechas \\(\iota\_1 \times 1\_B\\) e \\(\iota\_2 \times 1\_B\\), **es** un coproducto de \\(A \times B\\) y \\(A' \times B\\). Se verifica directamente: dadas \\(g\colon A \times B \to C\\) y \\(g'\colon A' \times B \to C\\), la única función \\(h\colon (A \sqcup A') \times B \to C\\) con \\(h \circ (\iota\_1 \times 1\_B) = g\\) y \\(h \circ (\iota\_2 \times 1\_B) = g'\\) es

\\[
h((0, a), b) = g(a, b), \qquad h((1, a'), b) = g'(a', b),
\\]

porque todo elemento de \\((A \sqcup A') \times B\\) tiene exactamente una de esas dos formas. La adjunción explica por qué: al currificar,

\\[
\mathbf{Set}((A \sqcup A') \times B, C) \cong \mathbf{Set}(A \sqcup A', C^B) \cong \mathbf{Set}(A, C^B) \times \mathbf{Set}(A', C^B) \cong \mathbf{Set}(A \times B, C) \times \mathbf{Set}(A' \times B, C).
\\]

\\(\blacksquare\\)

Para conjuntos finitos con \\(m\\), \\(m'\\) y \\(n\\) elementos, la biyección es la ley distributiva \\((m + m') n = mn + m'n\\).

---

### Ejercicio 5

*\\(\Delta\colon \mathcal{C} \to \mathcal{C} \times \mathcal{C}\\) tiene adjunto derecho si y solo si hay productos binarios, e izquierdo si y solo si hay coproductos binarios.*

Una flecha \\(\Delta X \to (A, B)\\) en \\(\mathcal{C} \times \mathcal{C}\\) es un par \\((f\colon X \to A, \ g\colon X \to B)\\), y \\(\Delta(h) = (h, h)\\).

**Adjunto derecho.** Por el Teorema 8.10 dual, \\(\Delta\\) tiene adjunto derecho si y solo si para cada \\((A, B)\\) existen un objeto \\(P\\) y una flecha \\(\varepsilon = (\pi\_1, \pi\_2)\colon (P, P) \to (A, B)\\) tales que todo par \\((f, g)\colon \Delta X \to (A, B)\\) se escribe de manera única como

\\[
(f, g) = (\pi\_1, \pi\_2) \circ \Delta(h) = (\pi\_1 \circ h, \ \pi\_2 \circ h), \qquad h\colon X \to P.
\\]

Es, palabra por palabra, la Definición 4.4 del producto, con \\(h = \langle f, g \rangle\\). Luego el adjunto derecho existe si y solo si todo par de objetos tiene producto. En ese caso, el adjunto es \\((A, B) \mapsto A \times B\\), con \\((f, g) \mapsto f \times g = \langle f \circ \pi\_1, g \circ \pi\_2 \rangle\\), y la counidad es el par de proyecciones.

**Adjunto izquierdo.** Por el Teorema 8.10, \\(\Delta\\) tiene adjunto izquierdo si y solo si para cada \\((A, B)\\) hay una flecha universal \\((\iota\_1, \iota\_2)\colon (A, B) \to \Delta S\\): todo par \\((f\colon A \to X, \ g\colon B \to X)\\) se escribe de manera única como \\((h \circ \iota\_1, h \circ \iota\_2)\\). Es la Definición 4.7 del coproducto, con \\(h = [f, g]\\). \\(\blacksquare\\)

**Sobre la solución seleccionada.** La de la sección de ejercicios es correcta. Su paso "esto es exactamente decir que \\(P(A,B)\\) es un producto" es el Teorema 8.10 dual; aquí se hace explícito, y con él la funtorialidad de \\(P\\).

---

## Nivel 2

### Ejercicio 6

*\\(\Delta\colon \mathcal{C} \to [\mathcal{J}, \mathcal{C}]\\) tiene adjunto derecho si y solo si \\(\mathcal{C}\\) tiene límites de forma \\(\mathcal{J}\\); los límites conmutan con los límites.*

**El funtor diagonal.** \\(\Delta X\\) es el funtor constante con valor \\(X\\) y \\(\Delta X(u) = 1\_X\\). Para \\(h\colon X \to Y\\), \\(\Delta h\colon \Delta X \Rightarrow \Delta Y\\) tiene todas sus componentes iguales a \\(h\\); es natural porque \\(1\_Y \circ h = h \circ 1\_X\\). Como se observó en la Sección 1 del Capítulo 6, una transformación natural \\(\lambda\colon \Delta X \Rightarrow D\\) es exactamente un cono sobre \\(D\\) con vértice \\(X\\): la naturalidad respecto de \\(u\colon j \to k\\) es \\(D(u) \circ \lambda\_j = \lambda\_k \circ 1\_X\\).

**El adjunto.** Por el Teorema 8.10 dual, \\(\Delta\\) tiene adjunto derecho si y solo si para cada \\(D\\) existen \\(L\\) y \\(\pi\colon \Delta L \Rightarrow D\\) tales que todo \\(\lambda\colon \Delta X \Rightarrow D\\) se escribe de manera única como \\(\pi \circ \Delta h\\), es decir, \\(\lambda\_j = \pi\_j \circ h\\) para todo \\(j\\). Es la Definición 6.2: \\((L, \pi)\\) es un límite de \\(D\\). Luego \\(\Delta\\) tiene adjunto derecho si y solo si todo diagrama de forma \\(\mathcal{J}\\) tiene límite, y en ese caso el adjunto es

\\[
\lim\colon [\mathcal{J}, \mathcal{C}] \to \mathcal{C}, \qquad \mathcal{C}(X, \lim D) \cong \mathrm{Nat}(\Delta X, D),
\\]

con counidad el cono límite \\(\pi\\). En particular, \\(\lim\\) es un funtor (su acción en flechas la da el Teorema 8.10 dual) y es un adjunto derecho. Dualmente, \\(\mathrm{colim} \dashv \Delta\\) cuando existen los colímites de forma \\(\mathcal{J}\\).

**Límites punto por punto.** Para aplicar el Teorema 9.2 hace falta saber que \\([\mathcal{J}, \mathcal{C}]\\) tiene límites. La Proposición 7.10 se dio con una idea de prueba; aquí se completa para una forma fija \\(\mathcal{I}\\). Supóngase que \\(\mathcal{C}\\) tiene límites de forma \\(\mathcal{I}\\) y sea \\(E\colon \mathcal{I} \to [\mathcal{J}, \mathcal{C}]\\), \\(i \mapsto E\_i\\).

- Para cada \\(j\\), sea \\(L(j)\\) el límite de \\(i \mapsto E\_i(j)\\), con proyecciones \\(p\_{i,j}\\).
- Para \\(v\colon j \to j'\\), la familia \\(E\_i(v) \circ p\_{i,j}\\) es un cono sobre \\(i \mapsto E\_i(j')\\): para \\(w\colon i \to i'\\), la naturalidad de \\(E(w)\\) da \\(E(w)\_{j'} \circ E\_i(v) \circ p\_{i,j} = E\_{i'}(v) \circ E(w)\_j \circ p\_{i,j} = E\_{i'}(v) \circ p\_{i',j}\\). Se define \\(L(v)\\) como la única flecha con \\(p\_{i,j'} \circ L(v) = E\_i(v) \circ p\_{i,j}\\). La unicidad da \\(L(1) = 1\\) y \\(L(v' v) = L(v') L(v)\\).
- Por construcción, cada \\(p\_i = (p\_{i,j})\_j\colon L \Rightarrow E\_i\\) es natural, y \\((L, (p\_i))\\) es un cono sobre \\(E\\) porque \\(E(w)\_j \circ p\_{i,j} = p\_{i',j}\\).
- Universalidad: si \\(\mu\_i\colon M \Rightarrow E\_i\\) es un cono, para cada \\(j\\) hay una única \\(h\_j\colon M(j) \to L(j)\\) con \\(p\_{i,j} \circ h\_j = \mu\_{i,j}\\). La familia \\(h\\) es natural: \\(L(v) \circ h\_j\\) y \\(h\_{j'} \circ M(v)\\) factorizan el mismo cono \\(E\_i(v) \circ \mu\_{i,j} = \mu\_{i,j'} \circ M(v)\\) sobre \\(i \mapsto E\_i(j')\\), luego son iguales. La unicidad de \\(h\\) es componente a componente.

**Los límites conmutan con los límites.** Sea \\(D\colon \mathcal{I} \times \mathcal{J} \to \mathcal{C}\\), con \\(\mathcal{C}\\) con límites de forma \\(\mathcal{I}\\) y de forma \\(\mathcal{J}\\). Fijando la primera variable se obtiene \\(E\colon \mathcal{I} \to [\mathcal{J}, \mathcal{C}]\\), \\(E\_i = D(i, -)\\). Por el paso anterior, \\(E\\) tiene límite, calculado punto por punto: \\((\lim\_i E\_i)(j) = \lim\_i D(i, j)\\). Como \\(\lim\_{\mathcal{J}}\\) es adjunto derecho, preserva ese límite (Teorema 9.2):

\\[
\lim\_j \lim\_i D(i, j) = \lim\_{\mathcal{J}} \Big(\lim\_i E\_i\Big) \cong \lim\_i \lim\_{\mathcal{J}} E\_i = \lim\_i \lim\_j D(i, j).
\\]

El isomorfismo se debe a que ambos lados son límites del mismo diagrama \\(i \mapsto \lim\_j D(i, j)\\), y los límites son únicos salvo isomorfismo. \\(\blacksquare\\)

**Idea clave:** un cono es una transformación natural desde un funtor constante; por eso "límite" es lo mismo que "adjunto derecho de la diagonal", y el Teorema 9.2 hace el resto.

---

### Ejercicio 7

*El anillo de monoide \\(\mathbb{Z}[M]\\) es adjunto izquierdo de \\(U\colon \mathbf{Ring} \to \mathbf{Mon}\\).*

**La construcción.** Sea \\(M\\) un monoide con neutro \\(1\_M\\). Como grupo abeliano, \\(\mathbb{Z}[M] = \mathbb{Z}^{(M)}\\) es el grupo abeliano libre con base \\(\\{e\_m \mid m \in M\\}\\) (Ejemplo 9.9): sumas formales finitas \\(\sum n\_m e\_m\\). El producto se define en la base y se extiende de manera bilineal:

\\[
\Big(\textstyle\sum\_m n\_m e\_m\Big) \Big(\sum\_{m'} n'\_{m'} e\_{m'}\Big) = \sum\_{m, m'} n\_m n'\_{m'} \\, e\_{m m'}.
\\]

Es distributivo por construcción. Es asociativo porque ambos lados de \\((xy)z = x(yz)\\) son trilineales y coinciden en la base: \\((e\_m e\_{m'}) e\_{m''} = e\_{(m m') m''} = e\_{m (m' m'')}\\). El neutro es \\(e\_{1\_M}\\). Luego \\(\mathbb{Z}[M]\\) es un anillo, conmutativo si y solo si \\(M\\) lo es.

**La unidad.** \\(\eta\_M\colon M \to U\mathbb{Z}[M]\\), \\(m \mapsto e\_m\\). Es un homomorfismo de monoides: \\(e\_m e\_{m'} = e\_{m m'}\\) y \\(e\_{1\_M} = 1\\).

**Universalidad.** Sea \\(R\\) un anillo y \\(\varphi\colon M \to UR\\) un homomorfismo de monoides, es decir, \\(\varphi(m m') = \varphi(m) \varphi(m')\\) y \\(\varphi(1\_M) = 1\\). Se define

\\[
\bar{\varphi}\colon \mathbb{Z}[M] \to R, \qquad \bar{\varphi}\Big(\textstyle\sum n\_m e\_m\Big) = \sum n\_m \varphi(m).
\\]

Es la única función aditiva con \\(\bar{\varphi}(e\_m) = \varphi(m)\\), por la propiedad del grupo abeliano libre. Es multiplicativa: \\(\bar{\varphi}(x y)\\) y \\(\bar{\varphi}(x) \bar{\varphi}(y)\\) son biaditivas en \\((x, y)\\) y coinciden en la base, porque \\(\bar{\varphi}(e\_m e\_{m'}) = \varphi(m m') = \varphi(m) \varphi(m')\\). Preserva el uno: \\(\bar{\varphi}(e\_{1\_M}) = \varphi(1\_M) = 1\\). Luego es un homomorfismo de anillos con \\(U(\bar{\varphi}) \circ \eta\_M = \varphi\\). Es único: un homomorfismo de anillos con esa propiedad es aditivo y toma los valores \\(\varphi(m)\\) en la base. Así, \\((\mathbb{Z}[M], \eta\_M)\\) es una flecha universal de \\(M\\) a \\(U\\).

Por el Teorema 8.10, \\(\mathbb{Z}[-]\\) se extiende a un funtor con \\(\mathbb{Z}[-] \dashv U\\); en flechas, \\(\mathbb{Z}[f]\\) envía \\(\sum n\_m e\_m\\) a \\(\sum n\_m e\_{f(m)}\\). \\(\blacksquare\\)

**Comprobación.** Para \\(M = (\mathbb{N}, +, 0)\\), \\(e\_n \mapsto x^n\\) da \\(\mathbb{Z}[\mathbb{N}] \cong \mathbb{Z}[x]\\). Como \\((\mathbb{N}, +, 0)\\) es el monoide libre en un generador, la Proposición 9.8 dice que \\(\mathbb{Z}[x]\\) es el anillo libre en un generador: \\(\mathbf{Ring}(\mathbb{Z}[x], R) \cong \mathbf{Mon}(\mathbb{N}, UR) \cong UR\\). Es el Ejemplo 5.2. Para un grupo \\(G\\), \\(\mathbb{Z}[G]\\) es el **anillo de grupo**, y para \\(M = \mathbb{Z}\\) se obtienen los polinomios de Laurent \\(\mathbb{Z}[x, x^{-1}]\\), que aparecen en el polinomio de Alexander.

---

### Ejercicio 8

*Adjuntos de la inclusión \\(T\colon \mathbf{Set} \to [\mathbf{B}G, \mathbf{Set}]\\) de los \\(G\\)-conjuntos triviales.*

Se escribe \\(g \cdot y\\) para la acción de un \\(G\\)-conjunto \\(Y\\) y \\(TX\\) para \\(X\\) con la acción trivial \\(g \cdot x = x\\). Las flechas de \\([\mathbf{B}G, \mathbf{Set}]\\) son las funciones equivariantes (Ejemplo 3.6). \\(T\\) es un funtor: toda función entre conjuntos con acción trivial es equivariante; y es plenamente fiel.

**Adjunto izquierdo: las órbitas.** Sea \\(Y/G\\) el conjunto de órbitas y \\(q\_Y\colon Y \to Y/G\\) la proyección. Una función equivariante \\(\alpha\colon Y \to Y'\\) envía órbitas en órbitas, así que induce \\(\alpha/G\colon [y] \mapsto [\alpha(y)]\\), y \\((-)/G\\) es un funtor. Se afirma \\((-)/G \dashv T\\):

\\[
\mathbf{Set}(Y/G, X) \cong \mathrm{Nat}(Y, TX), \qquad \psi \mapsto \psi \circ q\_Y.
\\]

Una función \\(\varphi\colon Y \to X\\) es equivariante hacia \\(TX\\) si y solo si \\(\varphi(g \cdot y) = g \cdot \varphi(y) = \varphi(y)\\) para todo \\(g\\), es decir, si es constante en las órbitas. Por la propiedad del conjunto cociente (Ejemplo 6.9), esas funciones son exactamente las de la forma \\(\psi \circ q\_Y\\) con \\(\psi\\) única. La naturalidad: para \\(\alpha\colon Y' \to Y\\) equivariante y \\(h\colon X \to X'\\), \\(h \circ \psi \circ (\alpha/G) \circ q\_{Y'} = h \circ \psi \circ q\_Y \circ \alpha\\), que es \\(T(h) \circ (\psi \circ q\_Y) \circ \alpha\\).

**Adjunto derecho: los puntos fijos.** Sea \\(Y^G = \\{y \in Y \mid g \cdot y = y \ \text{para todo} \ g\\}\\). Una función equivariante \\(\alpha\\) envía puntos fijos en puntos fijos, porque \\(g \cdot \alpha(y) = \alpha(g \cdot y) = \alpha(y)\\); así \\((-)^G\\) es un funtor. Se afirma \\(T \dashv (-)^G\\):

\\[
\mathrm{Nat}(TX, Y) \cong \mathbf{Set}(X, Y^G).
\\]

Si \\(\varphi\colon TX \to Y\\) es equivariante, \\(\varphi(x) = \varphi(g \cdot x) = g \cdot \varphi(x)\\), luego \\(\varphi(X) \subseteq Y^G\\). Recíprocamente, toda función \\(X \to Y^G\\), vista con valores en \\(Y\\), es equivariante desde \\(TX\\). La biyección es la correstricción, natural porque componer y correstringir conmutan. \\(\blacksquare\\)

**Dos comprobaciones.**

- \\(T\\) es el funtor diagonal \\(\Delta\colon \mathbf{Set} \to [\mathbf{B}G, \mathbf{Set}]\\). Por el Ejercicio 6, su adjunto derecho es \\(\lim\\) y el izquierdo es \\(\mathrm{colim}\\). En efecto, por la fórmula del Teorema 7.2, el límite de \\(Y\colon \mathbf{B}G \to \mathbf{Set}\\) son los \\(y\\) con \\(Y(g)(y) = y\\) para toda \\(g\\): los puntos fijos. El colímite es el cociente de \\(Y\\) por \\(y \sim g \cdot y\\): las órbitas.
- Como \\(T\\) es plenamente fiel, la counidad de \\((-)/G \dashv T\\) es un isomorfismo (Proposición 9.6): las órbitas de una acción trivial son puntos. Dualmente, la unidad \\(X \to (TX)^G = X\\) de \\(T \dashv (-)^G\\) es la identidad.

---

### Ejercicio 9

*En una categoría cartesiana cerrada, \\(A \times (B + C) \cong (A \times B) + (A \times C)\\); por qué falla en Vect con \\(\times = \oplus\\).*

**\\(A \times -\\) es adjunto izquierdo.** La definición pide que \\(- \times A\\) tenga adjunto derecho \\((-)^A\\). Sea \\(\sigma\_X = \langle \pi\_2, \pi\_1 \rangle\colon X \times A \to A \times X\\), un isomorfismo (su inversa es la flecha análoga), natural en \\(X\\). Entonces

\\[
\mathcal{C}(A \times X, Y) \cong \mathcal{C}(X \times A, Y) \cong \mathcal{C}(X, Y^A), \qquad \varphi \mapsto \varphi \circ \sigma\_X \mapsto \overline{\varphi \circ \sigma\_X},
\\]

es una composición de biyecciones naturales en \\(X\\) y en \\(Y\\). Luego \\(A \times - \dashv (-)^A\\).

**La ley distributiva.** Por el Teorema 9.2, \\(A \times -\\) preserva los colímites que existen, en particular el coproducto \\(B + C\\): el objeto \\(A \times (B + C)\\), con las flechas \\(1\_A \times \iota\_1\\) y \\(1\_A \times \iota\_2\\), es un coproducto de \\(A \times B\\) y \\(A \times C\\). Por la unicidad del coproducto salvo isomorfismo, la flecha canónica

\\[
[1\_A \times \iota\_1, \ 1\_A \times \iota\_2]\colon (A \times B) + (A \times C) \to A \times (B + C)
\\]

es un isomorfismo. Basta que exista \\(B + C\\); el coproducto de la izquierda existe entonces automáticamente. \\(\blacksquare\\)

El mismo argumento, con el colímite vacío, da \\(A \times 0 \cong 0\\) si existe un objeto inicial \\(0\\).

**Por qué falla en \\(\mathbf{Vect}\_k\\).** Allí el producto y el coproducto son ambos \\(\oplus\\) (Ejemplo 4.8). La ley diría \\(A \oplus (B \oplus C) \cong (A \oplus B) \oplus (A \oplus C)\\). Con \\(A = k\\) y \\(B = C = 0\\) se obtiene \\(k \cong k \oplus k\\), falso por dimensión. Más simple aún: \\(A \oplus 0 = A \neq 0\\), así que \\(A \oplus -\\) no preserva el objeto inicial. Por el Teorema 9.2, \\(- \oplus A\\) no tiene adjunto derecho para \\(A \neq 0\\): \\(\mathbf{Vect}\_k\\) **no** es cartesiana cerrada. Sí es cerrada respecto de \\(\otimes\\) (Ejemplo 8.5), y en consecuencia \\(A \otimes (B \oplus C) \cong (A \otimes B) \oplus (A \otimes C)\\), que es la distributividad correcta en álgebra lineal.

---

### Ejercicio 10

*Con el Teorema 9.2, \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) no tiene adjunto derecho.*

Si \\(U\\) tuviera adjunto derecho, \\(U\\) sería adjunto izquierdo y, por el Teorema 9.2, preservaría todos los colímites. El objeto inicial es el colímite del diagrama vacío, así que \\(U\\) enviaría el objeto inicial de \\(\mathbf{Grp}\\), el grupo trivial (Ejemplo 4.3), a un objeto inicial de \\(\mathbf{Set}\\). Pero \\(U\\) del grupo trivial es un conjunto con un elemento, que no es inicial: no hay ninguna función \\(\\{\star\\} \to \emptyset\\). Contradicción. \\(\blacksquare\\)

Otro testigo, del Ejemplo 7.8: \\(U\\) tampoco preserva coproductos, porque \\(U(\mathbb{Z} \ast \mathbb{Z})\\) no es \\(U\mathbb{Z} \sqcup U\mathbb{Z}\\). Basta un solo colímite no preservado.

**Sobre la solución seleccionada.** La de la sección de ejercicios es correcta.
