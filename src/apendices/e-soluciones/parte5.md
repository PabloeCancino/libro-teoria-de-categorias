# Soluciones de la Parte V

Soluciones completas de los ejercicios de nivel 1 y 2 de la Parte V (mónadas, álgebras y categorías de Kleisli). Conviene intentar cada ejercicio antes de leer su solución.

---

## Nivel 1

### Ejercicio 1

*Verificar las leyes de mónada para la mónada de elementos opcionales.*

Se fija la notación. Para un conjunto \\(X\\), \\(TX = X + \\{\bot\\}\\). Para \\(f\colon X \to Y\\), \\(T(f)\colon X + \\{\bot\\} \to Y + \\{\bot\\}\\) es \\(f\\) en \\(X\\) y envía \\(\bot \mapsto \bot\\). Es claro que \\(T(1\_X) = 1\_{TX}\\) y \\(T(g \circ f) = T(g) \circ T(f)\\), así que \\(T\\) es un funtor.

Para distinguir los puntos agregados en las iteraciones se escribe

\\[
TTX = X + \\{\bot\_1\\} + \\{\bot\_2\\},
\\]

donde \\(\bot\_1\\) es el punto de \\(TX\\) (el interior) y \\(\bot\_2\\) el que agrega la segunda aplicación de \\(T\\) (el exterior). Las transformaciones son:

- \\(\eta\_X\colon X \to X + \\{\bot\\}\\), la inclusión;
- \\(\mu\_X\colon TTX \to TX\\), con \\(x \mapsto x\\) y \\(\bot\_1, \bot\_2 \mapsto \bot\\).

**Naturalidad.** Para \\(f\colon X \to Y\\), \\(T(f) \circ \eta\_X\\) y \\(\eta\_Y \circ f\\) envían \\(x\\) a \\(f(x)\\). Las funciones \\(T(f) \circ \mu\_X\\) y \\(\mu\_Y \circ TT(f)\\) envían \\(x \mapsto f(x)\\) y los dos puntos \\(\bot\_1, \bot\_2\\) a \\(\bot\\), porque \\(TT(f)\\) fija \\(\bot\_1\\) y \\(\bot\_2\\).

**Unidad.** La función \\(\eta\_{TX}\colon TX \to TTX\\) es la inclusión de \\(X + \\{\bot\\}\\) como \\(X + \\{\bot\_1\\}\\). La función \\(T(\eta\_X)\\) es la identidad en \\(X\\) y envía el \\(\bot\\) de \\(TX\\) al punto exterior \\(\bot\_2\\). En ambos casos, al aplicar \\(\mu\_X\\) se recupera \\(x \mapsto x\\) y \\(\bot \mapsto \bot\\). Luego

\\[
\mu\_X \circ \eta\_{TX} = 1\_{TX} = \mu\_X \circ T(\eta\_X).
\\]

**Asociatividad.** Se escribe \\(TTTX = X + \\{\bot\_1, \bot\_2, \bot\_3\\}\\), con \\(\bot\_k\\) agregado en la etapa \\(k\\). Las dos flechas \\(TTTX \to TTX\\) son:

- \\(T(\mu\_X)\\): aplica \\(\mu\_X\\) a la parte \\(TTX = X + \\{\bot\_1, \bot\_2\\}\\) y fija el punto exterior; envía \\(\bot\_1, \bot\_2 \mapsto \bot\_1\\) y \\(\bot\_3 \mapsto \bot\_2\\);
- \\(\mu\_{TX}\\): ve \\(TTTX\\) como \\(TT(TX)\\), con \\(TX = X + \\{\bot\_1\\}\\), e identifica los dos puntos exteriores; envía \\(\bot\_1 \mapsto \bot\_1\\) y \\(\bot\_2, \bot\_3 \mapsto \bot\_2\\).

Las dos fijan \\(X\\) y envían los tres puntos agregados a \\(\\{\bot\_1, \bot\_2\\}\\). Después, \\(\mu\_X\\) envía \\(\bot\_1\\) y \\(\bot\_2\\) a \\(\bot\\). Así, \\(\mu\_X \circ T(\mu\_X)\\) y \\(\mu\_X \circ \mu\_{TX}\\) son la misma función: la identidad en \\(X\\) y la constante \\(\bot\\) en los tres puntos agregados. \\(\blacksquare\\)

**Idea clave:** todas las flechas de la estructura fijan \\(X\\) y mandan "fallos" a "fallos"; las leyes se reducen a que todos los fallos se identifican al final.

---

### Ejercicio 2

*Asociatividad de la mónada \\(\mathcal{P}\\): unir primero por dentro o primero por fuera da lo mismo.*

Recuérdese que \\(\mathcal{P}(f)\\) es la imagen directa, \\(\mathcal{P}(f)(S) = \\{f(s) \mid s \in S\\}\\), y que \\(\mu\_X(\mathcal{S}) = \bigcup \mathcal{S}\\). Sea \\(\mathfrak{S} \in \mathcal{P}\mathcal{P}\mathcal{P}(X)\\): un conjunto de familias \\(\mathcal{A}\\) de subconjuntos de \\(X\\).

**Primero el nivel interior.** \\(\mathcal{P}(\mu\_X)(\mathfrak{S}) = \\{\bigcup \mathcal{A} \mid \mathcal{A} \in \mathfrak{S}\\}\\), y luego

\\[
\mu\_X\big(\mathcal{P}(\mu\_X)(\mathfrak{S})\big) = \bigcup\_{\mathcal{A} \in \mathfrak{S}} \bigcup \mathcal{A}.
\\]

**Primero el nivel exterior.** \\(\mu\_{\mathcal{P}X}(\mathfrak{S}) = \bigcup \mathfrak{S} = \\{B \mid B \in \mathcal{A} \text{ para algún } \mathcal{A} \in \mathfrak{S}\\}\\), y luego

\\[
\mu\_X\big(\mu\_{\mathcal{P}X}(\mathfrak{S})\big) = \bigcup \Big(\bigcup \mathfrak{S}\Big).
\\]

Un elemento \\(x \in X\\) pertenece a cualquiera de los dos conjuntos si y solo si existen \\(\mathcal{A} \in \mathfrak{S}\\) y \\(B \in \mathcal{A}\\) con \\(x \in B\\). Por lo tanto \\(\mu\_X \circ \mathcal{P}(\mu\_X) = \mu\_X \circ \mu\_{\mathcal{P}X}\\). \\(\blacksquare\\)

---

### Ejercicio 3

*La composición de Kleisli es asociativa y \\(\eta\\) es neutra; indicar qué ley de mónada se usa en cada paso.*

Sean \\(f\colon X \to TY\\), \\(g\colon Y \to TZ\\) y \\(h\colon Z \to TW\\). Por la Definición 11.1, \\(g \circ\_T f = \mu\_Z \circ T(g) \circ f\\).

**Asociatividad.** Por un lado, como \\(T\\) es un funtor,

\\[
(h \circ\_T g) \circ\_T f = \mu\_W \circ T\big(\mu\_W \circ T(h) \circ g\big) \circ f = \mu\_W \circ T(\mu\_W) \circ TT(h) \circ T(g) \circ f.
\\]

Por otro lado,

\\[
h \circ\_T (g \circ\_T f) = \mu\_W \circ T(h) \circ \mu\_Z \circ T(g) \circ f.
\\]

La **naturalidad de \\(\mu\\)** aplicada a \\(h\colon Z \to TW\\) dice \\(T(h) \circ \mu\_Z = \mu\_{TW} \circ TT(h)\\). Al sustituir, la segunda expresión queda

\\[
\mu\_W \circ \mu\_{TW} \circ TT(h) \circ T(g) \circ f.
\\]

La **ley de asociatividad** \\(\mu\_W \circ \mu\_{TW} = \mu\_W \circ T(\mu\_W)\\) (Definición 10.1, en la componente \\(W\\)) iguala esta expresión con la primera.

**Neutralidad.** A la derecha:

\\[
f \circ\_T \eta\_X = \mu\_Y \circ T(f) \circ \eta\_X = \mu\_Y \circ \eta\_{TY} \circ f = f.
\\]

El segundo paso es la **naturalidad de \\(\eta\\)** aplicada a \\(f\\); el tercero, la **ley de unidad** \\(\mu \circ \eta T = 1\_T\\). A la izquierda:

\\[
\eta\_Y \circ\_T f = \mu\_Y \circ T(\eta\_Y) \circ f = f,
\\]

por la **ley de unidad** \\(\mu \circ T\eta = 1\_T\\). Así, \\(\mathcal{C}\_T\\) es una categoría. \\(\blacksquare\\)

**Idea clave:** la asociatividad de Kleisli usa la naturalidad de \\(\mu\\) y la asociatividad de \\(\mu\\); cada neutralidad usa una de las dos leyes de unidad (y la neutralidad derecha, además, la naturalidad de \\(\eta\\)).

---

### Ejercicio 4

*Componer dos núcleos de Markov dados por matrices estocásticas de \\(2 \times 2\\).*

Se usa la convención del Ejemplo 11.9 y de \\(\mathbf{Mat}\_k\\): la entrada \\((y, x)\\) de la matriz de \\(f\\) es \\(f(y \mid x)\\), así que cada **columna** es una distribución. Sean

\\[
F = \begin{pmatrix} 0.9 & 0.2 \\\\ 0.1 & 0.8 \end{pmatrix}, \qquad G = \begin{pmatrix} 0.7 & 0.5 \\\\ 0.3 & 0.5 \end{pmatrix}
\\]

las matrices de \\(f\colon X \rightsquigarrow Y\\) y \\(g\colon Y \rightsquigarrow Z\\). Por la ecuación de Chapman–Kolmogorov, \\((g \circ\_{\mathcal{D}} f)(z \mid x) = \sum\_y g(z \mid y)\\, f(y \mid x)\\), que es la entrada \\((z, x)\\) de \\(GF\\). Por ejemplo, \\((g \circ\_{\mathcal{D}} f)(z\_1 \mid x\_1) = 0.7 \cdot 0.9 + 0.5 \cdot 0.1 = 0.68\\). En total:

\\[
GF = \begin{pmatrix} 0.68 & 0.54 \\\\ 0.32 & 0.46 \end{pmatrix}.
\\]

El enunciado no fija el orden. Si se aplica primero el núcleo de la segunda matriz y después el de la primera, la composición es

\\[
FG = \begin{pmatrix} 0.69 & 0.55 \\\\ 0.31 & 0.45 \end{pmatrix}.
\\]

Las dos composiciones son distintas: la composición de Kleisli no es conmutativa.

En ambos casos cada columna suma 1. Esto vale en general: si \\(f\\) y \\(g\\) son núcleos de Markov,

\\[
\sum\_z \sum\_y g(z \mid y)\\, f(y \mid x) = \sum\_y f(y \mid x) \sum\_z g(z \mid y) = \sum\_y f(y \mid x) = 1,
\\]

y las entradas son no negativas. Así, la composición de núcleos de Markov es un núcleo de Markov. \\(\blacksquare\\)

---

### Ejercicio 5

*La cerradura topológica es una mónada sobre \\((\mathcal{P}(X), \subseteq)\\); describir sus álgebras.*

Sea \\(c(S) = \overline{S}\\), la intersección de todos los cerrados que contienen a \\(S\\). Por el Ejemplo 10.6 basta comprobar que \\(c\\) es monótona y que \\(S \subseteq c(S)\\) y \\(c(c(S)) \subseteq c(S)\\).

- **Monótona (es un funtor).** Si \\(S \subseteq S'\\), todo cerrado que contiene a \\(S'\\) contiene a \\(S\\). Luego \\(c(S)\\) es la intersección de una familia que incluye a la que define \\(c(S')\\), y así \\(c(S) \subseteq c(S')\\).
- **Unidad.** \\(S\\) está contenido en cada cerrado de la intersección, luego \\(S \subseteq c(S)\\). Esta es la flecha \\(\eta\_S\colon S \to c(S)\\).
- **Multiplicación.** Una intersección de cerrados es cerrada, así que \\(c(S)\\) es un cerrado que contiene a \\(c(S)\\). Luego \\(c(c(S)) \subseteq c(S)\\). Esta es la flecha \\(\mu\_S\colon c(c(S)) \to c(S)\\).

En un orden parcial hay a lo más una flecha entre dos objetos. Por eso la naturalidad de \\(\eta\\) y \\(\mu\\) y los diagramas de la Definición 10.1 conmutan automáticamente. Así, \\((c, \eta, \mu)\\) es una mónada.

**Álgebras.** Un álgebra es un objeto \\(A \in \mathcal{P}(X)\\) con una flecha \\(a\colon c(A) \to A\\), es decir, con \\(c(A) \subseteq A\\). Junto con \\(A \subseteq c(A)\\), esto da \\(c(A) = A\\): **\\(A\\) es cerrado**. Las dos ecuaciones de la Definición 10.10 son automáticas, porque relacionan flechas paralelas en un orden. Recíprocamente, todo cerrado \\(A\\) cumple \\(c(A) \subseteq A\\), y por lo tanto es un álgebra de una única manera.

Un morfismo de álgebras \\(A \to B\\) es una flecha \\(A \subseteq B\\); la condición \\(h \circ a = b \circ T(h)\\) también es automática. Así, la categoría de Eilenberg–Moore es el orden de los **subconjuntos cerrados de \\(X\\)**, ordenados por inclusión. \\(\blacksquare\\)

El argumento usa solo que los cerrados son estables bajo intersecciones arbitrarias. Vale igual para la envolvente convexa (las álgebras son los convexos) o para el subgrupo generado (las álgebras son los subgrupos).

---

## Nivel 2

### Ejercicio 6

*Completar la demostración del Teorema 10.13.*

Sean \\((T, \eta, \mu)\\) una mónada sobre \\(\mathcal{C}\\), \\(X\\) un objeto y \\((A, a)\\) un álgebra. Para \\(f\colon X \to A\\) se escribe \\(f^\sharp = a \circ T(f)\colon TX \to A\\). Para un morfismo de álgebras \\(g\colon (TX, \mu\_X) \to (A, a)\\) se escribe \\(g^\flat = g \circ \eta\_X\colon X \to A\\).

**(a) \\((TX, \mu\_X)\\) es un álgebra.** La ecuación \\(\mu\_X \circ \eta\_{TX} = 1\_{TX}\\) es la ley de unidad \\(\mu \circ \eta T = 1\\). La ecuación \\(\mu\_X \circ T(\mu\_X) = \mu\_X \circ \mu\_{TX}\\) es la ley de asociatividad.

**(b) \\(f^\sharp\\) es un morfismo de álgebras.** Hay que ver que \\(f^\sharp \circ \mu\_X = a \circ T(f^\sharp)\\):

\\[
a \circ T(f^\sharp) = a \circ T(a) \circ TT(f) = a \circ \mu\_A \circ TT(f) = a \circ T(f) \circ \mu\_X = f^\sharp \circ \mu\_X.
\\]

El segundo paso es la ley de álgebra \\(a \circ T(a) = a \circ \mu\_A\\). El tercero es la naturalidad de \\(\mu\\) aplicada a \\(f\\): \\(\mu\_A \circ TT(f) = T(f) \circ \mu\_X\\).

**(c) \\((f^\sharp)^\flat = f\\).**

\\[
a \circ T(f) \circ \eta\_X = a \circ \eta\_A \circ f = f,
\\]

por la naturalidad de \\(\eta\\) y la ley de álgebra \\(a \circ \eta\_A = 1\_A\\).

**(d) \\((g^\flat)^\sharp = g\\).** Como \\(g\\) es un morfismo de álgebras, \\(a \circ T(g) = g \circ \mu\_X\\). Luego

\\[
a \circ T(g \circ \eta\_X) = a \circ T(g) \circ T(\eta\_X) = g \circ \mu\_X \circ T(\eta\_X) = g,
\\]

por la ley de unidad \\(\mu \circ T\eta = 1\\).

Por (b), (c) y (d), \\(g \mapsto g \circ \eta\_X\\) es una biyección \\(\mathcal{C}^T\big((TX, \mu\_X), (A, a)\big) \to \mathcal{C}(X, A)\\), con inversa \\(f \mapsto a \circ T(f)\\).

**(e) Funtorialidad y naturalidad.** Para \\(k\colon X' \to X\\), \\(T(k)\\) es un morfismo de álgebras \\((TX', \mu\_{X'}) \to (TX, \mu\_X)\\): la ecuación \\(T(k) \circ \mu\_{X'} = \mu\_X \circ TT(k)\\) es la naturalidad de \\(\mu\\). Así, \\(F^T(k) = T(k)\\) define un funtor \\(F^T\\). Para \\(k\\) y un morfismo de álgebras \\(h\colon (A, a) \to (B, b)\\),

\\[
(h \circ g \circ T(k))^\flat = h \circ g \circ T(k) \circ \eta\_{X'} = h \circ g \circ \eta\_X \circ k = U^T(h) \circ g^\flat \circ k,
\\]

por la naturalidad de \\(\eta\\). Esta es la condición de naturalidad del Capítulo 8, de modo que \\(F^T \dashv U^T\\).

**(f) La mónada de la adjunción es \\(T\\).** En objetos y flechas, \\(U^T F^T = T\\). La unidad es la transpuesta de \\(1\_{F^T X}\\), es decir, \\((1\_{TX})^\flat = \eta\_X\\). La counidad en \\((A, a)\\) es la transpuesta de \\(1\_A\\): \\((1\_A)^\sharp = a \circ T(1\_A) = a\\). Luego \\(\varepsilon\_{(A, a)} = a\\), y \\(U^T \varepsilon F^T\\) tiene componente \\(\varepsilon\_{(TX, \mu\_X)} = \mu\_X\\). Por el Teorema 10.8, la mónada de \\(F^T \dashv U^T\\) es \\((T, \eta, \mu)\\). \\(\blacksquare\\)

**Idea clave:** la counidad de la adjunción de Eilenberg–Moore es la propia estructura \\(a\\): "evaluar" es transponer la identidad.

---

### Ejercicio 7

*Las \\(\mathcal{P}\\)-álgebras son los retículos completos, y sus morfismos, las funciones que preservan supremos arbitrarios.*

**De retículo a álgebra.** Sea \\((A, \le)\\) un orden parcial en el que todo subconjunto tiene supremo. Se define \\(a(S) = \bigvee S\\). Entonces \\(a(\\{x\\}) = x\\), que es \\(a \circ \eta\_A = 1\_A\\). Para \\(\mathcal{S} \in \mathcal{P}\mathcal{P}(A)\\),

\\[
a\big(\mathcal{P}(a)(\mathcal{S})\big) = \bigvee\_{S \in \mathcal{S}} \bigvee S, \qquad a\big(\mu\_A(\mathcal{S})\big) = \bigvee \bigcup \mathcal{S}.
\\]

Son iguales: \\(u\\) es cota superior de \\(\\{\bigvee S \mid S \in \mathcal{S}\\}\\) si y solo si \\(u \ge \bigvee S\\) para todo \\(S \in \mathcal{S}\\), si y solo si \\(u\\) acota a todo elemento de \\(\bigcup \mathcal{S}\\). Los dos conjuntos tienen las mismas cotas superiores y, por lo tanto, el mismo supremo.

**De álgebra a retículo.** Sea \\((A, a)\\) una \\(\mathcal{P}\\)-álgebra. La ley \\(a \circ \mathcal{P}(a) = a \circ \mu\_A\\), aplicada a una familia \\(\\{S\_i\\}\_{i \in I}\\), dice

\\[
a\Big(\bigcup\_{i} S\_i\Big) = a\big(\\{a(S\_i) \mid i \in I\\}\big). \qquad (\dagger)
\\]

Junto con \\(a(\\{x\\}) = x\\), esto permite reemplazar cualquier pedazo de un conjunto por su valor. Se define \\(x \le y\\) si \\(a(\\{x, y\\}) = y\\).

- *Reflexiva:* \\(a(\\{x, x\\}) = a(\\{x\\}) = x\\).
- *Antisimétrica:* si \\(a(\\{x, y\\}) = y\\) y \\(a(\\{y, x\\}) = x\\), entonces \\(x = y\\).
- *Transitiva:* sean \\(x \le y\\) y \\(y \le z\\). Por \\((\dagger)\\), \\(a(\\{x, y, z\\}) = a(\\{a(\\{x,y\\}), a(\\{y,z\\})\\}) = a(\\{y, z\\}) = z\\), al escribir \\(\\{x,y,z\\} = \\{x,y\\} \cup \\{y,z\\}\\). También \\(a(\\{x, y, z\\}) = a(\\{a(\\{x\\}), a(\\{y, z\\})\\}) = a(\\{x, z\\})\\). Luego \\(a(\\{x, z\\}) = z\\).

Ahora se ve que \\(a(S)\\) es el supremo de \\(S\\).

- *Cota superior:* para \\(s \in S\\), \\(a(\\{s, a(S)\\}) = a(\\{a(\\{s\\}), a(S)\\}) = a(\\{s\\} \cup S) = a(S)\\). Luego \\(s \le a(S)\\).
- *La menor:* sea \\(u\\) con \\(s \le u\\) para todo \\(s \in S\\), es decir, \\(a(\\{s, u\\}) = u\\). Como \\(S \cup \\{u\\} = \\{u\\} \cup \bigcup\_{s \in S} \\{s, u\\}\\), la regla \\((\dagger)\\) da \\(a(S \cup \\{u\\}) = a(\\{u\\}) = u\\). Por otro lado, \\(a(\\{a(S), u\\}) = a(\\{a(S), a(\\{u\\})\\}) = a(S \cup \\{u\\})\\). Luego \\(a(\\{a(S), u\\}) = u\\), es decir, \\(a(S) \le u\\).

Así, todo subconjunto de \\(A\\) tiene supremo, y \\(A\\) es un retículo completo. (Los ínfimos existen también: el ínfimo de \\(S\\) es el supremo del conjunto de cotas inferiores de \\(S\\).)

**Las construcciones son inversas.** Si se parte de un retículo, \\(a(\\{x,y\\}) = x \vee y\\), y \\(x \vee y = y\\) si y solo si \\(x \le y\\): se recupera el orden. Si se parte de un álgebra, se acaba de ver que el supremo en el orden inducido es \\(a(S)\\): se recupera \\(a\\).

**Morfismos.** Una función \\(h\colon A \to B\\) es un morfismo de álgebras si \\(h \circ a = b \circ \mathcal{P}(h)\\), es decir, si \\(h(\bigvee S) = \bigvee h(S)\\) para todo \\(S \subseteq A\\). Esas son las funciones que preservan supremos arbitrarios. (Son monótonas, pues \\(x \le y\\) implica \\(h(y) = h(x \vee y) = h(x) \vee h(y)\\), pero en general no preservan ínfimos.) \\(\blacksquare\\)

**Idea clave:** la ley de asociatividad \\((\dagger)\\) dice que un supremo se puede calcular por bloques; de ahí salen el orden y todas sus propiedades.

---

### Ejercicio 8

*\\(T(X) = M \times X\\), para un monoide \\(M\\), es una mónada; sus álgebras son los \\(M\\)-conjuntos.*

**Funtor y naturalidad.** Se define \\(T(f) = 1\_M \times f\\), es decir, \\(T(f)(m, x) = (m, f(x))\\). Es un funtor. La naturalidad de \\(\eta\\) es \\(T(f)(e, x) = (e, f(x)) = \eta\_Y(f(x))\\). La de \\(\mu\\) es

\\[
T(f)\big(\mu\_X(m, (n, x))\big) = (mn, f(x)) = \mu\_Y\big(m, (n, f(x))\big) = \mu\_Y\big(TT(f)(m, (n, x))\big).
\\]

**Asociatividad.** Para \\((m, (n, (p, x))) \in TTTX\\):

\\[
\mu\_X \circ T(\mu\_X)\colon (m, (n, (p, x))) \mapsto (m, (np, x)) \mapsto (m(np), x),
\\]

\\[
\mu\_X \circ \mu\_{TX}\colon (m, (n, (p, x))) \mapsto (mn, (p, x)) \mapsto ((mn)p, x).
\\]

En la segunda línea, \\(\mu\_{TX}\\) trata a \\((p, x)\\) como un elemento de \\(TX\\). Las dos coinciden por la asociatividad de \\(M\\).

**Unidad.** \\(\mu\_X(\eta\_{TX}(m, x)) = \mu\_X(e, (m, x)) = (em, x) = (m, x)\\) y \\(\mu\_X(T(\eta\_X)(m, x)) = \mu\_X(m, (e, x)) = (me, x) = (m, x)\\).

**Álgebras.** Un álgebra es un conjunto \\(A\\) con \\(a\colon M \times A \to A\\). Se escribe \\(m \cdot x = a(m, x)\\). Las dos ecuaciones de la Definición 10.10 son

\\[
a(\eta\_A(x)) = e \cdot x = x, \qquad a(T(a)(m, (n, x))) = m \cdot (n \cdot x) = (mn) \cdot x = a(\mu\_A(m, (n, x))).
\\]

Son exactamente los axiomas de una acción (izquierda) de \\(M\\) sobre \\(A\\). Un morfismo \\(h\colon (A, a) \to (B, b)\\) cumple \\(h \circ a = b \circ (1\_M \times h)\\), es decir, \\(h(m \cdot x) = m \cdot h(x)\\): es una función equivariante. Así, \\(\mathbf{Set}^T\\) es la categoría de \\(M\\)-conjuntos. \\(\blacksquare\\)

La solución seleccionada del final de la Parte V es correcta; aquí se agregaron la naturalidad y la descripción de los morfismos.

---

### Ejercicio 9

*Una adjunción para la mónada de elementos opcionales; sus categorías de Kleisli y de Eilenberg–Moore son equivalentes. Para las listas, no.*

**La adjunción.** Sea \\(\mathbf{Set}\_\ast\\) la categoría de conjuntos punteados \\((Y, y\_0)\\) con funciones que preservan el punto. Sean \\(F(X) = (X + \\{\bot\\}, \bot)\\) y \\(U(Y, y\_0) = Y\\). Una función punteada \\(X + \\{\bot\\} \to Y\\) está obligada a enviar \\(\bot \mapsto y\_0\\), así que queda determinada por su restricción a \\(X\\), que es arbitraria:

\\[
\mathbf{Set}\_\ast\big(F X, (Y, y\_0)\big) \cong \mathbf{Set}(X, Y).
\\]

La biyección es la restricción a lo largo de la inclusión, natural en ambos argumentos, así que \\(F \dashv U\\). La unidad \\(\eta\_X\colon X \to X + \\{\bot\\}\\) es la inclusión. La counidad \\(\varepsilon\_{(Y, y\_0)}\colon (Y + \\{\bot\\}, \bot) \to (Y, y\_0)\\) es la identidad en \\(Y\\) y envía \\(\bot \mapsto y\_0\\). Por el Teorema 10.8, la mónada es \\(UF(X) = X + \\{\bot\\}\\) con \\(\mu\_X = U(\varepsilon\_{FX})\\). Esta función \\((X + \\{\bot\\}) + \\{\bot\\} \to X + \\{\bot\\}\\) envía el punto nuevo al punto base \\(\bot\\) de \\(FX\\): es la mónada del Ejemplo 10.4.

**Kleisli.** Una flecha \\(X \rightsquigarrow Y\\) es una función \\(f\colon X \to Y + \\{\bot\\}\\), es decir, una función parcial con dominio \\(\\{x \mid f(x) \neq \bot\\}\\). La composición \\(\mu\_Z \circ T(g) \circ f\\) vale \\(g(f(x))\\) si \\(f(x) \neq \bot\\) y vale \\(\bot\\) si no. Es la composición de funciones parciales (Ejemplo 11.3).

**Eilenberg–Moore.** Un álgebra \\(a\colon A + \\{\bot\\} \to A\\) cumple \\(a \circ \eta\_A = 1\_A\\), así que \\(a\\) es la identidad en \\(A\\) y queda determinada por el punto \\(a\_0 = a(\bot)\\). La segunda ecuación es automática. En \\(TTA = A + \\{\bot\_1, \bot\_2\\}\\), las dos funciones \\(a \circ T(a)\\) y \\(a \circ \mu\_A\\) fijan \\(A\\) y envían \\(\bot\_1\\) y \\(\bot\_2\\) a \\(a\_0\\). Un morfismo \\(h\colon (A, a) \to (B, b)\\) cumple \\(h \circ a = b \circ T(h)\\); en \\(A\\) esto no dice nada, y en \\(\bot\\) dice \\(h(a\_0) = b\_0\\). Luego \\(\mathbf{Set}^T \cong \mathbf{Set}\_\ast\\).

**La equivalencia.** Sea \\(K\colon \mathbf{Set}\_T \to \mathbf{Set}^T\\) el funtor de comparación, con \\(K(X) = (TX, \mu\_X)\\) y \\(K(f) = \mu\_Y \circ T(f)\\) para \\(f\colon X \to TY\\). Para cualquier mónada:

- \\(K\\) es un funtor: \\(K(\eta\_X) = \mu\_X \circ T(\eta\_X) = 1\\), y
  \\[
  K(g \circ\_T f) = \mu\_Z \circ T(\mu\_Z) \circ TT(g) \circ T(f) = \mu\_Z \circ \mu\_{TZ} \circ TT(g) \circ T(f) = \mu\_Z \circ T(g) \circ \mu\_Y \circ T(f) = K(g) \circ K(f),
  \\]
  por la asociatividad y la naturalidad de \\(\mu\\).
- \\(K\\) es plenamente fiel: con la notación del Ejercicio 6, \\(K(f) = f^\sharp\\) para el álgebra \\((TY, \mu\_Y)\\). Por ese ejercicio, \\(f \mapsto f^\sharp\\) es una biyección \\(\mathcal{C}(X, TY) \to \mathcal{C}^T\big((TX, \mu\_X), (TY, \mu\_Y)\big)\\).

Para la mónada de elementos opcionales, \\(K\\) es además esencialmente sobreyectivo. Todo conjunto punteado \\((A, a\_0)\\) es isomorfo a \\(K(A \setminus \\{a\_0\\}) = \big((A \setminus \\{a\_0\\}) + \\{\bot\\}, \bot\big)\\), mediante la biyección que envía \\(\bot \mapsto a\_0\\) y fija lo demás. Por el Teorema 3.11, \\(K\\) es una equivalencia. En palabras: una función parcial \\(X \to Y\\) es lo mismo que una función punteada \\(X + \\{\bot\\} \to Y + \\{\bot\\}\\), y **todo conjunto punteado es libre**.

**Listas.** Por el Teorema 10.11, \\(\mathbf{Set}^L \cong \mathbf{Mon}\\). En la categoría de Kleisli, \\(\mathbf{Set}\_L(X, Y) = \mathbf{Set}(X, L(Y))\\). Este conjunto tiene un solo elemento si \\(X = \emptyset\\). Tiene también uno solo si \\(X \neq \emptyset\\) y \\(Y = \emptyset\\), porque \\(L(\emptyset) = \\{()\\}\\). Es infinito si \\(X\\) y \\(Y\\) son no vacíos, porque \\(L(Y)\\) es infinito. Así, **todo conjunto de flechas de \\(\mathbf{Set}\_L\\) tiene uno o una infinidad de elementos**.

En \\(\mathbf{Mon}\\), en cambio, el monoide \\(\mathbb{Z}/2 = \\{0, 1\\}\\) tiene exactamente dos endomorfismos: un homomorfismo envía \\(0 \mapsto 0\\) y \\(1\\) a un elemento \\(x\\) con \\(x + x = 0\\), y ambos elementos sirven. Una equivalencia \\(G\colon \mathbf{Mon} \to \mathbf{Set}\_L\\) es plenamente fiel (Teorema 3.11), así que daría una biyección entre \\(\mathbf{Mon}(\mathbb{Z}/2, \mathbb{Z}/2)\\), de dos elementos, y un conjunto de flechas de \\(\mathbf{Set}\_L\\), que tiene uno o una infinidad. Esto es imposible. Luego **\\(\mathbf{Set}\_L\\) y \\(\mathbf{Mon}\\) no son equivalentes por ningún funtor**, no solo por \\(K\\). En particular, \\(\mathbb{Z}/2\\) no es libre: un monoide libre \\(L(X)\\) tiene un elemento o una infinidad. \\(\blacksquare\\)

La guía del final de la Parte V es correcta. Con el argumento de cardinalidad se cierra la cuestión que dejaba abierta: que no exista ninguna equivalencia, y no solo que \\(K\\) no lo sea.

**Idea clave:** la comparación de Kleisli en Eilenberg–Moore siempre es plenamente fiel; es una equivalencia exactamente cuando toda álgebra es isomorfa a una libre.

---

### Ejercicio 10

*La mónada de excepciones \\(T(X) = X + E\\) y sus álgebras.*

**La mónada.** Se escribe \\(TX = X + E\\) y \\(T(f) = f + 1\_E\\): \\(f\\) en \\(X\\) y la identidad en \\(E\\). Para distinguir las copias de \\(E\\), \\(TTX = X + E\_1 + E\_2\\), con \\(E\_1\\) la copia interior y \\(E\_2\\) la exterior. Para \\(e \in E\\), \\(e\_i\\) denota su copia en \\(E\_i\\).

- \\(\eta\_X\colon X \to X + E\\) es la inclusión;
- \\(\mu\_X\colon X + E\_1 + E\_2 \to X + E\\) fija \\(X\\) y envía \\(e\_1 \mapsto e\\) y \\(e\_2 \mapsto e\\): "un error en cualquier etapa es ese error".

La naturalidad es directa: \\(T(f) \circ \eta\_X = \eta\_Y \circ f\\), y \\(T(f) \circ \mu\_X\\) y \\(\mu\_Y \circ TT(f)\\) envían \\(x \mapsto f(x)\\) y \\(e\_i \mapsto e\\).

*Unidad.* \\(\eta\_{TX}\\) envía \\(x \mapsto x\\) y \\(e \mapsto e\_1\\); \\(T(\eta\_X)\\) envía \\(x \mapsto x\\) y \\(e \mapsto e\_2\\). Al aplicar \\(\mu\_X\\) se obtiene, en ambos casos, la identidad de \\(X + E\\).

*Asociatividad.* Sea \\(TTTX = X + E\_1 + E\_2 + E\_3\\). Entonces \\(T(\mu\_X)\\) envía \\(e\_1, e\_2 \mapsto e\_1\\) y \\(e\_3 \mapsto e\_2\\), mientras que \\(\mu\_{TX}\\) envía \\(e\_1 \mapsto e\_1\\) y \\(e\_2, e\_3 \mapsto e\_2\\). Ambas fijan \\(X\\). Después de \\(\mu\_X\\), las dos composiciones fijan \\(X\\) y envían \\(e\_i \mapsto e\\) para \\(i = 1, 2, 3\\). Luego \\(\mu\_X \circ T(\mu\_X) = \mu\_X \circ \mu\_{TX}\\).

Con \\(E = \\{\bot\\}\\) se recupera el Ejercicio 1.

**Álgebras.** Sea \\(a\colon A + E \to A\\) un álgebra. La ecuación \\(a \circ \eta\_A = 1\_A\\) dice que \\(a\\) es la identidad en \\(A\\). Así, \\(a\\) queda determinada por la función \\(\varphi = a|\_E\colon E \to A\\). La segunda ecuación es automática. En \\(TTA = A + E\_1 + E\_2\\), las dos funciones \\(a \circ T(a)\\) y \\(a \circ \mu\_A\\) fijan \\(A\\) y envían \\(e\_1\\) y \\(e\_2\\) a \\(\varphi(e)\\). Para \\(e\_1\\): \\(T(a)(e\_1) = a(e) = \varphi(e) \in A\\), y luego \\(a(\varphi(e)) = \varphi(e)\\). Para \\(e\_2\\): \\(T(a)(e\_2) = e\\), y luego \\(a(e) = \varphi(e)\\).

Por lo tanto, **un álgebra es un conjunto \\(A\\) con una función arbitraria \\(\varphi\colon E \to A\\)**: un conjunto con \\(|E|\\) constantes distinguidas, sin ecuaciones entre ellas. Un morfismo \\(h\colon (A, \varphi) \to (B, \psi)\\) cumple \\(h \circ a = b \circ (h + 1\_E)\\), es decir, \\(h \circ \varphi = \psi\\). La categoría de Eilenberg–Moore es la categoría de conjuntos bajo \\(E\\), la categoría coma \\(E \downarrow \mathbf{Set}\\). La lectura computacional: un álgebra es un tipo de resultados que sabe "manejar" cada excepción \\(e\\) reemplazándola por un valor \\(\varphi(e)\\). \\(\blacksquare\\)

Como en el Ejercicio 9, la mónada proviene de la adjunción \\(X \mapsto (X + E, \text{inclusión de } E)\\), adjunta izquierda del olvidadizo \\(E \downarrow \mathbf{Set} \to \mathbf{Set}\\). Para \\(E = \emptyset\\), la mónada es la identidad y sus álgebras son los conjuntos.
