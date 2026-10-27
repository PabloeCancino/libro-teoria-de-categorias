# Soluciones de la Parte III

Soluciones completas de los ejercicios de nivel 1 y 2 de los capítulos 6 y 7 (límites, colímites, existencia y preservación). Conviene intentar cada ejercicio antes de leer su solución.

Una convención que se usa varias veces: un cono sobre un coespán \\(A \xrightarrow{f} C \xleftarrow{g} B\\) tiene tres componentes, pero la componente hacia \\(C\\) queda forzada: es \\(f \circ x = g \circ y\\). Así, un cono es un par \\((x\colon X \to A, \ y\colon X \to B)\\) con \\(f \circ x = g \circ y\\), y la Definición 6.6 coincide con la Definición 6.2 para esa forma.

---

## Nivel 1

### Ejercicio 1

*Ecualizador en Set de \\(f(x) = x^2\\) y \\(g(x) = x + 2\\); qué es "resolver una ecuación".*

Por el Ejemplo 6.4, el ecualizador es el conjunto

\\[
E = \\{x \in \mathbb{R} \mid x^2 = x + 2\\} = \\{x \in \mathbb{R} \mid (x - 2)(x + 1) = 0\\} = \\{-1, 2\\},
\\]

con la inclusión \\(e\colon E \to \mathbb{R}\\). Se verifica la propiedad universal. Claramente \\(f \circ e = g \circ e\\). Si \\(h\colon X \to \mathbb{R}\\) cumple \\(f \circ h = g \circ h\\), entonces \\(h(t)^2 = h(t) + 2\\) para todo \\(t \in X\\), es decir, \\(h(t) \in E\\). La función \\(\bar{h}\colon X \to E\\), \\(t \mapsto h(t)\\), cumple \\(e \circ \bar{h} = h\\), y es la única porque \\(e\\) es inyectiva, luego monomorfismo (Proposición 1.13). \\(\blacksquare\\)

**Qué es resolver una ecuación.** Una ecuación \\(f(x) = g(x)\\) es un par paralelo \\(f, g\colon A \rightrightarrows B\\). La propiedad universal dice que, para todo \\(X\\),

\\[
\mathbf{Set}(X, E) \cong \\{h\colon X \to A \mid f \circ h = g \circ h\\}.
\\]

El lado derecho es el conjunto de las **soluciones con parámetro \\(X\\)** (elementos generalizados de forma \\(X\\) que satisfacen la ecuación). Con \\(X = \\{\star\\}\\) se recuperan las soluciones usuales. El ecualizador existe siempre en \\(\mathbf{Set}\\), y es único salvo isomorfismo único; por eso "resolver" no es probar que existe, sino **dar una descripción explícita del objeto que representa a las soluciones**, aquí el conjunto \\(\\{-1, 2\\}\\). Decir "las soluciones son \\(-1\\) y \\(2\\)" es exhibir un isomorfismo entre \\(E\\) y un objeto concreto.

---

### Ejercicio 2

*El núcleo de \\(T\colon V \to W\\) ecualiza \\(T\\) y \\(0\\); el conúcleo \\(W/\mathrm{im}\\, T\\) los coecualiza.*

**Núcleo.** Sea \\(K = \ker T = \\{v \in V \mid T v = 0\\}\\), con la inclusión \\(i\colon K \to V\\), que es lineal. Se tiene \\(T \circ i = 0 = 0 \circ i\\). Sea \\(h\colon X \to V\\) lineal con \\(T \circ h = 0 \circ h\\). Como \\(0 \circ h = 0\\), se tiene \\(T(h(x)) = 0\\) para todo \\(x\\), luego \\(h(X) \subseteq K\\). La correstricción \\(\bar{h}\colon X \to K\\), \\(x \mapsto h(x)\\), es lineal porque las operaciones de \\(K\\) son las de \\(V\\), y cumple \\(i \circ \bar{h} = h\\). Es única: si \\(i \circ \bar{h} = i \circ \bar{h}'\\), la inyectividad de \\(i\\) da \\(\bar{h} = \bar{h}'\\).

**Conúcleo.** Sea \\(q\colon W \to W/\mathrm{im}\\, T\\) la proyección al cociente. Para \\(v \in V\\), \\(q(T v) = 0\\) porque \\(T v \in \mathrm{im}\\, T\\); luego \\(q \circ T = 0 = q \circ 0\\). Sea \\(k\colon W \to Z\\) lineal con \\(k \circ T = k \circ 0 = 0\\), es decir, \\(k\\) se anula en \\(\mathrm{im}\\, T\\). Se define

\\[
\bar{k}\colon W/\mathrm{im}\\, T \to Z, \qquad \bar{k}(w + \mathrm{im}\\, T) = k(w).
\\]

Está bien definida: si \\(w - w' = T v\\), entonces \\(k(w) - k(w') = k(T v) = 0\\). Es lineal porque \\(k\\) lo es, y cumple \\(\bar{k} \circ q = k\\). Es única porque \\(q\\) es sobreyectiva: dos funciones que coinciden después de \\(q\\) coinciden en cada clase. \\(\blacksquare\\)

**Idea clave:** en \\(\mathbf{Vect}\_k\\), ecualizar \\(T\\) con \\(0\\) es anularse después de \\(T\\), y coecualizarlos es anularse en la imagen de \\(T\\).

---

### Ejercicio 3

*La fibra \\(f^{-1}(y)\\) como producto fibrado.*

Se ve el elemento \\(y\\) como la función \\(y\colon \\{\star\\} \to Y\\), \\(\star \mapsto y\\). Sea \\(i\colon f^{-1}(y) \to X\\) la inclusión y \\(!\colon f^{-1}(y) \to \\{\star\\}\\) la única función. El cuadrado es

\\[
\require{AMScd}
\begin{CD}
f^{-1}(y) @>{!}>> \\{\star\\} \\\\
@V{i}VV @VV{y}V \\\\
X @>>{f}> Y
\end{CD}
\\]

Conmuta: para \\(x \in f^{-1}(y)\\), \\(f(i(x)) = y = y(!(x))\\).

Es universal. Sea \\(Z\\) un conjunto con \\(a\colon Z \to X\\) y \\(b\colon Z \to \\{\star\\}\\) tales que \\(f \circ a = y \circ b\\). Como \\(y \circ b\\) es la función constante \\(y\\), esto dice que \\(f(a(z)) = y\\) para todo \\(z\\), es decir, \\(a(Z) \subseteq f^{-1}(y)\\). La correstricción \\(u\colon Z \to f^{-1}(y)\\) de \\(a\\) cumple \\(i \circ u = a\\), y \\(! \circ u = b\\) porque hay una sola función \\(Z \to \\{\star\\}\\). Es única porque \\(i\\) es inyectiva. Luego \\(f^{-1}(y) \cong X \times\_Y \\{\star\\}\\). \\(\blacksquare\\)

La fórmula del Ejemplo 6.7 da lo mismo: \\(\\{(x, \star) \mid f(x) = y\\}\\), que está en biyección con \\(f^{-1}(y)\\). Si \\(y \notin f(X)\\), la fibra es \\(\emptyset\\), y el cuadrado sigue siendo un producto fibrado.

---

### Ejercicio 4

*En un orden parcial, el producto fibrado de \\(a \le c\\) y \\(b \le c\\) es \\(a \wedge b\\).*

En un orden parcial hay a lo más una flecha entre dos objetos, así que **todo diagrama conmuta**. Un cono sobre el coespán \\(a \to c \leftarrow b\\) es entonces un objeto \\(x\\) con \\(x \le a\\) y \\(x \le b\\); la condición de conmutatividad se cumple sola, y la flecha \\(x \le c\\) se sigue por transitividad.

Un producto fibrado es un cono \\(p\\) (es decir, \\(p \le a\\), \\(p \le b\\)) tal que todo cono \\(x\\) cumple \\(x \le p\\); la unicidad de la factorización es automática. Esto dice exactamente:

\\[
x \le a \ \text{y} \ x \le b \iff x \le p,
\\]

que es la propiedad del ínfimo (Ejemplo 4.5). Luego el producto fibrado existe si y solo si existe \\(a \wedge b\\), y en ese caso es \\(a \wedge b\\). \\(\blacksquare\\)

**Papel de \\(c\\).** Ninguno, salvo garantizar que el coespán exista. El resultado no depende de \\(c\\): el producto fibrado sobre cualquier cota superior común coincide con el producto \\(a \wedge b\\). Esto ocurre porque en un orden la condición "el cuadrado conmuta" es vacía. En categorías como \\(\mathbf{Set}\\), en cambio, la condición \\(f(a) = g(b)\\) es la que distingue \\(A \times\_C B\\) de \\(A \times B\\).

---

### Ejercicio 5

*El coecualizador en Top que produce \\(S^1\\) a partir de \\([0,1]\\).*

Sean \\(f\_0, f\_1\colon \\{\star\\} \rightrightarrows [0,1]\\) las funciones \\(f\_0(\star) = 0\\) y \\(f\_1(\star) = 1\\). Por el Ejemplo 6.9, su coecualizador en \\(\mathbf{Top}\\) es el cociente \\(Q = [0,1]/\sim\\) por la relación de equivalencia generada por \\(0 \sim 1\\), con la topología cociente y la proyección \\(q\colon [0,1] \to Q\\). Las clases son \\(\\{0, 1\\}\\) y los conjuntos \\(\\{t\\}\\) con \\(0 \lt t \lt 1\\).

Se demuestra que \\(Q \cong S^1\\). Sea \\(p\colon [0,1] \to S^1\\), \\(p(t) = (\cos 2\pi t, \sin 2\pi t)\\). Es continua y \\(p \circ f\_0 = p \circ f\_1\\), porque \\(p(0) = p(1)\\). Por la propiedad universal hay una única función continua \\(\bar{p}\colon Q \to S^1\\) con \\(\bar{p} \circ q = p\\).

- \\(\bar{p}\\) es sobreyectiva, porque \\(p\\) lo es.
- \\(\bar{p}\\) es inyectiva: si \\(p(s) = p(t)\\) con \\(s \neq t\\) en \\([0,1]\\), entonces \\(s - t\\) es un entero no nulo, luego \\(\\{s, t\\} = \\{0, 1\\}\\), y \\(q(s) = q(t)\\).
- \\(Q = q([0,1])\\) es compacto y \\(S^1\\) es de Hausdorff. Una biyección continua de un compacto en un Hausdorff es un homeomorfismo.

Luego \\((S^1, p)\\) es también un coecualizador de \\(f\_0\\) y \\(f\_1\\), isomorfo a \\((Q, q)\\) por el isomorfismo \\(\bar{p}\\). \\(\blacksquare\\)

La propiedad universal dice: **una función continua \\(S^1 \to Z\\) es lo mismo que una función continua \\([0,1] \to Z\\) que toma el mismo valor en \\(0\\) y en \\(1\\)**. Es decir, un lazo es un camino cerrado, la identificación que se usa en todo el estudio de \\(\pi\_1\\).

---

## Nivel 2

### Ejercicio 6

*El producto fibrado de un monomorfismo es un monomorfismo.*

Sea el producto fibrado de \\(f\colon A \to C\\) y \\(g\colon B \to C\\), con \\(g\\) mono, como en la Definición 6.6: \\(f \circ p\_1 = g \circ p\_2\\). Sean \\(x, y\colon X \to P\\) con \\(p\_1 \circ x = p\_1 \circ y\\). Entonces

\\[
g \circ p\_2 \circ x = f \circ p\_1 \circ x = f \circ p\_1 \circ y = g \circ p\_2 \circ y,
\\]

y como \\(g\\) es mono, \\(p\_2 \circ x = p\_2 \circ y\\). Considérese el cono \\((X, \ p\_1 \circ x, \ p\_2 \circ x)\\), que conmuta porque \\(f \circ p\_1 \circ x = g \circ p\_2 \circ x\\). Tanto \\(x\\) como \\(y\\) lo factorizan: \\(p\_1 \circ y = p\_1 \circ x\\) y \\(p\_2 \circ y = p\_2 \circ x\\). Por la unicidad en la propiedad universal, \\(x = y\\). Luego \\(p\_1\\) es mono. \\(\blacksquare\\)

En \\(\mathbf{Set}\\) es el hecho de que la imagen inversa de un subconjunto es un subconjunto: si \\(g\\) es inyectiva, \\(P \cong f^{-1}(g(B))\\) y \\(p\_1\\) es la inclusión.

**Idea clave:** las proyecciones de un límite separan flechas; basta comprobar que \\(x\\) e \\(y\\) tienen las mismas dos proyecciones.

---

### Ejercicio 7

*Lema del pegado de productos fibrados.*

Se fija la notación. Sea el diagrama conmutativo

\\[
\require{AMScd}
\begin{CD}
A @>{f}>> B @>{g}>> C \\\\
@V{a}VV @V{b}VV @VV{c}V \\\\
D @>>{h}> E @>>{k}> F
\end{CD}
\\]

con \\(b \circ f = h \circ a\\) (cuadrado izquierdo) y \\(c \circ g = k \circ b\\) (cuadrado derecho). El rectángulo exterior, con lados \\(g \circ f\\), \\(a\\), \\(c\\) y \\(k \circ h\\), conmuta: \\(c \circ g \circ f = k \circ b \circ f = k \circ h \circ a\\).

En términos de conos:

- el cuadrado derecho es producto fibrado si para todo par \\((s\colon Z \to E, \ t\colon Z \to C)\\) con \\(k \circ s = c \circ t\\) hay una única \\(z\colon Z \to B\\) con \\(b \circ z = s\\) y \\(g \circ z = t\\);
- el izquierdo, si para todo par \\((x\colon Z \to D, \ z\colon Z \to B)\\) con \\(h \circ x = b \circ z\\) hay una única \\(w\colon Z \to A\\) con \\(a \circ w = x\\) y \\(f \circ w = z\\);
- el exterior, si para todo par \\((x\colon Z \to D, \ y\colon Z \to C)\\) con \\(k \circ h \circ x = c \circ y\\) hay una única \\(w\colon Z \to A\\) con \\(a \circ w = x\\) y \\(g \circ f \circ w = y\\).

Se supone que el cuadrado derecho es producto fibrado.

**(Izquierdo \\(\Rightarrow\\) exterior).** Sea \\((x, y)\\) con \\(k \circ h \circ x = c \circ y\\). El par \\((h \circ x, \ y)\\) es un cono sobre el coespán derecho, así que hay una única \\(z\colon Z \to B\\) con \\(b \circ z = h \circ x\\) y \\(g \circ z = y\\). Ahora \\((x, z)\\) es un cono sobre el coespán izquierdo, porque \\(h \circ x = b \circ z\\). Hay una única \\(w\\) con \\(a \circ w = x\\) y \\(f \circ w = z\\). Entonces \\(g \circ f \circ w = g \circ z = y\\): existe la factorización.

Unicidad: si \\(w'\\) cumple \\(a \circ w' = x\\) y \\(g \circ f \circ w' = y\\), sea \\(z' = f \circ w'\\). Entonces \\(b \circ z' = b \circ f \circ w' = h \circ a \circ w' = h \circ x\\) y \\(g \circ z' = y\\). Por la unicidad en el cuadrado derecho, \\(z' = z\\). Luego \\(w'\\) cumple \\(a \circ w' = x\\) y \\(f \circ w' = z\\), y por la unicidad en el cuadrado izquierdo, \\(w' = w\\).

**(Exterior \\(\Rightarrow\\) izquierdo).** Sea \\((x, z)\\) con \\(h \circ x = b \circ z\\). Entonces \\((x, \ g \circ z)\\) es un cono sobre el coespán exterior:

\\[
k \circ h \circ x = k \circ b \circ z = c \circ g \circ z.
\\]

Hay una única \\(w\\) con \\(a \circ w = x\\) y \\(g \circ f \circ w = g \circ z\\). Falta ver que \\(f \circ w = z\\). Las dos flechas \\(f \circ w\\) y \\(z\\), de \\(Z\\) en \\(B\\), factorizan el mismo cono \\((h \circ x, \ g \circ z)\\) del cuadrado derecho:

\\[
b \circ f \circ w = h \circ a \circ w = h \circ x = b \circ z, \qquad g \circ f \circ w = g \circ z.
\\]

Por la unicidad en el cuadrado derecho, \\(f \circ w = z\\). Unicidad de \\(w\\): si \\(a \circ w' = x\\) y \\(f \circ w' = z\\), entonces \\(g \circ f \circ w' = g \circ z\\), y la unicidad en el exterior da \\(w' = w\\). \\(\blacksquare\\)

En \\(\mathbf{Set}\\) el lema dice que tomar imagen inversa a lo largo de \\(h\\) y luego a lo largo de \\(k\\) es lo mismo que hacerlo a lo largo de \\(k \circ h\\): \\((k \circ h)^{-1}(T) = h^{-1}(k^{-1}(T))\\).

**Idea clave:** la hipótesis sobre el cuadrado derecho se usa siempre para lo mismo: para pasar de un cono sobre \\(F\\) a una flecha hacia \\(B\\), o para concluir que dos flechas hacia \\(B\\) son iguales.

---

### Ejercicio 8

*Objeto terminal y productos fibrados dan productos binarios, ecualizadores y todos los límites finitos.*

Sea \\(1\\) el objeto terminal y \\(!\_X\colon X \to 1\\) la flecha única.

**Productos binarios.** Sea \\(P\\), con \\(p\_1\colon P \to A\\) y \\(p\_2\colon P \to B\\), el producto fibrado de \\(!\_A\\) y \\(!\_B\\). Un cono sobre \\(A \to 1 \leftarrow B\\) es un par \\((x\colon X \to A, \ y\colon X \to B)\\) con \\(!\_A \circ x = !\_B \circ y\\), pero esta condición se cumple siempre, porque ambos lados son flechas \\(X \to 1\\). Luego los conos son **todos** los pares de flechas, y la propiedad universal del producto fibrado es literalmente la Definición 4.4. Así \\(P = A \times B\\).

**Ecualizadores.** Sean \\(f, g\colon A \rightrightarrows B\\). Con el producto \\(A \times B\\) ya construido, sea \\(P\\), con \\(p\_1, p\_2\colon P \to A\\), el producto fibrado de \\(\langle 1\_A, f \rangle\\) y \\(\langle 1\_A, g \rangle\colon A \to A \times B\\). La conmutatividad \\(\langle 1\_A, f \rangle \circ p\_1 = \langle 1\_A, g \rangle \circ p\_2\\) equivale, componente a componente, a

\\[
p\_1 = p\_2 \qquad \text{y} \qquad f \circ p\_1 = g \circ p\_2.
\\]

Sea \\(e = p\_1 = p\_2\\). Entonces \\(f \circ e = g \circ e\\). Si \\(h\colon X \to A\\) cumple \\(f \circ h = g \circ h\\), entonces \\(\langle 1\_A, f \rangle \circ h = \langle h, f h \rangle = \langle h, g h \rangle = \langle 1\_A, g \rangle \circ h\\), así que \\((h, h)\\) es un cono y existe una única \\(u\\) con \\(p\_1 \circ u = h\\) y \\(p\_2 \circ u = h\\); en particular \\(e \circ u = h\\). Si \\(u'\\) cumple \\(e \circ u' = h\\), entonces \\(p\_1 \circ u' = p\_2 \circ u' = h\\), y la unicidad da \\(u' = u\\). Luego \\(e\\) es el ecualizador.

**Productos finitos.** Por inducción sobre \\(n\\). El producto de la familia vacía es el objeto terminal: un cono sobre el diagrama vacío es solo un objeto \\(X\\), y la flecha única \\(X \to 1\\) lo factoriza. Si \\(P\_n\\), con proyecciones \\(\pi\_i\\), es producto de \\(A\_1, \dots, A\_n\\), entonces \\(P\_n \times A\_{n+1}\\), con proyecciones \\(\pi\_i \circ p\_1\\) (\\(i \le n\\)) y \\(p\_2\\), es producto de \\(A\_1, \dots, A\_{n+1}\\): dada una familia \\(f\_i\colon X \to A\_i\\), la flecha \\(\langle \langle f\_1, \dots, f\_n \rangle, f\_{n+1} \rangle\\) la factoriza, y si \\(h\\) también la factoriza, \\(p\_1 \circ h\\) factoriza \\((f\_1, \dots, f\_n)\\), luego es \\(\langle f\_1, \dots, f\_n \rangle\\), y \\(p\_2 \circ h = f\_{n+1}\\); así \\(h\\) es única.

**Límites finitos.** Sea \\(D\colon \mathcal{J} \to \mathcal{C}\\) con \\(\mathcal{J}\\) finita (finitos objetos y flechas). En la demostración del Teorema 7.2, los productos \\(P\\) y \\(Q\\) están indexados por los objetos y por las flechas de \\(\mathcal{J}\\), que son conjuntos finitos, y además se usa un ecualizador. La prueba no usa nada más, así que funciona igual con productos finitos. Luego \\(\mathcal{C}\\) tiene todos los límites finitos. \\(\blacksquare\\)

**Sobre la solución seleccionada.** La de la sección de ejercicios es correcta; aquí se completan dos pasos que allí se resumen: la verificación de la propiedad universal del ecualizador y la obtención de los productos finitos, que la versión finita del Teorema 7.2 necesita.

---

### Ejercicio 9

*\\(\mathbb{Z}\_p\\) es un dominio entero.*

**La estructura.** Por el Ejemplo 7.8, el olvidadizo \\(\mathbf{Ring} \to \mathbf{Set}\\) preserva límites, así que el conjunto subyacente de \\(\mathbb{Z}\_p\\) es el de las sucesiones compatibles (Ejemplo 6.8), y las proyecciones \\(\pi\_n\colon \mathbb{Z}\_p \to \mathbb{Z}/p^n\\) son homomorfismos de anillos. Se usan dos propiedades del límite:

- **(L1)** Un elemento queda determinado por sus componentes: \\(a = b\\) si y solo si \\(a\_n = b\_n\\) para todo \\(n\\). Como cada \\(\pi\_n\\) es homomorfismo, las operaciones son componente a componente: \\((ab)\_n = a\_n b\_n\\), y \\(1 = (1, 1, \dots)\\).
- **(L2)** Compatibilidad: si \\(m \le n\\), \\(a\_m\\) es la reducción de \\(a\_n\\) módulo \\(p^m\\) (se compone la cadena de reducciones).

**\\(\mathbb{Z}\_p\\) es conmutativo y no nulo.** La conmutatividad se sigue de (L1), porque cada \\(\mathbb{Z}/p^n\\) es conmutativo. Además \\(1 \neq 0\\), porque \\(1 \neq 0\\) en \\(\mathbb{Z}/p\\).

**Orden de un elemento no nulo.** Sea \\(a \neq 0\\). Por (L2), si \\(a\_n = 0\\) y \\(m \le n\\), entonces \\(a\_m = 0\\). Por (L1), algún \\(a\_N \neq 0\\), y entonces \\(a\_n \neq 0\\) para todo \\(n \ge N\\). Luego existe un entero \\(k \ge 0\\) tal que

\\[
a\_n = 0 \iff n \le k.
\\]

Sea \\(n \ge k + 1\\) y sea \\(\alpha \in \mathbb{Z}\\) un representante de \\(a\_n\\). Por (L2), \\(\alpha\\) reducido módulo \\(p^{k+1}\\) es \\(a\_{k+1} \neq 0\\) y, si \\(k \ge 1\\), reducido módulo \\(p^k\\) es \\(a\_k = 0\\). Luego \\(p^k \mid \alpha\\) (trivial si \\(k = 0\\)) y \\(p^{k+1} \nmid \alpha\\); es decir, \\(\alpha = p^k u\\) con \\(p \nmid u\\).

**No hay divisores de cero.** Sean \\(a, b \neq 0\\), con órdenes \\(k\\) y \\(l\\) como arriba, y sea \\(n = k + l + 1\\). Representantes de \\(a\_n\\) y \\(b\_n\\) son \\(p^k u\\) y \\(p^l w\\) con \\(p \nmid u\\), \\(p \nmid w\\). Como \\(p\\) es primo, \\(p \nmid u w\\). Entonces \\(p^{k+l} u w\\), que representa a \\(a\_n b\_n = (ab)\_n\\), no es divisible por \\(p^{k+l+1} = p^n\\). Así \\((ab)\_n \neq 0\\), y por (L1), \\(ab \neq 0\\). \\(\blacksquare\\)

**Qué se usó.** Del límite: (L1), que las proyecciones separan elementos y que las operaciones son componente a componente, y (L2), la compatibilidad, que permite hablar del orden \\(k\\) de un elemento. De cada \\(\mathbb{Z}/p^n\\): que todo elemento no nulo se escribe \\(p^j u\\) con \\(0 \le j \lt n\\) y \\(p \nmid u\\), y que los exponentes se suman al multiplicar porque \\(p\\) es primo.

Observe que para \\(n \ge 2\\) **ningún** \\(\mathbb{Z}/p^n\\) es dominio: \\(p \cdot p^{n-1} = 0\\). La propiedad no se hereda componente a componente; surge de la compatibilidad, que obliga a que un elemento no nulo tenga orden \\(k\\) fijo mientras \\(n\\) crece sin límite.

---

### Ejercicio 10

*\\(\mathbf{Grp}(\mathrm{colim}\\, D, H) \cong \lim\_j \mathbf{Grp}(D(j), H)\\); homomorfismos que salen de un producto libre amalgamado.*

La prueba vale en cualquier categoría \\(\mathcal{C}\\) localmente pequeña. Sea \\(D\colon \mathcal{J} \to \mathcal{C}\\) con colímite \\((\mathrm{colim}\\, D, (\iota\_j))\\), y sea \\(H\\) un objeto.

**El diagrama de la derecha.** La asignación \\(j \mapsto \mathcal{C}(D(j), H)\\) es un funtor \\(K\colon \mathcal{J}^{\mathrm{op}} \to \mathbf{Set}\\): a \\(u\colon j \to k\\) le corresponde la función \\(K(u)\colon \mathcal{C}(D(k), H) \to \mathcal{C}(D(j), H)\\), \\(\varphi \mapsto \varphi \circ D(u)\\). Por la fórmula de los límites en \\(\mathbf{Set}\\) (después del Teorema 7.2), aplicada a la forma \\(\mathcal{J}^{\mathrm{op}}\\),

\\[
\lim K = \\{(\varphi\_j)\_j \mid \varphi\_j\colon D(j) \to H, \ \varphi\_k \circ D(u) = \varphi\_j \ \text{para toda} \ u\colon j \to k\\}.
\\]

Es exactamente el conjunto de los **cocones** sobre \\(D\\) con vértice \\(H\\).

**La biyección.** Se define \\(\Theta\colon \mathcal{C}(\mathrm{colim}\\, D, H) \to \lim K\\), \\(\psi \mapsto (\psi \circ \iota\_j)\_j\\). La familia es un cocono porque \\(\iota\_k \circ D(u) = \iota\_j\\). La propiedad universal del colímite dice que todo cocono \\((\varphi\_j)\\) es \\((\psi \circ \iota\_j)\\) para una única \\(\psi\\): es decir, que \\(\Theta\\) es biyectiva. Es natural en \\(H\\): para \\(t\colon H \to H'\\), \\((t \circ \psi) \circ \iota\_j = t \circ (\psi \circ \iota\_j)\\). \\(\blacksquare\\)

También se obtiene por dualidad: \\(\mathrm{colim}\\, D\\) es el límite de \\(D^{\mathrm{op}}\\) en \\(\mathcal{C}^{\mathrm{op}}\\), y la Proposición 7.6 en \\(\mathcal{C}^{\mathrm{op}}\\) da \\(\mathcal{C}^{\mathrm{op}}(H, \lim D^{\mathrm{op}}) \cong \lim\_j \mathcal{C}^{\mathrm{op}}(H, D(j))\\), que es la misma afirmación.

**Producto libre amalgamado.** Sea \\(D\\) el espán \\(A \xleftarrow{f} C \xrightarrow{g} B\\) en \\(\mathbf{Grp}\\), con colímite \\(A \ast\_C B\\) (Ejemplo 6.10). El diagrama \\(K\\) es el coespán

\\[
\mathbf{Grp}(A, H) \xrightarrow{- \circ f} \mathbf{Grp}(C, H) \xleftarrow{- \circ g} \mathbf{Grp}(B, H),
\\]

y su límite es un producto fibrado de conjuntos: la componente en \\(C\\) queda forzada. Luego

\\[
\mathbf{Grp}(A \ast\_C B, H) \cong \\{(\varphi, \psi) \in \mathbf{Grp}(A, H) \times \mathbf{Grp}(B, H) \mid \varphi \circ f = \psi \circ g\\}.
\\]

**Un homomorfismo que sale de \\(A \ast\_C B\\) es un par de homomorfismos, uno en cada factor, que coinciden en \\(C\\).** Dos casos:

- Si \\(C\\) es trivial, la condición es vacía: \\(\mathbf{Grp}(A \ast B, H) \cong \mathbf{Grp}(A, H) \times \mathbf{Grp}(B, H)\\), la propiedad del coproducto.
- Sea \\(G = \mathbb{Z} \ast\_{\mathbb{Z}} \mathbb{Z}\\) con \\(f(n) = 2n\\) y \\(g(n) = 3n\\). Como \\(\mathbf{Grp}(\mathbb{Z}, H) \cong UH\\) (Ejemplo 5.2), un homomorfismo \\(G \to H\\) es un par de elementos \\((x, y)\\) de \\(H\\) con \\(x^2 = y^3\\). Así \\(G = \langle x, y \mid x^2 = y^3 \rangle\\): es el **grupo del nudo trébol**, que Seifert–van Kampen produce al descomponer su complemento.

**Idea clave:** las flechas que salen de un colímite forman un límite de conjuntos de flechas; el funtor hom contravariante convierte colímites en límites.
