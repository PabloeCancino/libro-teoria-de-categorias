# 2. Funtores: morfismos entre categorías

## Hilo conductor

Un homomorfismo de grupos es una función que respeta la estructura de grupo. Una categoría también tiene estructura: composición e identidades. Una "función entre categorías" que respete esa estructura se llama **funtor**. Este capítulo muestra que muchas construcciones conocidas son funtores: el conjunto subyacente de un grupo, el grupo libre sobre un conjunto, el grupo fundamental de un espacio y el espacio dual de un espacio vectorial. Muestra también por qué esto importa: **los funtores son la fuente de los invariantes**.

## Ideas previas que se cristalizan

- Una función continua \\(f\colon X \to Y\\) induce un homomorfismo \\(f\_\ast\colon \pi\_1(X, x) \to \pi\_1(Y, f(x))\\), y \\((g \circ f)\_\ast = g\_\ast \circ f\_\ast\\).
- Una transformación lineal \\(T\colon V \to W\\) induce su transpuesta \\(T^{\top}\colon W^{\ast} \to V^{\ast}\\), que **invierte** el sentido.
- Una acción de un grupo \\(G\\) sobre un conjunto \\(X\\) asigna a cada \\(g \in G\\) una biyección de \\(X\\), compatible con el producto.
- El grupo de un nudo, \\(\pi\_1(\mathbb{R}^3 \setminus K)\\), no cambia bajo isotopía.

---

## 1. La definición

> **Definición 2.1 (Funtor).**
> Sean \\(\mathcal{C}\\) y \\(\mathcal{D}\\) categorías. Un **funtor** \\(F\colon \mathcal{C} \to \mathcal{D}\\) consta de:
>
> 1. una asignación de objetos \\(A \mapsto F(A)\\), o simplemente \\(FA\\);
> 2. para cada par de objetos \\(A, B\\), una función \\(\mathcal{C}(A,B) \to \mathcal{D}(FA, FB)\\), \\(f \mapsto F(f)\\),
>
> de modo que se preservan la composición y las identidades:
>
> \\[
> F(g \circ f) = F(g) \circ F(f), \qquad F(1\_A) = 1\_{FA}.
> \\]

Un funtor envía diagramas conmutativos en diagramas conmutativos, porque cada igualdad entre compuestos se transporta por \\(F\\).

> **Proposición 2.2 (Los funtores preservan isomorfismos).**
> Si \\(f\colon A \to B\\) es un isomorfismo en \\(\mathcal{C}\\), entonces \\(F(f)\\) es un isomorfismo en \\(\mathcal{D}\\), con inversa \\(F(f^{-1})\\).
>
> *Demostración.* \\(F(f^{-1}) \circ F(f) = F(f^{-1} \circ f) = F(1\_A) = 1\_{FA}\\), y de manera análoga en el otro orden. \\(\blacksquare\\)

La consecuencia es poderosa. **Si \\(FA \not\cong FB\\), entonces \\(A \not\cong B\\).** Un funtor es una máquina de producir invariantes: para distinguir dos objetos complicados, se les aplica un funtor y se comparan los resultados, más sencillos.

> **Ejemplo 2.3 (El grupo de un nudo como invariante).**
> Dos nudos \\(K\\) y \\(K'\\) isotópicos en el ambiente tienen complementos \\(\mathbb{R}^3 \setminus K\\) y \\(\mathbb{R}^3 \setminus K'\\) homeomorfos. El grupo fundamental es un funtor de los espacios con punto base en los grupos, así que transforma ese homeomorfismo en un isomorfismo de grupos. Por eso el **grupo del nudo** es un invariante. El argumento no usa nada específico de los nudos: es la Proposición 2.2.

> **Ejemplo 2.4 (Brouwer en dimensión 2).**
> Supongamos que existiera una retracción continua \\(r\colon D^2 \to S^1\\) con \\(r \circ i = 1\_{S^1}\\), donde \\(i\colon S^1 \to D^2\\) es la inclusión. Al aplicar \\(\pi\_1\\) se obtendría \\(\pi\_1(r) \circ \pi\_1(i) = 1\_{\mathbb{Z}}\\), con \\(\pi\_1(i)\colon \mathbb{Z} \to 0\\) y \\(\pi\_1(r)\colon 0 \to \mathbb{Z}\\). La identidad de \\(\mathbb{Z}\\) se factorizaría a través del grupo trivial, lo cual es imposible. No hay tal retracción y, de ahí, toda función continua \\(D^2 \to D^2\\) tiene un punto fijo.

> **📝 Para pensar.** En el Ejemplo 2.4 se usaron solo dos propiedades: \\(\pi\_1\\) preserva la composición y la identidad. ¿Qué información sobre la topología se "pierde" al pasar a \\(\pi\_1\\)? ¿Por qué perder información es, aquí, una ventaja?

---

## 2. Catálogo de funtores

### A. Funtores olvidadizos

> **Ejemplo 2.5 (Olvidar estructura).**
> El funtor \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) envía un grupo a su conjunto subyacente y un homomorfismo a la función subyacente. De la misma manera hay olvidadizos \\(\mathbf{Top} \to \mathbf{Set}\\), \\(\mathbf{Vect}\_k \to \mathbf{Set}\\), \\(\mathbf{Ring} \to \mathbf{Ab}\\) (se olvida la multiplicación) y \\(\mathbf{Ab} \to \mathbf{Grp}\\) (se olvida que el grupo es abeliano).

### B. Funtores libres

> **Ejemplo 2.6 (Construcciones libres).**
>
> - \\(F\colon \mathbf{Set} \to \mathbf{Vect}\_k\\) envía un conjunto \\(X\\) al espacio vectorial \\(k^{(X)}\\) con base \\(X\\): las combinaciones lineales formales finitas de elementos de \\(X\\). Una función \\(f\colon X \to Y\\) se extiende por linealidad a \\(F(f)\colon k^{(X)} \to k^{(Y)}\\).
> - \\(F\colon \mathbf{Set} \to \mathbf{Grp}\\) envía \\(X\\) al **grupo libre** sobre \\(X\\): las palabras reducidas en las letras \\(x\\) y \\(x^{-1}\\). Una función \\(f\\) actúa sustituyendo cada letra \\(x\\) por \\(f(x)\\) y reduciendo.
> - \\(L\colon \mathbf{Set} \to \mathbf{Mon}\\) envía \\(X\\) al **monoide libre** \\(L(X)\\): las listas finitas \\((x\_1, \dots, x\_n)\\) con la concatenación como operación y la lista vacía como neutro.

Los funtores libres y los olvidadizos aparecen siempre en parejas. El Capítulo 8 explica esa relación con precisión: es el primer ejemplo de **adjunción**.

### C. Funtores entre estructuras vistas como categorías

> **Ejemplo 2.7.**
>
> - Si \\(P\\) y \\(Q\\) son órdenes parciales vistos como categorías, un funtor \\(P \to Q\\) es exactamente una **función monótona**: preservar flechas es preservar el orden, y las ecuaciones de un funtor se cumplen solas.
> - Si \\(M\\) y \\(N\\) son monoides, un funtor \\(\mathbf{B}M \to \mathbf{B}N\\) es exactamente un **homomorfismo de monoides**.

> **Ejemplo 2.8 (Acciones y representaciones).**
> Sea \\(G\\) un grupo. Un funtor \\(X\colon \mathbf{B}G \to \mathbf{Set}\\) consiste en un conjunto \\(X(\star)\\) y, para cada \\(g \in G\\), una función \\(X(g)\colon X(\star) \to X(\star)\\) tal que \\(X(gh) = X(g) \circ X(h)\\) y \\(X(e) = 1\\). Eso es exactamente una **acción de \\(G\\) sobre un conjunto**. De la misma manera, un funtor \\(\mathbf{B}G \to \mathbf{Vect}\_k\\) es una **representación lineal** de \\(G\\).

El Ejemplo 2.8 es un patrón general. **Un funtor de una categoría pequeña \\(\mathcal{J}\\) en \\(\mathbf{Set}\\) es una "acción" de \\(\mathcal{J}\\)**, o un sistema de conjuntos y funciones con la forma de \\(\mathcal{J}\\). Este punto de vista organiza los capítulos 5 y 6.

### D. Funtores de conjunto potencia

> **Ejemplo 2.9 (Potencia covariante).**
> \\(\mathcal{P}\colon \mathbf{Set} \to \mathbf{Set}\\) envía \\(X\\) al conjunto potencia \\(\mathcal{P}(X)\\) y \\(f\colon X \to Y\\) a la **imagen directa**:
>
> \\[
> \mathcal{P}(f)\colon \mathcal{P}(X) \to \mathcal{P}(Y), \qquad S \mapsto f(S) = \\{f(s) \mid s \in S\\}.
> \\]
>
> Se cumple \\((g \circ f)(S) = g(f(S))\\), así que \\(\mathcal{P}\\) es un funtor.

---

## 3. Funtores contravariantes

Algunas construcciones invierten el sentido de las flechas.

> **Definición 2.10 (Funtor contravariante).**
> Un **funtor contravariante** de \\(\mathcal{C}\\) en \\(\mathcal{D}\\) es un funtor \\(F\colon \mathcal{C}^{\mathrm{op}} \to \mathcal{D}\\). Concretamente, envía \\(f\colon A \to B\\) a \\(F(f)\colon FB \to FA\\) y cumple \\(F(g \circ f) = F(f) \circ F(g)\\).

> **Ejemplo 2.11.**
>
> - **Potencia contravariante.** \\(\mathcal{P}^{-}\colon \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}\\) envía \\(X\\) a \\(\mathcal{P}(X)\\) y \\(f\colon X \to Y\\) a la **imagen inversa** \\(T \mapsto f^{-1}(T)\\), que va de \\(\mathcal{P}(Y)\\) a \\(\mathcal{P}(X)\\).
> - **Espacio dual.** \\((-)^{\ast}\colon \mathbf{Vect}\_k^{\mathrm{op}} \to \mathbf{Vect}\_k\\) envía \\(V\\) a \\(V^{\ast} = \mathrm{Hom}(V, k)\\) y \\(T\colon V \to W\\) a \\(T^{\ast}\colon W^{\ast} \to V^{\ast}\\), \\(\varphi \mapsto \varphi \circ T\\).
> - **Funciones continuas a los reales.** \\(C\colon \mathbf{Top}^{\mathrm{op}} \to \mathbf{Ring}\\) envía \\(X\\) al anillo \\(C(X)\\) de funciones continuas \\(X \to \mathbb{R}\\) y \\(f\colon X \to Y\\) a \\(\varphi \mapsto \varphi \circ f\\).

En los tres casos la acción sobre flechas es **componer por la derecha**. Ese es el germen del funtor más importante de la teoría.

> **Definición 2.12 (Funtores hom).**
> Sea \\(\mathcal{C}\\) localmente pequeña y \\(A\\) un objeto. Se definen:
>
> - el funtor covariante \\(\mathcal{C}(A, -)\colon \mathcal{C} \to \mathbf{Set}\\), que envía \\(X\\) a \\(\mathcal{C}(A, X)\\) y \\(f\colon X \to Y\\) a la función \\(u \mapsto f \circ u\\);
> - el funtor contravariante \\(\mathcal{C}(-, A)\colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}\\), que envía \\(X\\) a \\(\mathcal{C}(X, A)\\) y \\(f\colon X \to Y\\) a la función \\(v \mapsto v \circ f\\), de \\(\mathcal{C}(Y,A)\\) en \\(\mathcal{C}(X,A)\\).

La funtorialidad es la asociatividad de la composición: \\((g \circ f) \circ u = g \circ (f \circ u)\\). Los dos se combinan en un **bifuntor** \\(\mathcal{C}(-,-)\colon \mathcal{C}^{\mathrm{op}} \times \mathcal{C} \to \mathbf{Set}\\).

Observe que \\(\mathcal{P}^{-}\\) es, salvo una biyección, el funtor hom \\(\mathbf{Set}(-, \\{0,1\\})\\): un subconjunto de \\(X\\) es lo mismo que su función característica \\(X \to \\{0,1\\}\\), y la imagen inversa corresponde a componer. La duplicidad es un primer indicio de la representabilidad (Capítulo 5).

---

## 4. La categoría de categorías y propiedades de los funtores

Los funtores se componen: si \\(F\colon \mathcal{C} \to \mathcal{D}\\) y \\(G\colon \mathcal{D} \to \mathcal{E}\\), entonces \\(G \circ F\\) se define objeto por objeto y flecha por flecha. Cada categoría tiene un funtor identidad. Así se obtiene la categoría \\(\mathbf{Cat}\\) de categorías pequeñas y funtores.

> **Definición 2.13 (Fiel, pleno, plenamente fiel).**
> Un funtor \\(F\colon \mathcal{C} \to \mathcal{D}\\) es **fiel** si cada función \\(\mathcal{C}(A,B) \to \mathcal{D}(FA,FB)\\) es inyectiva, **pleno** si cada una es sobreyectiva, y **plenamente fiel** si cada una es biyectiva. Una **subcategoría plena** es una subcategoría cuya inclusión es plenamente fiel.

> **Ejemplo 2.14.**
>
> - \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) es fiel (dos homomorfismos con la misma función subyacente son iguales) pero no pleno (no toda función entre grupos es un homomorfismo).
> - \\(\mathbf{Ab}\\) es una subcategoría plena de \\(\mathbf{Grp}\\): un homomorfismo entre grupos abelianos no necesita condiciones extra.
> - Un funtor plenamente fiel **refleja isomorfismos**: si \\(F(f)\\) es isomorfismo, también lo es \\(f\\), porque la inversa de \\(F(f)\\) proviene de una única flecha de \\(\mathcal{C}\\).

### No todo es funtorial

> **Ejemplo 2.15 (El centro no es un funtor).**
> No existe un funtor \\(Z\colon \mathbf{Grp} \to \mathbf{Grp}\\) que envíe cada grupo a su centro, cualquiera que sea su acción sobre las flechas. Considérense la inclusión \\(i\colon \mathbb{Z}/2 \to S\_3\\) de una transposición y el signo \\(\mathrm{sgn}\colon S\_3 \to \mathbb{Z}/2\\). Su compuesto es \\(\mathrm{sgn} \circ i = 1\_{\mathbb{Z}/2}\\). Si \\(Z\\) fuera un funtor, entonces
>
> \\[
> Z(\mathrm{sgn}) \circ Z(i) = 1\_{Z(\mathbb{Z}/2)} = 1\_{\mathbb{Z}/2},
> \\]
>
> pero esta identidad pasaría por \\(Z(S\_3) = \\{e\\}\\), lo cual es imposible. El centro **sí** es funtorial si se restringe la categoría a grupos y epimorfismos (sobreyectivos), porque un homomorfismo sobreyectivo envía el centro dentro del centro.

> **📝 Para pensar.** Ante una construcción nueva (el centro, el conmutador, el grupo de automorfismos), ¿cuál es tu primer reflejo para decidir si es funtorial? Prueba con el subgrupo conmutador \\([G,G]\\) y con el grupo de automorfismos \\(\mathrm{Aut}(G)\\).

---

## 🔑 Lo que cristalizó

- Un **funtor** preserva composición e identidades; por eso preserva isomorfismos y produce **invariantes**.
- Olvidar estructura y construir objetos libres son funtores, y aparecen en parejas.
- Las acciones de grupos y las representaciones lineales son funtores desde \\(\mathbf{B}G\\).
- Los **funtores hom** \\(\mathcal{C}(A,-)\\) y \\(\mathcal{C}(-,A)\\) existen en toda categoría localmente pequeña y serán el centro del Capítulo 5.
- No toda construcción natural en apariencia es funtorial; el centro de un grupo es el contraejemplo clásico.

## 🌉 Puente

El determinante, el doble dual y la abelianización son construcciones que se sienten "canónicas": no dependen de elegir una base ni un representante. El Capítulo 3 da a esa intuición una definición: la **naturalidad**.
