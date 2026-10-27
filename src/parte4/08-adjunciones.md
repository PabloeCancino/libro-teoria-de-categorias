# 8. Adjunciones: definición y ejemplos

## Hilo conductor

Saunders Mac Lane escribió que "los funtores adjuntos aparecen en todas partes". Este capítulo justifica la frase. Una adjunción es una pareja de funtores en sentidos opuestos, \\(F\colon \mathcal{C} \to \mathcal{D}\\) y \\(G\colon \mathcal{D} \to \mathcal{C}\\), tal que **dar una flecha \\(FX \to Y\\) en \\(\mathcal{D}\\) equivale a dar una flecha \\(X \to GY\\) en \\(\mathcal{C}\\)**. El grupo libre y el olvidadizo forman una adjunción; también la imagen y la imagen inversa, el cuantificador existencial y la sustitución, el producto y la exponencial, la parte entera y la inclusión de los enteros. Detrás de cada una de esas parejas hay la misma estructura.

## Ideas previas que se cristalizan

- Un homomorfismo \\(F(X) \to H\\) desde un grupo libre es lo mismo que una función \\(X \to UH\\).
- **Currificación:** una función de dos variables \\(A \times B \to C\\) es lo mismo que una función \\(A \to C^B\\) que devuelve funciones.
- **Imagen e imagen inversa:** \\(f(S) \subseteq T\\) si y solo si \\(S \subseteq f^{-1}(T)\\).
- **Parte entera superior:** \\(\lceil x \rceil \le n\\) si y solo si \\(x \le n\\), para \\(x \in \mathbb{R}\\) y \\(n \in \mathbb{Z}\\).
- **Conexiones de Galois:** la correspondencia entre subgrupos y campos intermedios, o entre ideales y conjuntos algebraicos.

---

## 1. La definición

> **Definición 8.1 (Adjunción).**
> Sean \\(F\colon \mathcal{C} \to \mathcal{D}\\) y \\(G\colon \mathcal{D} \to \mathcal{C}\\) funtores. Una **adjunción** \\(F \dashv G\\) es una familia de biyecciones
>
> \\[
> \mathcal{D}(FX, Y) \cong \mathcal{C}(X, GY),
> \\]
>
> una para cada \\(X \in \mathcal{C}\\) y cada \\(Y \in \mathcal{D}\\), **natural en \\(X\\) y en \\(Y\\)**. Se dice que \\(F\\) es **adjunto izquierdo** de \\(G\\) y que \\(G\\) es **adjunto derecho** de \\(F\\).

Si \\(g\colon FX \to Y\\), su imagen bajo la biyección se denota \\(\overline{g}\colon X \to GY\\), y se llama **transpuesta** de \\(g\\); en sentido inverso, \\(f\colon X \to GY\\) tiene transpuesta \\(\overline{f}\colon FX \to Y\\). La naturalidad se expresa así: para \\(k\colon X' \to X\\) y \\(h\colon Y \to Y'\\),

\\[
\overline{h \circ g \circ F(k)} = G(h) \circ \overline{g} \circ k.
\\]

En palabras: **transponer conmuta con componer por los lados**. Esta regla es lo único que se necesita para manipular adjunciones.

> **📝 Para pensar.** La notación \\(F \dashv G\\) no es simétrica: el adjunto izquierdo aparece a la izquierda del símbolo hom, en el primer argumento. Para recordar el sentido, revisa con el par libre y olvidadizo: ¿cuál de los dos aparece en \\(\mathcal{D}(FX, Y)\\)? ¿Puede ser el olvidadizo adjunto izquierdo de algo?

---

## 2. Ejemplos

### A. Libre y olvidadizo

> **Ejemplo 8.2.**
> Para \\(F\colon \mathbf{Set} \to \mathbf{Grp}\\) el grupo libre y \\(U\\) el olvidadizo,
>
> \\[
> \mathbf{Grp}(F(X), H) \cong \mathbf{Set}(X, UH).
> \\]
>
> La biyección envía un homomorfismo a su restricción a los generadores. Es la propiedad universal del grupo libre (Ejemplo 4.10). Lo mismo vale para los espacios vectoriales con base dada (\\(k^{(-)} \dashv U\\)), para el monoide libre (\\(L \dashv U\\)) y para el anillo de polinomios \\(\mathbb{Z}[X] \dashv U\colon \mathbf{CRing} \to \mathbf{Set}\\).

### B. Adjunciones entre órdenes: conexiones de Galois

Si \\(\mathcal{C}\\) y \\(\mathcal{D}\\) son órdenes parciales, los conjuntos hom tienen a lo más un elemento, la naturalidad es automática y una adjunción \\(f \dashv g\\) entre funciones monótonas es simplemente

\\[
f(x) \le y \iff x \le g(y).
\\]

Esta noción se llama **conexión de Galois** (monótona).

> **Ejemplo 8.3 (Parte entera).**
> Sea \\(i\colon \mathbb{Z} \to \mathbb{R}\\) la inclusión, entre órdenes usuales. Entonces
>
> \\[
> \lceil x \rceil \le n \iff x \le i(n), \qquad i(n) \le x \iff n \le \lfloor x \rfloor.
> \\]
>
> Es decir, \\(\lceil - \rceil \dashv i \dashv \lfloor - \rfloor\\). La parte entera inferior y la superior son los dos adjuntos de la inclusión.

> **Ejemplo 8.4 (Imagen, imagen inversa y cuantificadores).**
> Sea \\(f\colon X \to Y\\) una función y considérense los órdenes \\((\mathcal{P}(X), \subseteq)\\) y \\((\mathcal{P}(Y), \subseteq)\\). La imagen inversa \\(f^{-1}\colon \mathcal{P}(Y) \to \mathcal{P}(X)\\) tiene **dos** adjuntos:
>
> \\[
> \exists\_f \dashv f^{-1} \dashv \forall\_f,
> \\]
>
> con \\(\exists\_f(S) = f(S) = \\{y \mid \exists x \in S, \ f(x) = y\\}\\) y \\(\forall\_f(S) = \\{y \mid \forall x, \ f(x) = y \Rightarrow x \in S\\}\\).
>
> Cuando \\(f\\) es la proyección \\(\pi\colon X \times Y \to Y\\) y \\(S \subseteq X \times Y\\) es el conjunto de verdad de un predicado \\(\varphi(x, y)\\), resulta:
>
> \\[
> \exists\_\pi(S) = \\{y \mid \exists x \ \varphi(x,y)\\}, \qquad \forall\_\pi(S) = \\{y \mid \forall x \ \varphi(x,y)\\}.
> \\]
>
> **Los cuantificadores existencial y universal son los adjuntos izquierdo y derecho de la sustitución.** Esta observación, debida a F. W. Lawvere, es la puerta de entrada a la lógica categórica.

La regla de inferencia "de \\(\varphi(x) \to \psi\\), con \\(x\\) no libre en \\(\psi\\), se deduce \\(\exists x\\, \varphi(x) \to \psi\\)" es, palabra por palabra, la adjunción \\(\exists \dashv\\) sustitución: \\(\exists\_\pi(S) \subseteq T\\) si y solo si \\(S \subseteq \pi^{-1}(T)\\).

### C. Producto y exponencial

> **Ejemplo 8.5 (Currificación).**
> Para un conjunto fijo \\(B\\), el funtor \\(- \times B\colon \mathbf{Set} \to \mathbf{Set}\\) es adjunto izquierdo de \\((-)^B = \mathbf{Set}(B, -)\\):
>
> \\[
> \mathbf{Set}(A \times B, C) \cong \mathbf{Set}(A, C^B), \qquad g \mapsto \big(a \mapsto g(a, -)\big).
> \\]
>
> En \\(\mathbf{Vect}\_k\\), el producto tensorial cumple el mismo papel: \\(\mathrm{Hom}(U \otimes V, W) \cong \mathrm{Hom}(U, \mathrm{Hom}(V, W))\\). Una categoría con productos finitos en la que cada \\(- \times B\\) tiene adjunto derecho se llama **cartesiana cerrada**. Estas categorías son el modelo del cálculo lambda tipado.

### D. Topologías extremas

> **Ejemplo 8.6.**
> Sea \\(U\colon \mathbf{Top} \to \mathbf{Set}\\) el olvidadizo, \\(D\\) el funtor que da a un conjunto la topología discreta e \\(I\\) el que le da la indiscreta. Entonces
>
> \\[
> D \dashv U \dashv I.
> \\]
>
> Toda función desde un espacio discreto es continua, y toda función hacia un espacio indiscreto también.

### E. Reflexiones

> **Ejemplo 8.7.**
> La abelianización es adjunta izquierda de la inclusión: \\(\mathbf{Ab}(G^{\mathrm{ab}}, A) \cong \mathbf{Grp}(G, A)\\). La compactación de Stone–Čech es adjunta izquierda de la inclusión de los espacios compactos de Hausdorff en \\(\mathbf{Top}\\). Una subcategoría plena cuya inclusión tiene adjunto izquierdo se llama **reflexiva**.

---

## 3. Unidad y counidad

Al transponer las identidades se obtienen dos familias de flechas canónicas.

> **Definición 8.8 (Unidad y counidad).**
> Dada una adjunción \\(F \dashv G\\), se definen:
>
> - la **unidad** \\(\eta\_X = \overline{1\_{FX}}\colon X \to GFX\\);
> - la **counidad** \\(\varepsilon\_Y = \overline{1\_{GY}}\colon FGY \to Y\\).

Para el grupo libre, \\(\eta\_X\colon X \to UF(X)\\) es la inclusión de los generadores, y \\(\varepsilon\_H\colon F(UH) \to H\\) es la evaluación: una palabra formal en los elementos de \\(H\\) se envía a su producto en \\(H\\). Para la currificación, \\(\eta\_A\colon A \to (A \times B)^B\\) envía \\(a\\) a \\(b \mapsto (a, b)\\), y \\(\varepsilon\_C\colon C^B \times B \to C\\) es la **evaluación** \\((\varphi, b) \mapsto \varphi(b)\\).

> **Teorema 8.9 (Adjunciones vía unidad y counidad).**
> Dar una adjunción \\(F \dashv G\\) equivale a dar transformaciones naturales \\(\eta\colon 1\_{\mathcal{C}} \Rightarrow GF\\) y \\(\varepsilon\colon FG \Rightarrow 1\_{\mathcal{D}}\\) que satisfacen las **identidades triangulares**:
>
> \\[
> \varepsilon F \circ F\eta = 1\_F, \qquad G\varepsilon \circ \eta G = 1\_G.
> \\]
>
> Componente por componente: \\(\varepsilon\_{FX} \circ F(\eta\_X) = 1\_{FX}\\) y \\(G(\varepsilon\_Y) \circ \eta\_{GY} = 1\_{GY}\\).

*Demostración (de la adjunción a las identidades).* La naturalidad de la transposición da las fórmulas

\\[
\overline{g} = G(g) \circ \eta\_X \quad (g\colon FX \to Y), \qquad \overline{f} = \varepsilon\_Y \circ F(f) \quad (f\colon X \to GY).
\\]

En efecto, \\(\overline{g} = \overline{g \circ 1\_{FX}} = G(g) \circ \overline{1\_{FX}} = G(g) \circ \eta\_X\\), y la otra es dual. Al aplicar la segunda fórmula a \\(f = \eta\_X\\):

\\[
\varepsilon\_{FX} \circ F(\eta\_X) = \overline{\eta\_X} = \overline{\overline{1\_{FX}}} = 1\_{FX}.
\\]

La otra identidad triangular es dual. La naturalidad de \\(\eta\\) y \\(\varepsilon\\) se sigue de la naturalidad de la biyección.

*Demostración (de las identidades a la adjunción).* Se definen las dos transposiciones con las fórmulas anteriores. Las identidades triangulares, junto con la naturalidad de \\(\eta\\) y \\(\varepsilon\\), muestran que son mutuamente inversas. Por ejemplo, para \\(g\colon FX \to Y\\):

\\[
\varepsilon\_Y \circ F(G(g) \circ \eta\_X) = \varepsilon\_Y \circ FG(g) \circ F(\eta\_X) = g \circ \varepsilon\_{FX} \circ F(\eta\_X) = g,
\\]

donde se usó la naturalidad de \\(\varepsilon\\) y luego la primera identidad triangular. \\(\blacksquare\\)

La fórmula \\(\overline{g} = G(g) \circ \eta\_X\\) dice que **toda flecha \\(X \to GY\\) se factoriza de manera única a través de \\(\eta\_X\\)**. Es decir, \\(\eta\_X\\) es una flecha universal de \\(X\\) a \\(G\\), en el sentido del Capítulo 4. Esto lleva al siguiente teorema.

> **Teorema 8.10 (Adjuntos a partir de flechas universales).**
> Un funtor \\(G\colon \mathcal{D} \to \mathcal{C}\\) tiene adjunto izquierdo si y solo si para cada objeto \\(X\\) de \\(\mathcal{C}\\) existe una flecha universal \\((FX, \eta\_X)\\) de \\(X\\) a \\(G\\). En tal caso, \\(F\\) se extiende de manera única a un funtor con \\(F \dashv G\\).
>
> *Idea de la demostración.* Para \\(k\colon X \to X'\\), se define \\(F(k)\\) como la única flecha \\(FX \to FX'\\) con \\(G(F(k)) \circ \eta\_X = \eta\_{X'} \circ k\\). La unicidad de esa factorización garantiza que \\(F\\) preserva composición e identidades, y que \\(\eta\\) es natural. \\(\blacksquare\\)

Este teorema conecta los capítulos 4 y 8: **los objetos libres de la Parte II son, juntos, un adjunto izquierdo**.

> **📝 Para pensar.** Las identidades triangulares tienen la forma de los axiomas de un "inverso débil": \\(F\\) y \\(G\\) no son inversos, pero \\(\eta\\) y \\(\varepsilon\\) miden cuánto se alejan de serlo de manera coherente. Si \\(\eta\\) y \\(\varepsilon\\) son isomorfismos naturales, ¿qué es la adjunción? Compara con la Definición 3.9.

---

## 🔑 Lo que cristalizó

- Una **adjunción** \\(F \dashv G\\) es una biyección natural \\(\mathcal{D}(FX, Y) \cong \mathcal{C}(X, GY)\\).
- Libre y olvidadizo, imagen e imagen inversa, \\(\exists\\) y sustitución, sustitución y \\(\forall\\), producto y exponencial, parte entera e inclusión: todas son adjunciones.
- Una adjunción equivale a una **unidad** y una **counidad** que cumplen las **identidades triangulares**.
- Un adjunto izquierdo es una elección coherente de **flechas universales**: los objetos libres del Capítulo 4.

## 🌉 Puente

Las adjunciones explican las parejas que se observaron en los capítulos anteriores. Falta ver qué hacen: el Capítulo 9 demuestra que los adjuntos derechos preservan límites, que los adjuntos son únicos y que las equivalencias de categorías son adjunciones especiales.
