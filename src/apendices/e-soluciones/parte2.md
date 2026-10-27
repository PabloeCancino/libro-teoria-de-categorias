# Soluciones de la Parte II

Soluciones completas de los ejercicios de nivel 1 y nivel 2 de la Parte II (Capítulos 4 y 5). Conviene intentar cada ejercicio antes de leer su solución.

---

## Nivel 1

### Ejercicio 1

*Objetos iniciales y terminales de \\(\mathbf{Pos}\\), \\(\mathbf{Mon}\\), los campos y \\((\mathbb{N}, \mid)\\).*

**\\(\mathbf{Pos}\\).** El orden vacío \\(\emptyset\\) es inicial: de \\(\emptyset\\) a cualquier \\(P\\) hay exactamente una función, la vacía, y es monótona por vacuidad. El orden con un punto \\(\\{\star\\}\\) es terminal: de cualquier \\(P\\) hay una única función \\(P \to \\{\star\\}\\), la constante, y es monótona porque \\(\star \le \star\\). No hay objeto cero: \\(\emptyset\\) no es terminal, porque no hay funciones de \\(\\{\star\\}\\) a \\(\emptyset\\).

**\\(\mathbf{Mon}\\).** El monoide trivial \\(\\{e\\}\\) es un objeto cero. Es inicial: un homomorfismo \\(\\{e\\} \to M\\) debe enviar el neutro en el neutro, y esa única función es un homomorfismo. Es terminal: la función constante \\(M \to \\{e\\}\\) es la única función y es un homomorfismo.

**Campos.** Los homomorfismos de campos son homomorfismos de anillos (envían \\(1\\) en \\(1\\)). Dos hechos:

1. Todo homomorfismo de campos \\(\varphi\colon K \to L\\) es inyectivo. Si \\(\varphi(a) = 0\\) con \\(a \neq 0\\), entonces \\(1 = \varphi(a a^{-1}) = \varphi(a)\varphi(a^{-1}) = 0\\) en \\(L\\), lo cual es imposible en un campo.
2. Por lo tanto, \\(K\\) y \\(L\\) tienen la misma característica: para \\(n \in \mathbb{Z}\\), \\(n \cdot 1\_L = \varphi(n \cdot 1\_K)\\), y por la inyectividad \\(n \cdot 1\_K = 0\\) si y solo si \\(n \cdot 1\_L = 0\\).

No hay objeto inicial. Si \\(I\\) lo fuera, habría flechas \\(I \to \mathbb{Q}\\) e \\(I \to \mathbb{F}\_2\\), y \\(I\\) tendría característica \\(0\\) y \\(2\\) a la vez. Por el mismo argumento, con flechas \\(\mathbb{Q} \to T\\) y \\(\mathbb{F}\_2 \to T\\), no hay objeto terminal.

Si se fija la característica, sí hay objeto inicial: el campo primo \\(\mathbb{Q}\\) o \\(\mathbb{F}\_p\\). Sigue sin haber terminal, porque un terminal \\(T\\) recibiría una flecha inyectiva desde cualquier campo de esa característica, en particular desde uno de cardinal mayor que el de \\(T\\), como el campo de funciones racionales en un conjunto de variables de cardinal mayor que el de \\(T\\).

**\\((\mathbb{N}, \mid)\\).** Se toma \\(0 \in \mathbb{N}\\). Es un orden parcial (la antisimetría vale porque los números son no negativos). En un orden parcial, inicial es mínimo y terminal es máximo (Ejemplo 4.3). Como \\(1 \mid n\\) para todo \\(n\\), \\(1\\) es inicial. Como \\(n \mid 0\\) para todo \\(n\\) (pues \\(0 = n \cdot 0\\)), \\(0\\) es terminal. Si se excluye el \\(0\\) de \\(\mathbb{N}\\), sigue habiendo inicial, \\(1\\), pero no terminal, porque ningún \\(n \geq 1\\) es divisible por \\(2n\\).

---

### Ejercicio 2

*Dos productos de \\(A\\) y \\(B\\) son isomorfos por un único isomorfismo compatible con las proyecciones.*

**Existencia y unicidad de \\(h\\).** Por la propiedad universal de \\(P\\), aplicada al par \\(\pi\_1'\colon P' \to A\\), \\(\pi\_2'\colon P' \to B\\), existe una única \\(h = \langle \pi\_1', \pi\_2' \rangle\colon P' \to P\\) con \\(\pi\_1 \circ h = \pi\_1'\\) y \\(\pi\_2 \circ h = \pi\_2'\\). Esto ya da la unicidad que pide el enunciado: cualquier flecha \\(P' \to P\\) compatible con las proyecciones es esta \\(h\\). Falta ver que \\(h\\) es isomorfismo.

**\\(h\\) es isomorfismo.** Por la propiedad universal de \\(P'\\), existe \\(k\colon P \to P'\\) con \\(\pi\_1' \circ k = \pi\_1\\) y \\(\pi\_2' \circ k = \pi\_2\\). Entonces

\\[
\pi\_1 \circ (h \circ k) = \pi\_1' \circ k = \pi\_1, \qquad \pi\_2 \circ (h \circ k) = \pi\_2' \circ k = \pi\_2.
\\]

La flecha \\(1\_P\\) también cumple \\(\pi\_1 \circ 1\_P = \pi\_1\\) y \\(\pi\_2 \circ 1\_P = \pi\_2\\). Por la unicidad en la propiedad universal de \\(P\\), aplicada al par \\((\pi\_1, \pi\_2)\\), se tiene \\(h \circ k = 1\_P\\). Intercambiando los papeles de \\(P\\) y \\(P'\\), \\(k \circ h = 1\_{P'}\\). \\(\blacksquare\\)

Es la Proposición 4.2 aplicada a la categoría de conos sobre \\(A\\) y \\(B\\) (Sección 4.5), donde los productos son los objetos terminales.

---

### Ejercicio 3

*Producto y coproducto en \\(\mathbf{B}M\\), con \\(M = (\mathbb{N}, +, 0)\\).*

**No existen.** La categoría tiene un único objeto \\(\star\\), así que el único producto posible es el de \\(\star\\) consigo mismo, y su vértice es necesariamente \\(\star\\). La composición es la suma: \\(m \circ n = m + n\\).

Supongamos que \\((\star, a, b)\\), con proyecciones \\(a, b \in \mathbb{N}\\), es un producto de \\(\star\\) y \\(\star\\). Para todo par \\(f, g \in \mathbb{N}\\) debería haber una única \\(h\\) con

\\[
a + h = f, \qquad b + h = g.
\\]

Tome \\(f = a\\) y \\(g = b + 1\\). La primera ecuación fuerza \\(h = 0\\), y entonces la segunda dice \\(b = b + 1\\), lo cual es falso. Luego no hay producto.

Para el coproducto, las ecuaciones son \\([f,g] \circ \iota\_1 = f\\) y \\([f,g] \circ \iota\_2 = g\\), es decir, \\(h + a = f\\) y \\(h + b = g\\). Como \\(+\\) es conmutativa, son las mismas ecuaciones, y el mismo argumento muestra que no hay coproducto. \\(\blacksquare\\)

El argumento solo usó que existe un \\(f\\) que fuerza \\(h\\) y un \\(g\\) incompatible con esa \\(h\\). La intuición: en \\(\mathbf{B}\mathbb{N}\\) hay "demasiado pocas" flechas para codificar pares.

---

### Ejercicio 4

*El funtor \\(C(G) = \\{(g,h) \in G \times G \mid gh = hg\\}\\) es representable.*

Primero, \\(C\\) es un funtor: un homomorfismo \\(f\colon G \to G'\\) envía pares que conmutan en pares que conmutan, porque \\(f(g)f(h) = f(gh) = f(hg) = f(h)f(g)\\). Se define \\(C(f)(g,h) = (f(g), f(h))\\), y la funtorialidad es inmediata.

Sean \\(e\_1 = (1,0)\\) y \\(e\_2 = (0,1)\\) en \\(\mathbb{Z}^2\\). Se afirma que \\(C \cong \mathbf{Grp}(\mathbb{Z}^2, -)\\), mediante

\\[
\theta\_G\colon \mathbf{Grp}(\mathbb{Z}^2, G) \to C(G), \qquad u \mapsto (u(e\_1), u(e\_2)).
\\]

**Bien definida.** \\(e\_1\\) y \\(e\_2\\) conmutan en \\(\mathbb{Z}^2\\), así que sus imágenes conmutan.

**Inyectiva.** Todo elemento de \\(\mathbb{Z}^2\\) es \\(m e\_1 + n e\_2\\), así que \\(u(m,n) = u(e\_1)^m u(e\_2)^n\\) queda determinado por \\(u(e\_1)\\) y \\(u(e\_2)\\).

**Sobreyectiva.** Dado \\((g, h) \in C(G)\\), sea \\(u(m,n) = g^m h^n\\). Como \\(g\\) y \\(h\\) conmutan, también conmutan sus potencias, y

\\[
u(m,n)\\, u(m',n') = g^m h^n g^{m'} h^{n'} = g^{m+m'} h^{n+n'} = u(m+m', n+n').
\\]

Luego \\(u\\) es un homomorfismo con \\(\theta\_G(u) = (g,h)\\).

**Natural.** Para \\(f\colon G \to G'\\), \\(\theta\_{G'}(f \circ u) = (f(u(e\_1)), f(u(e\_2))) = C(f)(\theta\_G(u))\\).

Por la Proposición 3.8, \\(\theta\\) es un isomorfismo natural. El objeto representante es \\(\mathbb{Z}^2\\) y, en el sentido del Corolario 5.7 (en su forma covariante), el elemento universal es \\((e\_1, e\_2) = \theta\_{\mathbb{Z}^2}(1\_{\mathbb{Z}^2})\\). \\(\blacksquare\\)

La solución seleccionada del archivo de ejercicios es correcta; aquí se añadieron la verificación de que \\(u\\) es homomorfismo, que es justo donde se usa la conmutación, y la naturalidad.

---

### Ejercicio 5

*Producto y coproducto de una familia infinita en \\((\mathbb{N}, \mid)\\).*

En un orden parcial, el producto de una familia \\((a\_i)\_{i \in I}\\) es su ínfimo y el coproducto, su supremo. El argumento es el del Ejemplo 4.5: un cono es un \\(x\\) con \\(x \le a\_i\\) para todo \\(i\\), la flecha hacia el vértice existe si y solo si \\(x\\) es menor o igual que él, y la unicidad es automática. Así que hay que calcular ínfimos y supremos en el orden de divisibilidad. Se usan ideales de \\(\mathbb{Z}\\): todo ideal es de la forma \\(d\mathbb{Z}\\) con un único \\(d \geq 0\\), y \\(a \mid b\\) si y solo si \\(b\mathbb{Z} \subseteq a\mathbb{Z}\\).

**Producto: el máximo común divisor, que siempre existe.** Sea \\(S = \\{a\_i\\}\\) y sea \\(d\mathbb{Z}\\) el ideal generado por \\(S\\), con \\(d \geq 0\\). Como cada \\(a\_i \in d\mathbb{Z}\\), \\(d \mid a\_i\\). Si \\(c \mid a\_i\\) para todo \\(i\\), entonces \\(S \subseteq c\mathbb{Z}\\), luego \\(d\mathbb{Z} \subseteq c\mathbb{Z}\\) y \\(c \mid d\\). Así, \\(d = \gcd(a\_i)\\) es el producto. Como el ideal generado por \\(S\\) es generado por finitos elementos de \\(S\\) (\\(d\\) es combinación entera de finitos \\(a\_i\\)), el máximo común divisor de la familia coincide con el de alguna subfamilia finita.

**Coproducto: el mínimo común múltiplo, que también siempre existe.** Sea \\(m\mathbb{Z} = \bigcap\_i a\_i\mathbb{Z}\\), con \\(m \geq 0\\); es un ideal por ser intersección de ideales. Como \\(m\mathbb{Z} \subseteq a\_i\mathbb{Z}\\), \\(a\_i \mid m\\). Si \\(a\_i \mid n\\) para todo \\(i\\), entonces \\(n \in \bigcap\_i a\_i\mathbb{Z} = m\mathbb{Z}\\) y \\(m \mid n\\). Así, \\(m\\) es el coproducto.

La novedad respecto del caso finito: \\(m\\) es \\(0\\) con frecuencia. Ocurre exactamente cuando la familia no tiene un múltiplo común positivo, es decir, cuando aparecen infinitos primos o un primo con exponentes no acotados. Por ejemplo:

- la familia de todos los primos tiene producto \\(1\\) y coproducto \\(0\\);
- la familia \\(2, 4, 8, \dots\\) tiene producto \\(2\\) y coproducto \\(0\\);
- la familia \\(6, 10, 15, 6, 10, 15, \dots\\) tiene producto \\(1\\) y coproducto \\(30\\).

Para la familia vacía, el producto es el terminal \\(0\\) y el coproducto es el inicial \\(1\\), lo cual coincide con las fórmulas (\\(d\\) genera el ideal \\(0\\) y la intersección vacía es \\(\mathbb{Z} = 1\mathbb{Z}\\)). En conclusión, \\((\mathbb{N}, \mid)\\) es un **retículo completo**.

Si se excluye el \\(0\\) de \\(\mathbb{N}\\), los productos siguen existiendo para familias no vacías, pero el coproducto de las dos primeras familias deja de existir.

---

## Nivel 2

### Ejercicio 6

*Naturalidad de la biyección de Yoneda en \\(A\\) y en \\(F\\).*

Notación: \\(\Phi\_{A,F}(\alpha) = \alpha\_A(1\_A)\\), y \\(y(u) = u \circ -\colon \mathcal{C}(-, A') \Rightarrow \mathcal{C}(-, A)\\) para \\(u\colon A' \to A\\) (Corolario 5.5). La transformación \\(y(u)\\) es natural por asociatividad: \\(u \circ (f \circ g) = (u \circ f) \circ g\\).

**Naturalidad en \\(A\\).** Las dos asignaciones \\(A \mapsto \mathrm{Nat}(\mathcal{C}(-,A), F)\\) y \\(A \mapsto F(A)\\) son funtores \\(\mathcal{C}^{\mathrm{op}} \to \mathbf{Set}\\). En el primero, \\(u\colon A' \to A\\) actúa por \\(\alpha \mapsto \alpha \cdot y(u)\\) (composición de transformaciones naturales, Sección 3.3); la funtorialidad viene de \\(y(u \circ u') = y(u) \cdot y(u')\\) y \\(y(1\_A) = 1\\). En el segundo, \\(u\\) actúa por \\(F(u)\\). Hay que ver que el cuadrado

\\[
\require{AMScd}
\begin{CD}
\mathrm{Nat}(\mathcal{C}(-,A), F) @>{\Phi\_{A,F}}>> F(A) \\\\
@V{- \cdot y(u)}VV @VV{F(u)}V \\\\
\mathrm{Nat}(\mathcal{C}(-,A'), F) @>>{\Phi\_{A',F}}> F(A')
\end{CD}
\\]

conmuta. Sea \\(\alpha\\) natural. Por el camino de abajo:

\\[
\Phi\_{A',F}(\alpha \cdot y(u)) = \alpha\_{A'}\big(y(u)\_{A'}(1\_{A'})\big) = \alpha\_{A'}(u \circ 1\_{A'}) = \alpha\_{A'}(u).
\\]

Por el camino de arriba, usando la naturalidad de \\(\alpha\\) respecto de \\(u\\), que es el paso (3) de la demostración del Teorema 5.4:

\\[
F(u)\big(\Phi\_{A,F}(\alpha)\big) = F(u)\big(\alpha\_A(1\_A)\big) = \alpha\_{A'}(1\_A \circ u) = \alpha\_{A'}(u).
\\]

Los dos resultados coinciden.

**Naturalidad en \\(F\\).** Las asignaciones \\(F \mapsto \mathrm{Nat}(\mathcal{C}(-,A), F)\\) y \\(F \mapsto F(A)\\) son funtores \\([\mathcal{C}^{\mathrm{op}}, \mathbf{Set}] \to \mathbf{Set}\\). Una transformación \\(\theta\colon F \Rightarrow F'\\) actúa en el primero por \\(\alpha \mapsto \theta \cdot \alpha\\) y en el segundo por \\(\theta\_A\\). El cuadrado

\\[
\require{AMScd}
\begin{CD}
\mathrm{Nat}(\mathcal{C}(-,A), F) @>{\Phi\_{A,F}}>> F(A) \\\\
@V{\theta \cdot -}VV @VV{\theta\_A}V \\\\
\mathrm{Nat}(\mathcal{C}(-,A), F') @>>{\Phi\_{A,F'}}> F'(A)
\end{CD}
\\]

conmuta, porque

\\[
\Phi\_{A,F'}(\theta \cdot \alpha) = (\theta \cdot \alpha)\_A(1\_A) = \theta\_A\big(\alpha\_A(1\_A)\big) = \theta\_A\big(\Phi\_{A,F}(\alpha)\big).
\\]

Aquí no hizo falta la naturalidad de nada: es la definición de la composición componente a componente. \\(\blacksquare\\)

*Las dos variables a la vez.* Para \\(u\colon A' \to A\\) y \\(\theta\colon F \Rightarrow F'\\), la combinación de los dos cálculos da

\\[
\Phi\_{A',F'}(\theta \cdot \alpha \cdot y(u)) = \theta\_{A'}(\alpha\_{A'}(u)) = \theta\_{A'}\big(F(u)(\alpha\_A(1\_A))\big) = F'(u)\big(\theta\_A(\alpha\_A(1\_A))\big),
\\]

donde la última igualdad es la naturalidad de \\(\theta\\) respecto de \\(u\\). Es la naturalidad conjunta en el par \\((A, F)\\).

**Idea clave:** la naturalidad en \\(A\\) es la naturalidad de \\(\alpha\\) evaluada en la identidad; la naturalidad en \\(F\\) es la definición de composición vertical.

---

### Ejercicio 7

*Versión covariante: \\(\mathrm{Nat}(\mathcal{C}(A, -), F) \cong F(A)\\) para \\(F\colon \mathcal{C} \to \mathbf{Set}\\).*

> **Enunciado.** Sea \\(\mathcal{C}\\) localmente pequeña, \\(F\colon \mathcal{C} \to \mathbf{Set}\\) un funtor y \\(A\\) un objeto. La función
>
> \\[
> \Phi\colon \mathrm{Nat}(\mathcal{C}(A, -), F) \to F(A), \qquad \alpha \mapsto \alpha\_A(1\_A),
> \\]
>
> es una biyección, con inversa \\(x \mapsto \Psi(x)\\), donde \\(\Psi(x)\_X\colon \mathcal{C}(A, X) \to F(X)\\), \\(f \mapsto F(f)(x)\\). La biyección es natural en \\(A\\) y en \\(F\\).

*Demostración.* Recuerde que \\(\mathcal{C}(A, g)\\), para \\(g\colon X \to Y\\), es \\(f \mapsto g \circ f\\) (Definición 2.12).

**(1) \\(\Psi(x)\\) es natural.** Para \\(g\colon X \to Y\\) y \\(f\colon A \to X\\), por la funtorialidad (covariante) de \\(F\\):

\\[
F(g)\big(\Psi(x)\_X(f)\big) = F(g)\big(F(f)(x)\big) = F(g \circ f)(x) = \Psi(x)\_Y(g \circ f) = \Psi(x)\_Y\big(\mathcal{C}(A,g)(f)\big).
\\]

**(2) \\(\Phi \circ \Psi = 1\\).** \\(\Phi(\Psi(x)) = F(1\_A)(x) = x\\).

**(3) \\(\Psi \circ \Phi = 1\\).** Sea \\(\alpha\\) natural y \\(f\colon A \to X\\). La naturalidad de \\(\alpha\\) respecto de \\(f\\) dice \\(F(f) \circ \alpha\_A = \alpha\_X \circ \mathcal{C}(A, f)\\). Al evaluar en \\(1\_A\\):

\\[
\Psi(\Phi(\alpha))\_X(f) = F(f)\big(\alpha\_A(1\_A)\big) = \alpha\_X(f \circ 1\_A) = \alpha\_X(f).
\\]

**Naturalidad.** En \\(F\\), el cálculo es idéntico al del Ejercicio 6. En \\(A\\), ahora ambos lados son **covariantes** en \\(A\\): \\(u\colon A \to A'\\) induce \\(\mathcal{C}(u, -) = - \circ u\colon \mathcal{C}(A', -) \Rightarrow \mathcal{C}(A, -)\\), luego \\(\alpha \mapsto \alpha \cdot \mathcal{C}(u,-)\\) va de \\(\mathrm{Nat}(\mathcal{C}(A,-),F)\\) a \\(\mathrm{Nat}(\mathcal{C}(A',-),F)\\), y del otro lado se tiene \\(F(u)\colon F(A) \to F(A')\\). Se verifica

\\[
(\alpha \cdot \mathcal{C}(u,-))\_{A'}(1\_{A'}) = \alpha\_{A'}(1\_{A'} \circ u) = \alpha\_{A'}(u) = F(u)\big(\alpha\_A(1\_A)\big),
\\]

donde la última igualdad es el paso (3) con \\(f = u\\). \\(\blacksquare\\)

*Prueba por dualidad.* El funtor \\(\mathcal{C}(A, -)\colon \mathcal{C} \to \mathbf{Set}\\) es exactamente el prehaz \\(\mathcal{C}^{\mathrm{op}}(-, A)\colon (\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} \to \mathbf{Set}\\), porque \\(\mathcal{C}^{\mathrm{op}}(X, A) = \mathcal{C}(A, X)\\) y \\((\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} = \mathcal{C}\\). Un funtor \\(F\colon \mathcal{C} \to \mathbf{Set}\\) es un prehaz sobre \\(\mathcal{C}^{\mathrm{op}}\\). El Teorema 5.4 aplicado a \\(\mathcal{C}^{\mathrm{op}}\\) da el enunciado, con las mismas fórmulas. La prueba directa anterior sirve para comprobar que la traducción es correcta.

**Corolario (encaje covariante).** Con \\(F = \mathcal{C}(B, -)\\): \\(\mathrm{Nat}(\mathcal{C}(A,-), \mathcal{C}(B,-)) \cong \mathcal{C}(B, A)\\). Observe que el sentido se invierte: una flecha \\(p\colon B \to A\\) da la transformación \\(\Psi(p) = - \circ p\colon \mathcal{C}(A, -) \Rightarrow \mathcal{C}(B, -)\\). Este corolario se usa en el Ejercicio 10.

---

### Ejercicio 8

*\\((A \times B) \times C \cong A \times (B \times C)\\) vía Yoneda.*

**Paso 1: la biyección del producto es natural.** Para objetos \\(A, B\\) con producto, sea

\\[
\lambda\_X\colon \mathcal{C}(X, A \times B) \to \mathcal{C}(X, A) \times \mathcal{C}(X, B), \qquad h \mapsto (\pi\_1 \circ h, \pi\_2 \circ h).
\\]

Es biyectiva por la Definición 4.4: la existencia de \\(\langle f, g \rangle\\) da la sobreyectividad y su unicidad, la inyectividad. Es natural en \\(X\\): para \\(v\colon X' \to X\\),

\\[
\lambda\_{X'}(h \circ v) = (\pi\_1 \circ h \circ v, \pi\_2 \circ h \circ v),
\\]

que es lo que se obtiene al aplicar primero \\(\lambda\_X\\) y luego precomponer con \\(v\\) en cada coordenada. Por la Proposición 3.8, \\(\lambda\colon \mathcal{C}(-, A \times B) \cong \mathcal{C}(-, A) \times \mathcal{C}(-, B)\\) es un isomorfismo natural de prehaces.

**Paso 2: los dos prehaces son isomorfos.** Sea \\(T = \mathcal{C}(-, A) \times \mathcal{C}(-, B) \times \mathcal{C}(-, C)\\), el prehaz de ternas, con acción coordenada a coordenada. Aplicando el Paso 1 dos veces:

\\[
\mathcal{C}(X, (A \times B) \times C) \cong \mathcal{C}(X, A \times B) \times \mathcal{C}(X, C) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B) \times \mathcal{C}(X, C),
\\]

\\[
h \mapsto (\pi\_1 h, \pi\_2 h) \mapsto (\pi\_1 \pi\_1 h, \ \pi\_2 \pi\_1 h, \ \pi\_2 h).
\\]

Cada paso es natural en \\(X\\) (el segundo es \\(\lambda\\) en la primera coordenada y la identidad en la segunda), y la identificación de \\((S \times S') \times S''\\) con las ternas también es natural, porque se actúa coordenada a coordenada. Lo mismo vale para \\(A \times (B \times C)\\), con \\(k \mapsto (\pi\_1 k, \ \pi\_1 \pi\_2 k, \ \pi\_2 \pi\_2 k)\\). Componiendo uno con el inverso del otro se obtiene un isomorfismo natural

\\[
\varphi\colon \mathcal{C}(-, (A \times B) \times C) \cong \mathcal{C}(-, A \times (B \times C)).
\\]

**Paso 3: Yoneda.** Por el Corolario 5.6, \\((A \times B) \times C \cong A \times (B \times C)\\). \\(\blacksquare\\)

**El isomorfismo explícito.** Escriba \\(P = (A \times B) \times C\\) y \\(Q = A \times (B \times C)\\). Por el Corolario 5.5, \\(\varphi = y(a)\\) para una única \\(a\colon P \to Q\\), y la prueba del lema dice que \\(a = \varphi\_P(1\_P)\\). Se sigue \\(1\_P\\) por el Paso 2:

\\[
1\_P \mapsto (\pi\_1 \pi\_1, \ \pi\_2 \pi\_1, \ \pi\_2) \mapsto \langle \pi\_1 \pi\_1, \langle \pi\_2 \pi\_1, \pi\_2 \rangle \rangle.
\\]

El último paso es encontrar la única \\(k\colon P \to Q\\) con \\(\pi\_1 k = \pi\_1 \pi\_1\\), \\(\pi\_1 \pi\_2 k = \pi\_2 \pi\_1\\) y \\(\pi\_2 \pi\_2 k = \pi\_2\\). Así,

\\[
a = \langle \pi\_1 \circ \pi\_1, \ \langle \pi\_2 \circ \pi\_1, \pi\_2 \rangle \rangle\colon (A \times B) \times C \to A \times (B \times C),
\\]

y su inverso, obtenido del mismo modo con \\(\varphi^{-1}\\), es \\(\langle \langle \pi\_1, \pi\_1 \circ \pi\_2 \rangle, \pi\_2 \circ \pi\_2 \rangle\\). Por el Corolario 5.6 no hace falta verificar a mano que son inversos: ya se sabe que \\(a\\) es un isomorfismo, porque \\(y(a) = \varphi\\) lo es y \\(y\\) es plenamente fiel.

La solución seleccionada del archivo de ejercicios es correcta.

**Idea clave:** para comparar dos objetos, se comparan sus prehaces representables, que viven en \\(\mathbf{Set}\\), donde la asociatividad del producto cartesiano es evidente.

---

### Ejercicio 9

*\\(A \times 1 \cong A\\).*

**Por Yoneda.** Para cada \\(X\\), \\(\mathcal{C}(X, 1)\\) tiene un solo elemento \\(!\_X\\). Entonces

\\[
\mathcal{C}(X, A \times 1) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, 1) = \mathcal{C}(X, A) \times \\{!\_X\\} \cong \mathcal{C}(X, A), \qquad h \mapsto \pi\_1 \circ h.
\\]

El primer isomorfismo es natural en \\(X\\) (Ejercicio 8, Paso 1), y el segundo, \\((f, !\_X) \mapsto f\\), también lo es. Por el Corolario 5.6, \\(A \times 1 \cong A\\). El isomorfismo es \\(\varphi\_{A \times 1}(1\_{A \times 1}) = \pi\_1\\).

**Directamente.** Sea \\(s = \langle 1\_A, !\_A \rangle\colon A \to A \times 1\\). Entonces \\(\pi\_1 \circ s = 1\_A\\). Para el otro compuesto, \\(s \circ \pi\_1\colon A \times 1 \to A \times 1\\) cumple

\\[
\pi\_1 \circ (s \circ \pi\_1) = 1\_A \circ \pi\_1 = \pi\_1, \qquad \pi\_2 \circ (s \circ \pi\_1) = !\_A \circ \pi\_1 = \pi\_2,
\\]

donde la segunda igualdad final vale porque \\(!\_A \circ \pi\_1\\) y \\(\pi\_2\\) son flechas \\(A \times 1 \to 1\\), y solo hay una. Como \\(1\_{A \times 1}\\) cumple las mismas dos ecuaciones, la unicidad en la propiedad universal da \\(s \circ \pi\_1 = 1\_{A \times 1}\\). Luego \\(\pi\_1\colon A \times 1 \to A\\) es un isomorfismo con inversa \\(s\\). \\(\blacksquare\\)

Con los Ejercicios 8 y 9 (y la simetría \\(A \times B \cong B \times A\\), que se prueba igual), el producto se comporta como una multiplicación asociativa y conmutativa con neutro \\(1\\), salvo isomorfismo.

---

### Ejercicio 10

*\\(U \times U\\) es representable por \\(\mathbb{Z}[x,y]\\) en \\(\mathbf{CRing}\\); la suma y el producto vienen de homomorfismos \\(\mathbb{Z}[t] \to \mathbb{Z}[x,y]\\); el caso de \\(\mathbf{Ring}\\).*

**Representabilidad.** La propiedad universal del anillo de polinomios dice: para cada anillo conmutativo \\(R\\) y cada par \\((a, b) \in R \times R\\), hay un único homomorfismo \\(\mathrm{ev}\_{a,b}\colon \mathbb{Z}[x,y] \to R\\) con \\(x \mapsto a\\) e \\(y \mapsto b\\), a saber, \\(P(x,y) \mapsto P(a,b)\\). La conmutatividad de \\(R\\) se usa aquí: \\(\mathrm{ev}\_{a,b}\\) respeta el producto porque en \\(R\\) se pueden reordenar las potencias de \\(a\\) y \\(b\\), igual que en \\(\mathbb{Z}[x,y]\\). Así,

\\[
\theta\_R\colon \mathbf{CRing}(\mathbb{Z}[x,y], R) \to UR \times UR, \qquad u \mapsto (u(x), u(y)),
\\]

es una biyección, con inversa \\((a,b) \mapsto \mathrm{ev}\_{a,b}\\). Es natural: para \\(\varphi\colon R \to S\\), \\(\theta\_S(\varphi \circ u) = (\varphi(u(x)), \varphi(u(y)))\\). Luego \\(U \times U \cong \mathbf{CRing}(\mathbb{Z}[x,y], -)\\), con elemento universal \\((x, y)\\). De la misma manera, \\(U \cong \mathbf{CRing}(\mathbb{Z}[t], -)\\), \\(u \mapsto u(t)\\).

**Las operaciones son transformaciones naturales.** La suma \\(\sigma\_R\colon UR \times UR \to UR\\), \\((a,b) \mapsto a + b\\), es natural, porque los homomorfismos respetan la suma: \\(\varphi(a + b) = \varphi(a) + \varphi(b)\\). Lo mismo vale para el producto \\(\mu\_R(a,b) = ab\\). Al transportar por los isomorfismos anteriores, \\(\sigma\\) y \\(\mu\\) se convierten en transformaciones naturales

\\[
\mathbf{CRing}(\mathbb{Z}[x,y], -) \Rightarrow \mathbf{CRing}(\mathbb{Z}[t], -).
\\]

**Yoneda covariante.** Por el corolario del Ejercicio 7, con \\(A = \mathbb{Z}[x,y]\\) y \\(B = \mathbb{Z}[t]\\), estas transformaciones corresponden biyectivamente a homomorfismos \\(p\colon \mathbb{Z}[t] \to \mathbb{Z}[x,y]\\). El homomorfismo correspondiente se obtiene evaluando en \\(1\_{\mathbb{Z}[x,y]}\\). Bajo \\(\theta\\), la identidad corresponde al elemento universal \\((x, y)\\). La suma lo envía a \\(x + y\\) y el producto, a \\(xy\\). Por lo tanto:

\\[
\text{suma} \longleftrightarrow (t \mapsto x + y), \qquad \text{producto} \longleftrightarrow (t \mapsto xy).
\\]

Recíprocamente, la transformación asociada a \\(p\\) es \\(u \mapsto u \circ p\\). Con \\(u = \mathrm{ev}\_{a,b}\\) y \\(p(t) = x + y\\), se obtiene el homomorfismo \\(t \mapsto a + b\\), es decir, \\(a + b\\). La cuenta cierra.

El mismo argumento da más: **toda** operación binaria natural \\(U \times U \Rightarrow U\\) en anillos conmutativos es \\((a, b) \mapsto P(a, b)\\) para un único polinomio \\(P \in \mathbb{Z}[x,y]\\). Del mismo modo, la resta corresponde a \\(t \mapsto x - y\\), el opuesto a \\(\mathbb{Z}[t] \to \mathbb{Z}[t]\\), \\(t \mapsto -t\\), y las constantes \\(0\\) y \\(1\\) a los homomorfismos \\(\mathbb{Z}[t] \to \mathbb{Z}\\), \\(t \mapsto 0\\) y \\(t \mapsto 1\\) (\\(\mathbb{Z}\\) representa al funtor constante \\(\\{\star\\}\\), porque es inicial).

**En \\(\mathbf{Ring}\\).** Un homomorfismo \\(\mathbb{Z}[x,y] \to R\\) envía \\(x\\) e \\(y\\) a elementos que **conmutan**, porque \\(xy = yx\\) en \\(\mathbb{Z}[x,y]\\). Así, \\(\mathbb{Z}[x,y]\\) representa al funtor "pares de elementos que conmutan", no a \\(U \times U\\). El representante de \\(U \times U\\) en \\(\mathbf{Ring}\\) es el **anillo libre** \\(\mathbb{Z}\langle x, y \rangle\\) de polinomios en variables que no conmutan: sus elementos son combinaciones enteras finitas de palabras en \\(x\\) e \\(y\\), y el producto es la concatenación de palabras extendida bilinealmente. Para un anillo \\(R\\) y \\(a, b \in R\\), el único homomorfismo con \\(x \mapsto a\\), \\(y \mapsto b\\) envía cada palabra a la palabra correspondiente en \\(a\\) y \\(b\\), y se extiende por aditividad. La suma y el producto corresponden ahora a \\(t \mapsto x + y\\) y \\(t \mapsto xy\\), y \\(t \mapsto yx\\) da el producto opuesto \\((a,b) \mapsto ba\\), que en general es distinto.

La solución seleccionada del archivo de ejercicios es correcta.

**Idea clave:** las operaciones naturales de una estructura algebraica son flechas entre los objetos que representan a sus potencias; las leyes se leen en el objeto representante.
