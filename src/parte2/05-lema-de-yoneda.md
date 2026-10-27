# 5. Funtores representables y el lema de Yoneda

## Hilo conductor

En el Capítulo 1 se observó que los elementos de un conjunto \\(A\\) son las funciones \\(\\{\star\\} \to A\\). En los ejercicios de la Parte I se vio que los elementos de un grupo \\(G\\) son los homomorfismos \\(\mathbb{Z} \to G\\). En el Capítulo 4, que una flecha hacia \\(A \times B\\) es un par de flechas. En los tres casos, una pregunta sobre un objeto se respondió **mirando las flechas que entran en él**. Este capítulo demuestra que eso no es una coincidencia: un objeto queda completamente determinado, salvo isomorfismo, por el sistema de todas las flechas que llegan a él. El enunciado preciso es el **lema de Yoneda**, el resultado más importante de la teoría elemental.

## Ideas previas que se cristalizan

- **Teorema de Cayley:** todo grupo es isomorfo a un subgrupo de un grupo de permutaciones, actuando sobre sí mismo.
- **Órdenes parciales:** \\(x \le y\\) si y solo si todo elemento menor o igual que \\(x\\) es menor o igual que \\(y\\).
- **Álgebra lineal:** un vector queda determinado por los valores que toman en él todos los funcionales lineales.
- **Elementos como flechas:** \\(\mathbf{Set}(\\{\star\\}, A) \cong A\\), \\(\mathbf{Grp}(\mathbb{Z}, G) \cong UG\\), \\(\mathbf{Top}(\\{\star\\}, X) \cong UX\\).

---

## 1. Funtores representables

> **Definición 5.1 (Funtor representable).**
> Un funtor \\(F\colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}\\) (un **prehaz** sobre \\(\mathcal{C}\\)) es **representable** si existe un objeto \\(A\\) y un isomorfismo natural
>
> \\[
> F \cong \mathcal{C}(-, A).
> \\]
>
> Se dice que \\(A\\) **representa** a \\(F\\). Dualmente, un funtor covariante \\(F\colon \mathcal{C} \to \mathbf{Set}\\) es representable si \\(F \cong \mathcal{C}(A, -)\\) para algún \\(A\\).

> **Ejemplo 5.2 (Funtores representables conocidos).**
>
> | Funtor | Representado por | Por qué |
> | :--- | :--- | :--- |
> | \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) | \\(\mathbb{Z}\\) | Un homomorfismo \\(\mathbb{Z} \to G\\) es la elección de un elemento |
> | \\(U\colon \mathbf{Ring} \to \mathbf{Set}\\) | \\(\mathbb{Z}[x]\\) | Un homomorfismo \\(\mathbb{Z}[x] \to R\\) es la elección de la imagen de \\(x\\) |
> | \\(U\colon \mathbf{Top} \to \mathbf{Set}\\) | El espacio con un punto | Un punto de \\(X\\) es una función continua desde un punto |
> | \\(G \mapsto \\{g \in G \mid g^n = e\\}\\) | \\(\mathbb{Z}/n\\) | Un homomorfismo \\(\mathbb{Z}/n \to G\\) es un elemento con \\(g^n = e\\) |
> | \\(\mathcal{P}^{-}\colon \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}\\) | \\(\\{0, 1\\}\\) | Un subconjunto es su función característica |
> | \\(X \mapsto \mathcal{C}(X, A) \times \mathcal{C}(X, B)\\) | \\(A \times B\\) | Es la propiedad universal del producto |

La última fila reinterpreta el Capítulo 4: **el producto \\(A \times B\\) es, por definición, un objeto que representa al funtor "pares de flechas"**. Toda propiedad universal puede leerse así.

> **Ejemplo 5.3 (Un funtor no representable).**
> El funtor constante \\(K\colon \mathbf{Set} \to \mathbf{Set}\\) con valor \\(\\{0,1\\}\\) no es representable. Si \\(K \cong \mathbf{Set}(A, -)\\), al evaluar en \\(\emptyset\\) se tendría \\(\mathbf{Set}(A, \emptyset) \cong \\{0,1\\}\\). Pero \\(\mathbf{Set}(A, \emptyset)\\) tiene un elemento si \\(A = \emptyset\\) y ninguno si \\(A \neq \emptyset\\).

---

## 2. El lema

Sea \\(F\colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}\\) un prehaz y \\(A\\) un objeto. ¿Cuántas transformaciones naturales \\(\mathcal{C}(-, A) \Rightarrow F\\) hay? A primera vista, muchas: una transformación natural es una familia de funciones, una por cada objeto \\(X\\). El lema de Yoneda dice que hay **exactamente tantas como elementos tiene \\(F(A)\\)**.

> **Teorema 5.4 (Lema de Yoneda).**
> Sea \\(\mathcal{C}\\) localmente pequeña, \\(F\colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}\\) un funtor y \\(A\\) un objeto de \\(\mathcal{C}\\). La función
>
> \\[
> \Phi\colon \mathrm{Nat}(\mathcal{C}(-, A), F) \to F(A), \qquad \alpha \mapsto \alpha\_A(1\_A),
> \\]
>
> es una biyección. Su inversa envía \\(x \in F(A)\\) a la transformación \\(\Psi(x)\\) con componentes
>
> \\[
> \Psi(x)\_X\colon \mathcal{C}(X, A) \to F(X), \qquad f \mapsto F(f)(x).
> \\]
>
> Además, la biyección es natural en \\(A\\) y en \\(F\\).

*Demostración.* Hay que verificar tres cosas.

**(1) \\(\Psi(x)\\) es natural.** Sea \\(g\colon Y \to X\\). Hay que ver que \\(F(g) \circ \Psi(x)\_X = \Psi(x)\_Y \circ \mathcal{C}(g, A)\\), donde \\(\mathcal{C}(g, A)\\) es la función \\(f \mapsto f \circ g\\). Para \\(f \in \mathcal{C}(X, A)\\):

\\[
F(g)\big(F(f)(x)\big) = F(f \circ g)(x) = \Psi(x)\_Y(f \circ g).
\\]

La primera igualdad es la funtorialidad de \\(F\\), que es contravariante: \\(F(f \circ g) = F(g) \circ F(f)\\).

**(2) \\(\Phi \circ \Psi\\) es la identidad.** \\(\Phi(\Psi(x)) = \Psi(x)\_A(1\_A) = F(1\_A)(x) = x\\).

**(3) \\(\Psi \circ \Phi\\) es la identidad.** Sea \\(\alpha\\) natural y \\(f\colon X \to A\\). La naturalidad de \\(\alpha\\) respecto de \\(f\\) es el cuadrado

\\[
\require{AMScd}
\begin{CD}
\mathcal{C}(A, A) @>{\alpha\_A}>> F(A) \\\\
@V{-\circ f}VV @VV{F(f)}V \\\\
\mathcal{C}(X, A) @>>{\alpha\_X}> F(X)
\end{CD}
\\]

Al seguir el elemento \\(1\_A\\) por los dos caminos:

\\[
F(f)\big(\alpha\_A(1\_A)\big) = \alpha\_X(1\_A \circ f) = \alpha\_X(f).
\\]

El lado izquierdo es \\(\Psi(\Phi(\alpha))\_X(f)\\). Luego \\(\Psi(\Phi(\alpha)) = \alpha\\).

La naturalidad en \\(A\\) y en \\(F\\) se comprueba de la misma manera, siguiendo elementos por cuadrados; se deja como Ejercicio 6 de la Parte II. \\(\blacksquare\\)

El corazón de la prueba es el paso (3): **una transformación natural que sale de un representable queda determinada por lo que hace con la identidad**. Toda la información está concentrada en un solo elemento, \\(\alpha\_A(1\_A)\\).

> **📝 Para pensar.** Relee el paso (3) y localiza la única hipótesis que se usó sobre \\(\alpha\\). ¿Qué parte de la prueba fallaría si \\(\alpha\\) fuera solo una familia de funciones, sin naturalidad? Construye un contraejemplo pequeño con \\(\mathcal{C} = \mathbf{2}\\).

---

## 3. Consecuencias

> **Corolario 5.5 (El encaje de Yoneda).**
> El funtor \\(y\colon \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]\\), que envía \\(A\\) a \\(\mathcal{C}(-, A)\\) y \\(f\colon A \to B\\) a la transformación \\(f \circ -\\), es **plenamente fiel**.
>
> *Demostración.* Se aplica el lema de Yoneda con \\(F = \mathcal{C}(-, B)\\):
>
> \\[
> \mathrm{Nat}(\mathcal{C}(-, A), \mathcal{C}(-, B)) \cong \mathcal{C}(A, B).
> \\]
>
> La biyección envía \\(f\colon A \to B\\) a la transformación \\(g \mapsto f \circ g\\), que es \\(y(f)\\). \\(\blacksquare\\)

Toda categoría localmente pequeña es, entonces, **una subcategoría plena de una categoría de prehaces**. Los objetos abstractos de \\(\mathcal{C}\\) se pueden reemplazar por funtores concretos con valores en conjuntos, sin perder ni ganar flechas.

> **Corolario 5.6 (Un objeto se conoce por sus flechas).**
> Si \\(\mathcal{C}(-, A) \cong \mathcal{C}(-, B)\\) de manera natural, entonces \\(A \cong B\\).
>
> *Demostración.* Un funtor plenamente fiel refleja isomorfismos (Ejemplo 2.14). \\(\blacksquare\\)

> **Corolario 5.7 (Elementos universales).**
> Un prehaz \\(F\\) es representable si y solo si existen un objeto \\(A\\) y un elemento \\(u \in F(A)\\) tales que para todo \\(X\\) y todo \\(x \in F(X)\\) hay una única \\(f\colon X \to A\\) con \\(F(f)(u) = x\\). El par \\((A, u)\\) se llama **elemento universal** de \\(F\\), y es único salvo isomorfismo único.
>
> *Demostración.* Por el lema, un isomorfismo natural \\(\mathcal{C}(-, A) \to F\\) es \\(\Psi(u)\\) para un único \\(u \in F(A)\\), y \\(\Psi(u)\\) es biyectiva en cada \\(X\\) exactamente cuando se cumple la condición enunciada. \\(\blacksquare\\)

Para el funtor "pares de flechas" del Ejemplo 5.2, el elemento universal es el par de proyecciones \\((\pi\_1, \pi\_2)\\). El Corolario 5.7 reformula la Definición 4.4 sin cambiarle nada.

---

## 4. Dos teoremas clásicos como casos particulares

> **Ejemplo 5.8 (El teorema de Cayley).**
> Sea \\(G\\) un grupo y \\(\mathcal{C} = \mathbf{B}G\\), con un único objeto \\(\star\\). El único representable es \\(\mathcal{C}(-, \star)\\): el conjunto \\(G\\) con la acción por **multiplicación a la derecha** (precomponer con \\(g\\) es \\(h \mapsto hg\\)). El encaje de Yoneda da un isomorfismo
>
> \\[
> G = \mathcal{C}(\star, \star) \cong \mathrm{Nat}(\mathcal{C}(-, \star), \mathcal{C}(-, \star)),
> \\]
>
> que envía \\(g\\) a la multiplicación por la izquierda \\(h \mapsto gh\\). Cada transformación natural es en particular una permutación del conjunto \\(G\\). Así se obtiene un homomorfismo inyectivo \\(G \to \mathrm{Sym}(G)\\). **Es el teorema de Cayley**, y el lema de Yoneda lo generaliza de un objeto a muchos.

> **Ejemplo 5.9 (Órdenes parciales y conjuntos inferiores).**
> Sea \\(P\\) un orden parcial visto como categoría. Un prehaz \\(P^{\mathrm{op}} \to \mathbf{Set}\\) con valores en \\(\\{\emptyset, \\{\star\\}\\}\\) es lo mismo que un **conjunto inferior** (un subconjunto cerrado hacia abajo). El representable \\(P(-, x)\\) corresponde a \\(\downarrow x = \\{p \mid p \le x\\}\\). El Corolario 5.5 (el encaje es plenamente fiel) dice aquí:
>
> \\[
> x \le y \iff \ \downarrow x \subseteq \ \downarrow y,
> \\]
>
> y el encaje \\(x \mapsto \downarrow x\\) sumerge a \\(P\\) en el retículo completo de sus conjuntos inferiores. Esta es la idea que, refinada, conduce a la completación de Dedekind–MacNeille.

---

## 5. Lectura filosófica y una analogía con cautela

El lema de Yoneda tiene una lectura que va más allá de la técnica: **un objeto matemático es completamente conocido a través de sus relaciones con todos los demás objetos**. Las flechas \\(X \to A\\) se llaman a veces **elementos generalizados** de \\(A\\) "con forma \\(X\\)": puntos (forma \\(\\{\star\\}\\)), caminos (forma \\([0,1]\\)), pares de elementos (forma \\(\\{\star, \star'\\}\\)). Conocer todos los elementos generalizados de \\(A\\), junto con la manera en que cambian al cambiar la forma, es conocer \\(A\\).

> **📝 Para pensar.** En psicometría se dice que un constructo latente solo se conoce por sus manifestaciones: las respuestas a los reactivos. El lema de Yoneda es la versión exacta de esa intuición **en un contexto donde se dispone de todas las "pruebas" posibles y de su comportamiento bajo todas las transformaciones**. ¿Qué hipótesis del lema fallan en un instrumento real, con finitos reactivos y error de medición? La analogía ayuda a recordar el lema; no transfiere ningún resultado a la medición.

---

## 🔑 Lo que cristalizó

- Un funtor es **representable** si es isomorfo a un funtor hom; las propiedades universales del Capítulo 4 son representaciones.
- **Lema de Yoneda:** las transformaciones naturales \\(\mathcal{C}(-, A) \Rightarrow F\\) corresponden a los elementos de \\(F(A)\\), vía \\(\alpha \mapsto \alpha\_A(1\_A)\\).
- El **encaje de Yoneda** es plenamente fiel: un objeto queda determinado salvo isomorfismo por sus flechas entrantes.
- El teorema de Cayley y el encaje de un orden en sus conjuntos inferiores son casos particulares.

## 🌉 Puente

El producto representa al funtor "pares de flechas". ¿Qué representa al funtor "ternas de flechas que coinciden en algo", o "flechas que igualan a otras dos"? La Parte III da la respuesta general: los **límites** son los objetos que representan los funtores de conos.
