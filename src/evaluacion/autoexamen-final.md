# Auto-examen Final

Este auto-examen es un **simulacro de examen de cierre** para *Teoría de Categorías desde Cero*. Cubre las seis Partes del libro con la estructura y la exigencia de un examen final: reactivos de opción múltiple, problemas de cálculo, construcción y verificación, y demostraciones formales.

Como el libro es de estudio autodidacta, nadie te va a aplicar un examen al terminarlo. Este simulacro cumple esa función: te permite **verificar tu dominio antes de dar por terminado el estudio**. No busca asignarte una calificación, sino **mostrarte con precisión qué temas dominas y cuáles debes repasar**. Por eso cada reactivo está vinculado a la sección del libro donde se estudia su contenido.

El examen retoma los tres **puntos de control** del [Apéndice A](../apendices/a-plan-de-estudio.md) (semanas 4, 8 y 12) y los extiende a todo el libro:

| Punto de control del Apéndice A | Reactivos que lo evalúan |
| :--- | :--- |
| Semana 4, el lenguaje: categoría, funtor y transformación natural; lema de Yoneda; unicidad salvo isomorfismo único | 1 a 8, 21, 22, 29, 30 |
| Semana 8, la maquinaria: un límite y un colímite fuera de \\(\mathbf{Set}\\); una adjunción no vista en el libro; por qué los adjuntos preservan (co)límites | 11, 13 a 16, 24, 25, 31, 32 |
| Semana 12, los destinos: mónadas y sus álgebras; monoides internos; Yang–Baxter y el tercer movimiento de Reidemeister | 17 a 20, 26, 27, 28, 33, 34 |

---

## 📋 Instrucciones de aplicación

1. **Momento recomendado:** resuélvelo al terminar la semana 12 del plan de estudio, o cuando hayas leído el libro completo y resuelto los ejercicios clave de cada Parte. Si lo haces antes, tómalo como diagnóstico y repite el examen después de repasar.
2. **Condiciones de examen real:** reserva **3 horas continuas**, sin apuntes, sin el libro, sin el apéndice de soluciones y sin consultar la clave. No necesitas calculadora: todos los cálculos se hacen a mano. Escribe tus respuestas en hojas aparte.
3. **Distribución del tiempo sugerida:**

| Sección | Contenido | Reactivos | Puntos | Tiempo sugerido |
| :---: | :--- | :---: | :---: | :---: |
| I | Opción múltiple | 1 a 20 | 20 | 30 min |
| II | Respuesta corta, construcción y verificación | 21 a 28 | 32 | 60 min |
| III | Demostraciones | 29 a 34 | 48 | 90 min |
| | **Total** | **34** | **100** | **3 h** |

4. **Al terminar:** califícate con la clave y las rúbricas del final de esta página. Sé estricto: en un cálculo, un resultado correcto sin planteamiento no recibe el puntaje completo, y en una demostración, una idea correcta mal justificada tampoco. Después llena la **tabla de diagnóstico** para decidir qué repasar.

Para no confundir las secciones del examen con las Partes del libro, en este documento se escribe **Sección I, II, III** para las del examen y **Parte I a VI** para las del libro.

### Convenciones del libro

- **Composición:** \\(g \circ f\\) significa "primero \\(f\\), después \\(g\\)". El conjunto de flechas de \\(A\\) en \\(B\\) se escribe \\(\mathcal{C}(A, B)\\).
- **Adjunciones:** \\(F \dashv G\\), con \\(F\colon \mathcal{C} \to \mathcal{D}\\) y \\(G\colon \mathcal{D} \to \mathcal{C}\\), es una biyección \\(\mathcal{D}(FX, Y) \cong \mathcal{C}(X, GY)\\) natural en \\(X\\) y en \\(Y\\). La transpuesta de \\(g\\) se escribe \\(\overline{g}\\); la unidad es \\(\eta\colon 1 \Rightarrow GF\\) y la counidad, \\(\varepsilon\colon FG \Rightarrow 1\\).
- **Yoneda:** para un prehaz \\(F\colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}\\), \\(\mathrm{Nat}(\mathcal{C}(-, A), F) \cong F(A)\\) mediante \\(\alpha \mapsto \alpha\_A(1\_A)\\), con inversa \\(x \mapsto \Psi(x)\\), \\(\Psi(x)\_X(f) = F(f)(x)\\).
- **Mónadas:** \\((T, \eta, \mu)\\), con \\(\eta\colon 1 \Rightarrow T\\) y \\(\mu\colon TT \Rightarrow T\\). En la categoría de Kleisli \\(\mathcal{C}\_T\\), la composición de \\(f\colon X \to TY\\) y \\(g\colon Y \to TZ\\) es \\(g \circ\_T f = \mu\_Z \circ T(g) \circ f\\). Las álgebras forman \\(\mathcal{C}^T\\).
- **Trenzas:** \\(\sigma\_i\\) cruza las hebras \\(i\\) e \\(i+1\\), con la hebra \\(i\\) por encima.
- **Corchete de Kauffman:** \\(\langle \bigcirc \rangle = 1\\), \\(\langle D \sqcup \bigcirc \rangle = \delta \langle D \rangle\\) con \\(\delta = -A^2 - A^{-2}\\), y en cada cruce \\(\langle \text{cruce} \rangle = A \langle \text{suavizado A} \rangle + A^{-1} \langle \text{suavizado B} \rangle\\). Para \\(\sigma\_i\\), el suavizado A es el de dos hebras paralelas (la identidad) y el B es \\(e\_i = \mathrm{coev} \circ \mathrm{ev}\\). La corrección por la torsión es \\(X(L) = (-A^3)^{-w(D)} \langle D \rangle\\), y \\(A = t^{-1/4}\\) da el polinomio de Jones.

---

## 📝 Sección I. Opción múltiple (20 puntos, 1 punto cada reactivo)

Elige **una sola** respuesta en cada reactivo.

### Parte I del libro. El lenguaje de las categorías

**1.** Sean \\(f\colon A \to B\\) y \\(g\colon B \to C\\) flechas de una categoría \\(\mathcal{C}\\). En la categoría opuesta \\(\mathcal{C}^{\mathrm{op}}\\), la expresión \\(f^{\mathrm{op}} \circ g^{\mathrm{op}}\\):

- A) no está definida, porque en \\(\mathcal{C}^{\mathrm{op}}\\) la flecha \\(f^{\mathrm{op}}\\) va de \\(A\\) en \\(B\\).
- B) es igual a \\((f \circ g)^{\mathrm{op}}\\).
- C) es una flecha \\(C \to A\\) igual a \\((g \circ f)^{\mathrm{op}}\\).
- D) es una flecha \\(A \to C\\) igual a \\(g \circ f\\).

**2.** En \\(\mathbf{Mon}\\), considera la inclusión \\(j\colon (\mathbb{N}, +, 0) \to (\mathbb{Z}, +, 0)\\). Entonces \\(j\\):

- A) es monomorfismo y epimorfismo, pero no es isomorfismo.
- B) es monomorfismo, pero no es epimorfismo, porque no es sobreyectiva.
- C) es isomorfismo, porque es a la vez monomorfismo y epimorfismo.
- D) no es monomorfismo, porque \\(\mathbb{N}\\) no es un grupo.

**3.** Sea \\(\Delta\colon \mathbf{Set} \to \mathbf{Set}\\) el funtor \\(X \mapsto X \times X\\), \\(f \mapsto f \times f\\). ¿Cuántas transformaciones naturales \\(1\_{\mathbf{Set}} \Rightarrow \Delta\\) hay?

- A) Ninguna.
- B) Exactamente dos, inducidas por las proyecciones \\(\pi\_1\\) y \\(\pi\_2\\).
- C) Una por cada manera de elegir un elemento en cada conjunto no vacío.
- D) Exactamente una: la diagonal \\(x \mapsto (x, x)\\).

**4.** Sea \\(F\colon \mathcal{C} \to \mathcal{D}\\) un funtor plenamente fiel y esencialmente sobreyectivo. ¿Cuál afirmación es **necesariamente** verdadera?

- A) \\(F\\) es biyectivo en los objetos.
- B) Existe un funtor \\(G\colon \mathcal{D} \to \mathcal{C}\\) con \\(GF \cong 1\_{\mathcal{C}}\\) y \\(FG \cong 1\_{\mathcal{D}}\\).
- C) \\(F\\) es un isomorfismo de categorías.
- D) \\(F\\) es inyectivo en los objetos.

### Parte II del libro. Universalidad y representabilidad

**5.** Sea \\(I\\) un conjunto con al menos dos elementos. ¿Cuál es el objeto terminal de la categoría rebanada \\(\mathbf{Set}/I\\)?

- A) La única función \\(\emptyset \to I\\).
- B) La función \\(I \to \\{\star\\}\\).
- C) Cualquier función \\(\\{\star\\} \to I\\).
- D) La identidad \\(1\_I\colon I \to I\\).

**6.** En el orden \\((\mathbb{N}, \mid)\\) visto como categoría, el producto y el coproducto de \\(12\\) y \\(18\\) son, respectivamente:

- A) \\(6\\) y \\(36\\).
- B) \\(36\\) y \\(6\\).
- C) \\(216\\) y \\(30\\).
- D) \\(6\\) y \\(216\\).

**7.** Sea \\(\mathcal{C}\\) el orden \\(\\{0 \le 1 \le 2\\}\\) visto como categoría y sea \\(F\colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}\\) el prehaz con \\(F(0) = \\{a, b, c\\}\\), \\(F(1) = \\{a, b\\}\\), \\(F(2) = \\{a\\}\\), cuyas funciones de restricción \\(F(j) \to F(i)\\), para \\(i \le j\\), son las inclusiones. ¿Cuántas transformaciones naturales \\(\mathcal{C}(-, 1) \Rightarrow F\\) hay?

- A) 1
- B) 3
- C) 2
- D) 6

**8.** ¿Qué grupo representa al funtor \\(\mathbf{Grp} \to \mathbf{Set}\\), \\(G \mapsto \\{(g, h) \in G \times G \mid g^2 = e\\}\\), con la acción evidente sobre homomorfismos?

- A) \\(\mathbb{Z}/2 \times \mathbb{Z}\\)
- B) \\(\mathbb{Z}/2 \ast \mathbb{Z}\\), el producto libre
- C) \\(\mathbb{Z}/2\\)
- D) \\(\mathbb{Z} \times \mathbb{Z}\\)

### Parte III del libro. Límites y colímites

**9.** Sea \\(D\\) un diagrama con forma de coespán, \\(D(j) \xrightarrow{D(u)} D(k) \xleftarrow{D(v)} D(l)\\). Su **colímite** es:

- A) el producto fibrado de \\(D(u)\\) y \\(D(v)\\).
- B) el objeto central \\(D(k)\\), con las flechas \\(D(u)\\), \\(1\_{D(k)}\\) y \\(D(v)\\).
- C) la suma amalgamada de \\(D(u)\\) y \\(D(v)\\).
- D) el coproducto \\(D(j) + D(k) + D(l)\\).

**10.** Sean \\(f, g\colon \mathbb{Z}/12 \to \mathbb{Z}/12\\) las funciones \\(f(x) = x^2\\) y \\(g(x) = x\\) (aritmética módulo 12), vistas como flechas de \\(\mathbf{Set}\\). Sean \\(E\\) su ecualizador y \\(Q\\) su coecualizador. Entonces:

- A) \\(E = \\{0, 1\\}\\) y \\(Q\\) tiene 4 elementos.
- B) \\(E = \\{0, 1, 4, 9\\}\\) y \\(Q\\) tiene 8 elementos.
- C) \\(E = \\{0, 1, 4, 9\\}\\) y \\(Q\\) tiene 12 elementos.
- D) \\(E = \\{0, 1, 4, 9\\}\\) y \\(Q\\) tiene 4 elementos.

**11.** Sea \\(G\\) un grupo. En la categoría de \\(G\\)-conjuntos \\([\mathbf{B}G, \mathbf{Set}]\\), el producto de \\(X\\) y \\(Y\\) es:

- A) \\(X \times Y\\) con \\(g \cdot (x, y) = (g \cdot x, y)\\).
- B) \\(X \sqcup Y\\), con la acción de \\(G\\) en cada pedazo.
- C) \\(X \times Y\\) con la acción diagonal \\(g \cdot (x, y) = (g \cdot x, g \cdot y)\\).
- D) El conjunto de órbitas de \\(X \times Y\\) bajo la acción diagonal.

**12.** ¿Cuál de las siguientes categorías **no** tiene todos los productos binarios?

- A) El orden \\(\\{a, b, c\\}\\) con \\(a \le c\\) y \\(b \le c\\) como únicas relaciones no reflexivas.
- B) \\((\mathcal{P}(X), \subseteq)\\), para un conjunto \\(X\\).
- C) \\(\mathbf{Ab}\\).
- D) La categoría de conjuntos finitos y funciones.

### Parte IV del libro. Adjunciones

**13.** Sea \\(f\colon \mathbb{Z} \to \mathbb{Z}\\), \\(f(n) = 2n\\), como funtor del orden usual \\((\mathbb{Z}, \le)\\) en sí mismo. ¿Cuál afirmación es correcta?

- A) \\(\lceil -/2 \rceil \dashv f \dashv \lfloor -/2 \rfloor\\).
- B) \\(\lfloor -/2 \rfloor \dashv f \dashv \lceil -/2 \rceil\\).
- C) \\(f\\) no tiene adjuntos, porque no es sobreyectiva.
- D) \\(f \dashv \lceil -/2 \rceil\\), y \\(f\\) no tiene adjunto izquierdo.

**14.** En la adjunción \\(L \dashv U\\) entre \\(\mathbf{Set}\\) y \\(\mathbf{Mon}\\) (monoide libre de listas y olvidadizo), la counidad \\(\varepsilon\_M\colon L(UM) \to M\\) es:

- A) la función \\(m \mapsto (m)\\), que ve cada elemento como una lista de longitud uno.
- B) el homomorfismo \\((m\_1, \dots, m\_n) \mapsto m\_1 \cdots m\_n\\), que envía la lista vacía al neutro.
- C) la concatenación de una lista de listas.
- D) la inclusión de \\(M\\) en \\(L(M)\\).

**15.** Sea \\(f\colon X \to Y\\) una función, con \\(\exists\_f \dashv f^{-1} \dashv \forall\_f\\) entre \\((\mathcal{P}(X), \subseteq)\\) y \\((\mathcal{P}(Y), \subseteq)\\). ¿Cuál igualdad vale para **todos** \\(f\\), \\(S\\) y \\(S'\\)?

- A) \\(f(S \cap S') = f(S) \cap f(S')\\).
- B) \\(f(X \setminus S) = Y \setminus f(S)\\).
- C) \\(\forall\_f(S \cup S') = \forall\_f(S) \cup \forall\_f(S')\\).
- D) \\(f(S \cup S') = f(S) \cup f(S')\\).

**16.** Considera la adjunción \\((-)^{\mathrm{ab}} \dashv i\\), donde \\(i\colon \mathbf{Ab} \to \mathbf{Grp}\\) es la inclusión. ¿Cuál afirmación es correcta?

- A) La unidad es un isomorfismo natural, pero la counidad no.
- B) La unidad y la counidad son isomorfismos naturales; es una equivalencia.
- C) La counidad es un isomorfismo natural, pero la unidad no.
- D) Ni la unidad ni la counidad son isomorfismos naturales.

### Parte V del libro. Mónadas

**17.** En la categoría de Kleisli de la mónada de conjunto potencia \\(\mathcal{P}\\), sean \\(f\colon \\{1, 2, 3\\} \to \mathcal{P}(\\{a, b\\})\\) con \\(f(1) = \\{a\\}\\), \\(f(2) = \\{a, b\\}\\), \\(f(3) = \emptyset\\), y \\(g\colon \\{a, b\\} \to \mathcal{P}(\\{x, y, z\\})\\) con \\(g(a) = \\{x\\}\\), \\(g(b) = \\{y, z\\}\\). ¿Cuánto vale \\((g \circ\_{\mathcal{P}} f)(2)\\)?

- A) \\(\\{x\\}\\)
- B) \\(\\{x, y, z\\}\\)
- C) \\(\emptyset\\)
- D) \\(\\{\\{x\\}, \\{y, z\\}\\}\\)

**18.** ¿Cuál de las siguientes funciones \\(c\colon \mathbb{Z} \to \mathbb{Z}\\) es una **mónada** sobre el orden \\((\mathbb{Z}, \le)\\) visto como categoría?

- A) \\(c(n) = n + 1\\)
- B) \\(c(n) = 2 \lfloor n/2 \rfloor\\)
- C) \\(c(n) = -n\\)
- D) \\(c(n) = 2 \lceil n/2 \rceil\\)

### Parte VI del libro. Hacia los nudos

**19.** ¿Qué es un **monoide** en la categoría monoidal \\((\mathbf{Set}, \sqcup, \emptyset)\\)?

- A) Un monoide usual: un conjunto con una operación asociativa y un neutro.
- B) Solo el conjunto vacío admite estructura de monoide.
- C) Todo conjunto \\(M\\) admite exactamente una: la codiagonal \\(m = [1\_M, 1\_M]\colon M \sqcup M \to M\\) con la única \\(e\colon \emptyset \to M\\).
- D) Un anillo con unidad.

**20.** ¿Cuál de las siguientes igualdades **no** se cumple en el grupo de trenzas \\(B\_4\\)?

- A) \\(\sigma\_1 \sigma\_2 = \sigma\_2 \sigma\_1\\)
- B) \\(\sigma\_1 \sigma\_3 = \sigma\_3 \sigma\_1\\)
- C) \\(\sigma\_2 \sigma\_3 \sigma\_2 = \sigma\_3 \sigma\_2 \sigma\_3\\)
- D) \\(\sigma\_1 \sigma\_3 \sigma\_2 = \sigma\_3 \sigma\_1 \sigma\_2\\)

---

## 📝 Sección II. Respuesta corta, construcción y verificación (32 puntos, 4 puntos cada reactivo)

Muestra tu procedimiento: di qué categoría, funtor o flecha usas, escribe la definición o la propiedad universal que aplicas y después calcula. Una respuesta final sin justificación recibe a lo sumo 1 punto.

**21.** *(Naturalidad.)* Sea \\(L\colon \mathbf{Set} \to \mathbf{Set}\\) el funtor de listas, \\(L(f)(x\_1, \dots, x\_n) = (f(x\_1), \dots, f(x\_n))\\).

- a) Sea \\(\mathrm{rev}\_X\colon L(X) \to L(X)\\), \\((x\_1, \dots, x\_n) \mapsto (x\_n, \dots, x\_1)\\). Demuestra que \\(\mathrm{rev}\colon L \Rightarrow L\\) es natural.
- b) Sea \\(K\_{\mathbb{N}}\colon \mathbf{Set} \to \mathbf{Set}\\) el funtor constante con valor \\(\mathbb{N}\\) (que envía toda flecha a \\(1\_{\mathbb{N}}\\)). Demuestra que la longitud \\(\ell\_X\colon L(X) \to \mathbb{N}\\) es una transformación natural \\(L \Rightarrow K\_{\mathbb{N}}\\).
- c) Sea \\(\mathcal{P}\\) la potencia **covariante** (imagen directa). Demuestra con un contraejemplo explícito que el complemento \\(c\_X\colon \mathcal{P}(X) \to \mathcal{P}(X)\\), \\(S \mapsto X \setminus S\\), **no** es una transformación natural \\(\mathcal{P} \Rightarrow \mathcal{P}\\).
- d) Demuestra que la misma familia \\(c\_X\\) **sí** es una transformación natural \\(\mathcal{P}^{-} \Rightarrow \mathcal{P}^{-}\\) para la potencia contravariante (imagen inversa).

**22.** *(Representabilidad y Yoneda.)* Sea \\(F\colon \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}\\) el prehaz \\(F(X) = \mathcal{P}(X) \times \mathcal{P}(X)\\) que envía \\(f\colon X \to Y\\) a \\(F(f)(S, T) = (f^{-1}(S), f^{-1}(T))\\). Sean \\(R = \\{0, 1\\} \times \\{0, 1\\}\\), \\(S\_1 = \\{(1, 0), (1, 1)\\}\\), \\(S\_2 = \\{(0, 1), (1, 1)\\}\\) y \\(u = (S\_1, S\_2) \in F(R)\\).

- a) Demuestra que \\((R, u)\\) es un elemento universal de \\(F\\): para cada conjunto \\(X\\) y cada \\((S, T) \in F(X)\\) existe una única \\(f\colon X \to R\\) con \\(F(f)(u) = (S, T)\\). Concluye que \\(F \cong \mathbf{Set}(-, R)\\).
- b) Sea \\(2 = \\{0, 1\\}\\). Usa el lema de Yoneda para contar las transformaciones naturales \\(\mathbf{Set}(-, 2) \Rightarrow F\\).
- c) Describe explícitamente la componente \\(\Psi(x)\_X\colon \mathbf{Set}(X, 2) \to F(X)\\) de la transformación que corresponde a \\(x = (\\{0\\}, \\{0, 1\\}) \in F(2)\\).
- d) ¿Cuántas transformaciones naturales \\(F \Rightarrow F\\) hay? Justifica con el lema de Yoneda.

**23.** *(Límites y colímites en \\(\mathbf{Set}\\).)* Sean \\(A = \\{1, 2, 3, 4, 5\\}\\), \\(B = \\{p, q, r\\}\\) y \\(C = \\{0, 1, 2\\}\\).

- a) Sean \\(f\colon A \to C\\) con \\(f(1) = f(2) = 0\\), \\(f(3) = 1\\), \\(f(4) = f(5) = 2\\), y \\(g\colon B \to C\\) con \\(g(p) = 0\\), \\(g(q) = g(r) = 2\\). Calcula el producto fibrado \\(A \times\_C B\\): lista sus elementos y da sus dos proyecciones.
- b) Sean \\(K = \\{s, t, u\\}\\), \\(h\colon K \to A\\) con \\(h(s) = 1\\), \\(h(t) = 2\\), \\(h(u) = 3\\), y \\(k\colon K \to B\\) con \\(k(s) = k(t) = p\\), \\(k(u) = q\\). Calcula la suma amalgamada de \\(h\\) y \\(k\\): describe sus clases y di cuántos elementos tiene.
- c) Sean \\(\varphi, \psi\colon \\{a, b\\} \rightrightarrows \\{1, 2, 3, 4, 5, 6\\}\\) con \\(\varphi(a) = 1\\), \\(\psi(a) = 2\\), \\(\varphi(b) = 2\\), \\(\psi(b) = 3\\). Calcula su coecualizador y explica por qué hay que tomar la relación de equivalencia **generada**.

**24.** *(Límites y colímites en \\(\mathbf{Grp}\\).)* Todos los grupos son aditivos.

- a) Sean \\(f, g\colon \mathbb{Z}/12 \to \mathbb{Z}/12\\) los homomorfismos \\(f(x) = 5x\\) y \\(g(x) = x\\). Calcula su ecualizador en \\(\mathbf{Grp}\\) e identifica el grupo que resulta.
- b) Calcula el coecualizador de \\(f\\) y \\(g\\) en \\(\mathbf{Grp}\\) e identifica el grupo cociente.
- c) Sean \\(p\colon \mathbb{Z}/4 \to \mathbb{Z}/2\\) y \\(q\colon \mathbb{Z}/6 \to \mathbb{Z}/2\\) las reducciones módulo 2. Calcula el producto fibrado \\(\mathbb{Z}/4 \times\_{\mathbb{Z}/2} \mathbb{Z}/6\\) en \\(\mathbf{Grp}\\): su orden y su tipo de isomorfismo.
- d) ¿Es cíclico el producto \\(\mathbb{Z}/4 \times \mathbb{Z}/6\\)? Compara con c).

**25.** *(Una adjunción concreta.)* Para un monoide \\(M\\), sea \\(M^{\times}\\) el grupo de sus elementos invertibles. Un homomorfismo de monoides envía invertibles en invertibles, así que \\((-)^{\times}\colon \mathbf{Mon} \to \mathbf{Grp}\\) es un funtor. Sea \\(i\colon \mathbf{Grp} \to \mathbf{Mon}\\) la inclusión.

- a) Demuestra que hay una biyección \\(\mathbf{Mon}(iG, M) \cong \mathbf{Grp}(G, M^{\times})\\), natural en \\(G\\) y en \\(M\\). ¿Cuál de los dos funtores es el adjunto izquierdo?
- b) Describe la unidad \\(\eta\_G\\) y la counidad \\(\varepsilon\_M\\) de la adjunción.
- c) Verifica las dos identidades triangulares.
- d) Usa el teorema de preservación de límites de los adjuntos para calcular el número de elementos invertibles del monoide producto \\((\mathbb{Z}/8, \cdot) \times (\mathbb{Z}/9, \cdot)\\).

**26.** *(Una mónada concreta.)* Fija un conjunto \\(E\\). Sea \\(T\colon \mathbf{Set} \to \mathbf{Set}\\), \\(T(X) = X^E = \mathbf{Set}(E, X)\\) y \\(T(f)(\varphi) = f \circ \varphi\\). Define \\(\eta\_X(x) = c\_x\\), la función constante con valor \\(x\\), y \\(\mu\_X\colon (X^E)^E \to X^E\\) por \\(\mu\_X(\Phi)(e) = \Phi(e)(e)\\).

- a) Verifica que \\(\mu\\) es una transformación natural \\(TT \Rightarrow T\\).
- b) Verifica las dos leyes de unidad \\(\mu \circ \eta T = 1\_T = \mu \circ T\eta\\).
- c) Verifica la ley de asociatividad \\(\mu \circ T\mu = \mu \circ \mu T\\).
- d) Sean \\(E = \\{0, 1\\}\\) y \\(X = \\{0, 1, 2\\}\\). Calcula \\(\mu\_X(\Phi)\\) para \\(\Phi(0) = \varphi\_0\\), \\(\Phi(1) = \varphi\_1\\), con \\(\varphi\_0(0) = 0\\), \\(\varphi\_0(1) = 1\\), \\(\varphi\_1(0) = 2\\), \\(\varphi\_1(1) = 0\\). Después verifica que \\(a\colon A^E \to A\\), \\(a(\varphi) = \varphi(0)\\), es una \\(T\\)-álgebra para todo conjunto \\(A\\).

**27.** *(Composición de Kleisli.)*

- a) En la categoría de Kleisli de la mónada \\(\mathcal{D}\\) de distribuciones finitas, sean \\(f\colon \\{a, b\\} \rightsquigarrow \\{1, 2, 3\\}\\) y \\(g\colon \\{1, 2, 3\\} \rightsquigarrow \\{u, v\\}\\) dadas por
  - \\(f(a) = \left(\tfrac{1}{2}, \tfrac{1}{2}, 0\right)\\) y \\(f(b) = \left(0, \tfrac{1}{3}, \tfrac{2}{3}\right)\\), como distribuciones sobre \\((1, 2, 3)\\);
  - \\(g(1) = (1, 0)\\), \\(g(2) = \left(\tfrac{1}{4}, \tfrac{3}{4}\right)\\) y \\(g(3) = \left(\tfrac{1}{2}, \tfrac{1}{2}\right)\\), como distribuciones sobre \\((u, v)\\).

  Calcula \\(g \circ\_{\mathcal{D}} f\\) a partir de la definición \\(\mu \circ \mathcal{D}(g) \circ f\\).
- b) Escribe \\(f\\) y \\(g\\) como matrices estocásticas (columnas que suman 1) y comprueba tu resultado con un producto de matrices.
- c) Sea \\(p\colon \\{\star\\} \rightsquigarrow \\{a, b\\}\\) la distribución \\(p = \left(\tfrac{1}{3}, \tfrac{2}{3}\right)\\). Calcula la distribución marginal sobre \\(\\{u, v\\}\\) de dos maneras, como \\((g \circ\_{\mathcal{D}} f) \circ\_{\mathcal{D}} p\\) y como \\(g \circ\_{\mathcal{D}} (f \circ\_{\mathcal{D}} p)\\). ¿Qué ley de la categoría de Kleisli ilustra la coincidencia?
- d) En la categoría de Kleisli de la mónada de elementos opcionales \\(X \mapsto X + \\{\bot\\}\\), sean \\(\alpha, \beta\colon \mathbb{N} \to \mathbb{N} + \\{\bot\\}\\) con \\(\alpha(n) = n/2\\) si \\(n\\) es par y \\(\alpha(n) = \bot\\) si \\(n\\) es impar, y \\(\beta(n) = n - 3\\) si \\(n \ge 3\\) y \\(\beta(n) = \bot\\) si \\(n < 3\\). Calcula \\((\beta \circ\_T \alpha)(10)\\), \\((\beta \circ\_T \alpha)(4)\\) y \\((\alpha \circ\_T \beta)(9)\\).

**28.** *(Corchete de Kauffman.)* Sea \\(D\\) el diagrama que se obtiene al **cerrar** la trenza \\(\sigma\_1^4 \in B\_2\\): los extremos superiores de las dos hebras se unen con los inferiores mediante arcos exteriores, sin cruces nuevos. Es un diagrama con 4 cruces del enlace toroidal \\(T(2,4)\\), de dos componentes. Usa las convenciones del libro (recuadro de convenciones).

- a) Un estado es una elección de suavizado A o B en cada uno de los 4 cruces. Para cada \\(j = 0, 1, 2, 3, 4\\), di cuántos estados tienen exactamente \\(j\\) suavizados B, cuál es su peso en \\(A\\) y cuántos círculos producen. *(Sugerencia: \\(e\_1 \circ e\_1 = \delta\\, e\_1\\).)*
- b) Calcula \\(\langle D \rangle\\) como un polinomio de Laurent en \\(A\\).
- c) Orienta las dos componentes de modo que las dos hebras de la trenza suban; con la convención del libro, cada cruce \\(\sigma\_1\\) tiene entonces signo \\(+1\\). Calcula \\(w(D)\\), \\(X(L)\\) y el polinomio de Jones \\(V\_L(t)\\).
- d) La imagen especular de \\(D\\) es la cerradura de \\(\sigma\_1^{-4}\\). Calcula su invariante \\(X\\) y decide si \\(X\\) distingue a este enlace orientado de su imagen especular.

---

## 📝 Sección III. Demostraciones (48 puntos, 8 puntos cada una)

Redacta cada demostración en prosa matemática completa: declara lo que supones y lo que quieres probar, justifica cada paso con una definición, un axioma o un resultado del libro citado con precisión, y cierra con una conclusión explícita.

**29.** *(Unicidad salvo isomorfismo único.)* Sea \\(U\colon \mathcal{D} \to \mathcal{C}\\) un funtor y \\(C\\) un objeto de \\(\mathcal{C}\\). Sean \\((A, \eta)\\) y \\((A', \eta')\\) dos flechas universales de \\(C\\) a \\(U\\) (Definición 4.9).

- a) Demuestra, directamente a partir de la definición y sin usar la Proposición 4.14, que existe una flecha \\(\varphi\colon A \to A'\\) con \\(U(\varphi) \circ \eta = \eta'\\) y una flecha \\(\psi\colon A' \to A\\) con \\(U(\psi) \circ \eta' = \eta\\).
- b) Demuestra que \\(\psi \circ \varphi = 1\_A\\) y \\(\varphi \circ \psi = 1\_{A'}\\).
- c) Demuestra que \\(\varphi\\) es el **único** isomorfismo \\(A \to A'\\) que cumple \\(U(\varphi) \circ \eta = \eta'\\).
- d) Aplica el resultado: si \\(q\colon G \to Q\\) es un homomorfismo hacia un grupo abeliano tal que todo homomorfismo de \\(G\\) en un grupo abeliano se factoriza de manera única por \\(q\\), ¿qué relación hay entre \\(Q\\) y \\(G^{\mathrm{ab}}\\)?

**30.** *(Un caso del lema de Yoneda: monoides.)* Sea \\(M\\) un monoide y \\(\mathbf{B}M\\) la categoría con un objeto \\(\star\\) asociada (Ejemplo 1.6).

- a) Demuestra que un prehaz \\(X\colon \mathbf{B}M^{\mathrm{op}} \to \mathbf{Set}\\) es lo mismo que un conjunto \\(X = X(\star)\\) con una **acción derecha** \\(x \cdot m = X(m)(x)\\), que cumple \\(x \cdot e = x\\) y \\((x \cdot m) \cdot n = x \cdot (mn)\\). Identifica el representable \\(\mathbf{B}M(-, \star)\\) y explica por qué una transformación natural \\(\alpha\colon \mathbf{B}M(-, \star) \Rightarrow X\\) es una función \\(\alpha\colon M \to X\\) con \\(\alpha(v m) = \alpha(v) \cdot m\\).
- b) Demuestra, sin citar el Teorema 5.4, que la función \\(\alpha \mapsto \alpha(e)\\) es una biyección entre esas transformaciones naturales y \\(X\\), y da su inversa.
- c) Deduce que las funciones \\(\alpha\colon M \to M\\) con \\(\alpha(v m) = \alpha(v) m\\) son exactamente las multiplicaciones por la izquierda \\(v \mapsto a v\\), con \\(a \in M\\), y que la composición de dos de ellas corresponde al producto en \\(M\\).

**31.** *(Monomorfismos y productos fibrados.)* Sea \\(m\colon A \to B\\) una flecha de una categoría \\(\mathcal{C}\\).

- a) Demuestra que \\(m\\) es un monomorfismo si y solo si el cuadrado
  \\[
\begin{array}{ccc}
  A & \xrightarrow{\ 1\_A\ } & A \\\\
  {\scriptstyle 1\_A} \Big\downarrow & & \Big\downarrow {\scriptstyle m} \\\\
  A & \xrightarrow[\ m\ ]{} & B
  \end{array}
\\]
  es un producto fibrado de \\(m\\) consigo misma.
- b) Deduce que todo funtor que preserva productos fibrados preserva monomorfismos.
- c) Concluye que todo adjunto derecho preserva monomorfismos. Indica qué resultado del libro usas.

**32.** *(Los adjuntos derechos preservan productos y el objeto terminal.)* Sea \\(F \dashv G\\), con \\(F\colon \mathcal{C} \to \mathcal{D}\\) y \\(G\colon \mathcal{D} \to \mathcal{C}\\). Usa solo la biyección natural \\(\mathcal{D}(FX, Y) \cong \mathcal{C}(X, GY)\\) y su regla de naturalidad; no cites el Teorema 9.2.

- a) Sea \\((A \times B, \pi\_1, \pi\_2)\\) un producto en \\(\mathcal{D}\\). Demuestra que \\((G(A \times B), G\pi\_1, G\pi\_2)\\) es un producto de \\(GA\\) y \\(GB\\) en \\(\mathcal{C}\\).
- b) Demuestra que si \\(1\\) es terminal en \\(\mathcal{D}\\), entonces \\(G1\\) es terminal en \\(\mathcal{C}\\).
- c) Acepta sin prueba el enunciado dual: un adjunto izquierdo preserva el objeto inicial. Demuestra que la potencia covariante \\(\mathcal{P}\colon \mathbf{Set} \to \mathbf{Set}\\) no tiene adjunto izquierdo **ni** adjunto derecho.

**33.** *(La mónada de una adjunción y sus álgebras.)* Sea \\(F \dashv G\\), con \\(F\colon \mathcal{C} \to \mathcal{D}\\), unidad \\(\eta\\) y counidad \\(\varepsilon\\), y sean \\(T = GF\\) y \\(\mu = G\varepsilon F\\).

- a) Demuestra las leyes de unidad \\(\mu \circ \eta T = 1\_T\\) y \\(\mu \circ T\eta = 1\_T\\), componente por componente.
- b) Demuestra la ley de asociatividad \\(\mu \circ T\mu = \mu \circ \mu T\\).
- c) Demuestra que, para todo objeto \\(Y\\) de \\(\mathcal{D}\\), el par \\((GY, G\varepsilon\_Y)\\) es una \\(T\\)-álgebra.
- d) Demuestra que, para toda flecha \\(h\colon Y \to Y'\\) de \\(\mathcal{D}\\), \\(G(h)\\) es un morfismo de \\(T\\)-álgebras \\((GY, G\varepsilon\_Y) \to (GY', G\varepsilon\_{Y'})\\).

**34.** *(Representaciones de grupos de trenzas.)* Sea \\(\mathcal{V}\\) una categoría monoidal trenzada, con trenzado \\(c\\); omite los asociadores, como en el Capítulo 13. Sea \\(A\\) un objeto y escribe \\(c = c\_{A,A}\\). En \\(A^{\otimes 3}\\) define \\(\rho(\sigma\_1) = c \otimes 1\_A\\) y \\(\rho(\sigma\_2) = 1\_A \otimes c\\); en \\(A^{\otimes 4}\\) define \\(\rho(\sigma\_1) = c \otimes 1\_A \otimes 1\_A\\), \\(\rho(\sigma\_2) = 1\_A \otimes c \otimes 1\_A\\) y \\(\rho(\sigma\_3) = 1\_A \otimes 1\_A \otimes c\\).

- a) Demuestra que \\(\rho(\sigma\_1) \rho(\sigma\_2) \rho(\sigma\_1) = \rho(\sigma\_2) \rho(\sigma\_1) \rho(\sigma\_2)\\) en \\(A^{\otimes 3}\\), a partir de la naturalidad del trenzado y de un axioma del hexágono (sin citar la Proposición 13.2).
- b) Demuestra que \\(\rho(\sigma\_1) \rho(\sigma\_3) = \rho(\sigma\_3) \rho(\sigma\_1)\\) en \\(A^{\otimes 4}\\). ¿Qué propiedad del producto tensorial usas?
- c) Explica por qué \\(\rho\\) se extiende a un homomorfismo de grupos \\(B\_4 \to \mathrm{Aut}(A^{\otimes 4})\\).
- d) Demuestra que si \\(\mathcal{V}\\) es simétrica, entonces \\(\rho(\sigma\_i)^2 = 1\\) para todo \\(i\\), y explica qué consecuencia tiene esto para las representaciones que se obtienen así.

---

## 🔑 Clave de respuestas y soluciones

No abras estos bloques hasta haber terminado el examen completo.

<details>
<summary><strong>Mostrar / ocultar la clave de la Sección I</strong></summary>

| Reactivo | Respuesta | Justificación breve |
| :---: | :---: | :--- |
| 1 | C | \\(g^{\mathrm{op}}\colon C \to B\\) y \\(f^{\mathrm{op}}\colon B \to A\\), así que \\(f^{\mathrm{op}} \circ g^{\mathrm{op}}\colon C \to A\\), y por definición vale \\((g \circ f)^{\mathrm{op}}\\). A olvida que \\(f^{\mathrm{op}}\\) va de \\(B\\) en \\(A\\); B invierte el orden de composición (\\(f \circ g\\) ni siquiera está definida); D no invierte las flechas. |
| 2 | A | \\(j\\) es inyectiva, luego mono. Es epi: si \\(h, k\colon \mathbb{Z} \to M\\) coinciden en \\(\mathbb{N}\\), entonces \\(h(-1)\\) y \\(k(-1)\\) son inversos de \\(h(1) = k(1)\\), y el inverso es único (argumento de la Proposición 1.11), así que \\(h = k\\). No es iso porque no es biyectiva. B confunde epi con sobreyectiva; C cree que mono y epi implica iso. |
| 3 | D | Para \\(x\colon \\{\star\\} \to X\\), la naturalidad da \\(\alpha\_X(x) = (x \times x)(\alpha\_{\\{\star\\}}(\star)) = (x, x)\\), pues \\(\alpha\_{\\{\star\\}}(\star) = (\star, \star)\\) es forzado. B confunde el sentido: las proyecciones van de \\(X \times X\\) a \\(X\\). C describe una familia que depende de elecciones, lo opuesto a la naturalidad. |
| 4 | B | Es el Teorema 3.11. A, C y D fallan: un funtor de la categoría con dos objetos isomorfos (y una flecha entre cada par) en \\(\mathbf{1}\\) es plenamente fiel y esencialmente sobreyectivo, pero no es inyectivo en objetos; una equivalencia no tiene por qué ser un isomorfismo de categorías (\\(\mathbf{Mat}\_k \simeq \mathbf{FinVect}\_k\\)). |
| 5 | D | Una flecha \\(p \to 1\_I\\) es una \\(h\colon A \to I\\) con \\(1\_I \circ h = p\\), es decir, \\(h = p\\): hay exactamente una. A es el objeto **inicial**. B no es un objeto de \\(\mathbf{Set}/I\\). C confunde con el terminal de \\(\mathbf{Set}\\): si \\(p\\) no es constante, no hay flechas de \\(p\\) hacia \\(\\{\star\\} \to I\\). |
| 6 | A | En \\((\mathbb{N}, \mid)\\) el producto es el ínfimo, \\(\gcd(12, 18) = 6\\), y el coproducto es el supremo, \\(\mathrm{lcm}(12, 18) = 36\\). B dualiza mal; C usa la aritmética de \\(\mathbb{N}\\) en lugar del orden. |
| 7 | C | Por Yoneda, el número es \\(\lvert F(1) \rvert = 2\\). Directamente: \\(\mathcal{C}(0, 1)\\) y \\(\mathcal{C}(1, 1)\\) tienen un elemento, \\(\mathcal{C}(2, 1) = \emptyset\\), y la naturalidad obliga a que \\(\alpha\_0\\) y \\(\alpha\_1\\) elijan el mismo elemento de \\(F(1) \subseteq F(0)\\). A cuenta \\(F(2)\\) y B cuenta \\(F(0)\\), es decir, evalúan en el objeto equivocado. |
| 8 | B | Por la propiedad universal del coproducto en \\(\mathbf{Grp}\\), \\(\mathbf{Grp}(\mathbb{Z}/2 \ast \mathbb{Z}, G) \cong \mathbf{Grp}(\mathbb{Z}/2, G) \times \mathbf{Grp}(\mathbb{Z}, G)\\), que son los pares con \\(g^2 = e\\) y \\(h\\) arbitrario. A confunde coproducto con producto: \\(\mathbb{Z}/2 \times \mathbb{Z}\\) representa solo los pares que además **conmutan** (en \\(S\_3\\) hay 24 pares con \\(g^2 = e\\) y solo 12 de ellos conmutan). |
| 9 | B | El coespán tiene objeto terminal \\(k\\), y el colímite de un diagrama cuya forma tiene objeto terminal es el valor en ese objeto (tabla del Capítulo 6). A da el **límite**; C confunde la forma con la del espán. |
| 10 | D | \\(E = \\{x \mid x^2 \equiv x\\} = \\{0, 1, 4, 9\\}\\), los idempotentes de \\(\mathbb{Z}/12\\). La relación de equivalencia generada por \\(x^2 \sim x\\) tiene las clases \\(\\{0, 6\\}\\), \\(\\{1, 5, 7, 11\\}\\), \\(\\{2, 4, 8, 10\\}\\) y \\(\\{3, 9\\}\\). A razona como en un dominio entero, donde \\(x(x - 1) = 0\\) solo tiene las raíces \\(0\\) y \\(1\\); B toma \\(12 - \lvert E \rvert\\); C no identifica nada. |
| 11 | C | Los límites en \\([\mathbf{B}G, \mathbf{Set}]\\) se calculan punto por punto (Proposición 7.10 y Corolario 7.11): el conjunto es \\(X \times Y\\) y la acción debe hacer equivariantes las dos proyecciones. Con la acción de A, \\(\pi\_2\\) no es equivariante. B es el **coproducto**. |
| 12 | A | En ese orden no hay ningún elemento menor o igual que \\(a\\) y que \\(b\\), así que no hay conos sobre \\(\\{a, b\\}\\) y no existe \\(a \wedge b\\). B tiene la intersección, C la suma directa y D el producto cartesiano finito; a D le faltan solo los productos **infinitos**. |
| 13 | A | \\(2n \le m \iff n \le \lfloor m/2 \rfloor\\) y \\(\lceil m/2 \rceil \le n \iff m \le 2n\\). B invierte el sentido de las adjunciones; C confunde tener adjuntos con ser biyectiva. |
| 14 | B | La counidad transpone \\(1\_{UM}\\): es el único homomorfismo \\(L(UM) \to M\\) que extiende \\(1\_{UM}\\), es decir, multiplicar la lista. A es la **unidad** \\(\eta\\); C es la multiplicación \\(\mu\\) de la mónada de listas, que vive en \\(\mathbf{Set}\\). |
| 15 | D | \\(\exists\_f\\) es adjunto **izquierdo**, así que preserva supremos: las uniones. Con \\(f\colon \\{1, 2\\} \to \\{0\\}\\), \\(S = \\{1\\}\\) y \\(S' = \\{2\\}\\) fallan A (\\(\emptyset \ne \\{0\\}\\)), B (\\(\\{0\\} \ne \emptyset\\)) y C (\\(\\{0\\} \ne \emptyset\\)). C confunde: \\(\forall\_f\\) es adjunto derecho y preserva intersecciones, no uniones. |
| 16 | C | \\(i\\) es plenamente fiel, así que la counidad \\((iA)^{\mathrm{ab}} \to A\\) es un isomorfismo (Proposición 9.6): abelianizar un grupo abeliano no lo cambia. La unidad \\(G \to G^{\mathrm{ab}}\\) es el cociente, que no es iso si \\(G\\) no es abeliano (por ejemplo, \\(S\_3\\)). A intercambia los papeles de unidad y counidad. |
| 17 | B | \\((g \circ\_{\mathcal{P}} f)(2) = \bigcup\_{y \in f(2)} g(y) = \\{x\\} \cup \\{y, z\\}\\). D omite el paso \\(\mu\\), la unión, y se queda en \\(\mathcal{P}\mathcal{P}(\\{x, y, z\\})\\); A usa solo \\(a \in f(2)\\). |
| 18 | D | Una mónada sobre un orden es un operador de cerradura: monótono, \\(n \le c(n)\\) y \\(c(c(n)) \le c(n)\\). \\(c(n) = 2\lceil n/2 \rceil\\), el menor par \\(\ge n\\), cumple las tres. A falla la multiplicación (\\(c(c(n)) = n + 2\\)), B falla la unidad (para \\(n\\) impar), C no es monótona. |
| 19 | C | Las leyes de unidad \\(m \circ (e \sqcup 1) = \lambda\\) y \\(m \circ (1 \sqcup e) = \rho\\) dicen que \\(m\\) es la identidad en cada copia de \\(M\\), es decir, \\(m = [1\_M, 1\_M]\\); la asociatividad se cumple sola. Es el dual de que en \\((\mathbf{Set}, \times, \\{\star\\})\\) todo conjunto es un comonoide de manera única. A confunde \\(\sqcup\\) con \\(\times\\). |
| 20 | A | B es la relación de hebras lejanas; C es la relación de Artin para \\(i = 2\\); D se sigue de B. A no se cumple: bajo el homomorfismo \\(B\_4 \to S\_4\\), \\(\sigma\_i \mapsto (i \ i{+}1)\\), se tiene \\((1\\,2)(2\\,3) \ne (2\\,3)(1\\,2)\\). Las hebras **adyacentes** satisfacen la relación de Yang–Baxter, no la conmutatividad. |

</details>

<details>
<summary><strong>Mostrar / ocultar las soluciones de la Sección II</strong></summary>

**Reactivo 21.** Sea \\(f\colon X \to Y\\) una función.

- a) \\(L(f)(\mathrm{rev}\_X(x\_1, \dots, x\_n)) = (f(x\_n), \dots, f(x\_1)) = \mathrm{rev}\_Y(f(x\_1), \dots, f(x\_n)) = \mathrm{rev}\_Y(L(f)(x\_1, \dots, x\_n))\\). El cuadrado \\(L(f) \circ \mathrm{rev}\_X = \mathrm{rev}\_Y \circ L(f)\\) conmuta.
- b) El cuadrado de naturalidad pide \\(K\_{\mathbb{N}}(f) \circ \ell\_X = \ell\_Y \circ L(f)\\), es decir, \\(\ell\_X(w) = \ell\_Y(L(f)(w))\\): aplicar \\(f\\) coordenada por coordenada no cambia la longitud.
- c) Sean \\(X = \\{0, 1\\}\\), \\(Y = \\{0\\}\\), \\(f\\) la función constante y \\(S = \\{0\\}\\). Entonces \\(\mathcal{P}(f)(c\_X(S)) = f(\\{1\\}) = \\{0\\}\\), mientras que \\(c\_Y(\mathcal{P}(f)(S)) = Y \setminus \\{0\\} = \emptyset\\). El cuadrado no conmuta. (Basta cualquier \\(f\\) no inyectiva o no sobreyectiva.)
- d) Para \\(T \subseteq Y\\): \\(f^{-1}(Y \setminus T) = \\{x \mid f(x) \notin T\\} = X \setminus f^{-1}(T)\\), es decir, \\(\mathcal{P}^{-}(f) \circ c\_Y = c\_X \circ \mathcal{P}^{-}(f)\\), que es el cuadrado de naturalidad de un funtor contravariante. La imagen inversa preserva complementos; la directa, no.

*Puntaje:* 1 por inciso. En c), un contraejemplo sin el cálculo explícito de los dos caminos recibe 0.5.

**Reactivo 22.**

- a) Para \\(f\colon X \to R\\), \\(F(f)(u) = (f^{-1}(S\_1), f^{-1}(S\_2))\\) es el par formado por los \\(x\\) cuya primera coordenada \\(f(x)\\) vale 1 y los \\(x\\) cuya segunda coordenada vale 1. Dado \\((S, T)\\), la condición \\(F(f)(u) = (S, T)\\) obliga a \\(f(x) = (\chi\_S(x), \chi\_T(x))\\), y esta \\(f\\) la cumple. Existe y es única, así que \\((R, u)\\) es un elemento universal y, por el Corolario 5.7, \\(F \cong \mathbf{Set}(-, R)\\). (Es la representabilidad de \\(\mathcal{P}^{-}\\) por \\(\\{0, 1\\}\\), Ejemplo 5.2, "elevada al cuadrado".)
- b) Por el lema de Yoneda, \\(\mathrm{Nat}(\mathbf{Set}(-, 2), F) \cong F(2) = \mathcal{P}(2) \times \mathcal{P}(2)\\), que tiene \\(4 \cdot 4 = 16\\) elementos.
- c) \\(\Psi(x)\_X(\varphi) = F(\varphi)(x) = (\varphi^{-1}(\\{0\\}), \varphi^{-1}(\\{0, 1\\})) = (\varphi^{-1}(0), X)\\).
- d) \\(\mathrm{Nat}(F, F) \cong \mathrm{Nat}(\mathbf{Set}(-, R), F) \cong F(R) = \mathcal{P}(R) \times \mathcal{P}(R)\\), con \\(2^4 \cdot 2^4 = 256\\) elementos.

*Puntaje:* 1.5 por a) (existencia y unicidad), 0.5 por b), 1 por c), 1 por d) (0.5 por usar el isomorfismo de a) y 0.5 por el conteo).

**Reactivo 23.**

- a) \\(A \times\_C B = \\{(a, b) \mid f(a) = g(b)\\} = \\{(1, p), (2, p), (4, q), (4, r), (5, q), (5, r)\\}\\), con 6 elementos (\\(2 \cdot 1\\) sobre el 0, \\(1 \cdot 0\\) sobre el 1 y \\(2 \cdot 2\\) sobre el 2), y las proyecciones \\(p\_1(a, b) = a\\), \\(p\_2(a, b) = b\\).
- b) Se toma \\(A \sqcup B\\) y se identifican \\(h(c) \sim k(c)\\): \\(1 \sim p\\), \\(2 \sim p\\), \\(3 \sim q\\). Las clases son \\(\\{1, 2, p\\}\\), \\(\\{3, q\\}\\), \\(\\{4\\}\\), \\(\\{5\\}\\) y \\(\\{r\\}\\): la suma amalgamada tiene 5 elementos. Observa que 1 y 2 quedan identificados aunque ningún elemento de \\(K\\) los relaciona directamente.
- c) Las relaciones \\(1 \sim 2\\) y \\(2 \sim 3\\) obligan, por transitividad, a \\(1 \sim 3\\). El coecualizador es \\(\\{1, \dots, 6\\}/\\!\sim\\) con clases \\(\\{1, 2, 3\\}\\), \\(\\{4\\}\\), \\(\\{5\\}\\), \\(\\{6\\}\\): 4 elementos. Se necesita la relación **generada** porque la flecha cociente \\(q\\) debe cumplir \\(q \circ \varphi = q \circ \psi\\) y ser una función, lo cual obliga a identificar todo lo que esté conectado por una cadena de relaciones (Ejemplo 6.9).

*Puntaje:* 1.5 por a), 1.5 por b), 1 por c).

**Reactivo 24.**

- a) \\(\\{x \mid 5x = x\\} = \\{x \mid 4x = 0\\} = \\{0, 3, 6, 9\\}\\), el subgrupo generado por 3, isomorfo a \\(\mathbb{Z}/4\\), con su inclusión.
- b) El coecualizador es el cociente por el subgrupo normal generado por \\(f(x) - g(x) = 4x\\), que es \\(\langle 4 \rangle = \\{0, 4, 8\\}\\). El cociente \\((\mathbb{Z}/12)/\langle 4 \rangle\\) es isomorfo a \\(\mathbb{Z}/4\\). (Como el grupo es abeliano, es también el conúcleo de \\(f - g\\) en \\(\mathbf{Ab}\\).)
- c) El olvidadizo crea límites, así que el producto fibrado es \\(\\{(a, b) \in \mathbb{Z}/4 \times \mathbb{Z}/6 \mid a \equiv b \pmod 2\\}\\) con la operación componente a componente. Tiene \\(4 \cdot 6/2 = 12\\) elementos, y \\((1, 1)\\) tiene orden \\(\mathrm{mcm}(4, 6) = 12\\). Luego es cíclico: \\(\mathbb{Z}/4 \times\_{\mathbb{Z}/2} \mathbb{Z}/6 \cong \mathbb{Z}/12\\).
- d) No: \\(\mathbb{Z}/4 \times \mathbb{Z}/6\\) tiene orden 24, pero todo elemento tiene orden a lo más \\(\mathrm{mcm}(4, 6) = 12\\). El producto fibrado es un subgrupo cíclico de índice 2 del producto.

*Puntaje:* 1 por a), 1 por b), 1.5 por c), 0.5 por d).

**Reactivo 25.**

- a) Sea \\(h\colon iG \to M\\) un homomorfismo de monoides. Para \\(g \in G\\), \\(h(g)\\,h(g^{-1}) = h(e) = 1 = h(g^{-1})\\,h(g)\\), así que \\(h(g) \in M^{\times}\\), y \\(h\\) se corestringe a un homomorfismo de grupos \\(G \to M^{\times}\\). Recíprocamente, un homomorfismo \\(G \to M^{\times}\\) seguido de la inclusión es un homomorfismo de monoides. Las dos asignaciones son inversas y no cambian la función subyacente, así que la biyección es natural (componer por los lados se hace con las mismas funciones). Como \\(i\\) aparece en el primer argumento, \\(i \dashv (-)^{\times}\\): la inclusión es el adjunto izquierdo.
- b) \\(\eta\_G\colon G \to (iG)^{\times} = G\\) es la identidad (todo elemento de un grupo es invertible). \\(\varepsilon\_M\colon i(M^{\times}) \to M\\) es la inclusión de las unidades.
- c) \\(\varepsilon\_{iG} \circ i(\eta\_G)\\) es la inclusión de \\((iG)^{\times} = G\\) en \\(iG\\), que es la identidad. \\((\varepsilon\_M)^{\times} \circ \eta\_{M^{\times}}\\) es la corestricción de la inclusión \\(M^{\times} \to M\\) a las unidades, que es la identidad de \\(M^{\times}\\).
- d) \\((-)^{\times}\\) es adjunto derecho, así que preserva productos: \\((M \times N)^{\times} \cong M^{\times} \times N^{\times}\\). Como \\((\mathbb{Z}/8)^{\times} = \\{1, 3, 5, 7\\}\\) y \\((\mathbb{Z}/9)^{\times} = \\{1, 2, 4, 5, 7, 8\\}\\), el producto tiene \\(4 \cdot 6 = 24\\) elementos invertibles.

*Puntaje:* 1 por a) (0.5 por la biyección y 0.5 por identificar el sentido), 1 por b), 1 por c), 1 por d).

**Reactivo 26.**

- a) Para \\(f\colon X \to Y\\) y \\(\Phi \in (X^E)^E\\): \\(T(f)(\mu\_X(\Phi)) = \big(e \mapsto f(\Phi(e)(e))\big)\\). Por otro lado, \\(TT(f)(\Phi) = T(f) \circ \Phi\\), que envía \\(e\\) a \\(f \circ \Phi(e)\\), y \\(\mu\_Y\\) de esto envía \\(e\\) a \\((f \circ \Phi(e))(e) = f(\Phi(e)(e))\\). Coinciden.
- b) \\(\eta\_{TX}(\varphi)\\) es la constante con valor \\(\varphi\\), así que \\(\mu\_X(\eta\_{TX}(\varphi))(e) = \varphi(e)\\). Y \\(T(\eta\_X)(\varphi) = \eta\_X \circ \varphi\\) envía \\(e\\) a \\(c\_{\varphi(e)}\\), así que \\(\mu\_X(T(\eta\_X)(\varphi))(e) = c\_{\varphi(e)}(e) = \varphi(e)\\). Ambos compuestos son la identidad.
- c) Para \\(\Xi \in ((X^E)^E)^E\\): \\(T(\mu\_X)(\Xi) = \mu\_X \circ \Xi\\) envía \\(e\\) a \\(e' \mapsto \Xi(e)(e')(e')\\), y al aplicar \\(\mu\_X\\) queda \\(e \mapsto \Xi(e)(e)(e)\\). Por otro lado, \\(\mu\_{TX}(\Xi) = (e \mapsto \Xi(e)(e))\\), y \\(\mu\_X\\) de esto es \\(e \mapsto \Xi(e)(e)(e)\\). Coinciden: se toma la "diagonal triple".
- d) \\(\mu\_X(\Phi)(0) = \varphi\_0(0) = 0\\) y \\(\mu\_X(\Phi)(1) = \varphi\_1(1) = 0\\): \\(\mu\_X(\Phi)\\) es la constante \\(0\\). Para \\(a(\varphi) = \varphi(0)\\): \\(a(\eta\_A(x)) = c\_x(0) = x\\), y \\(a(T(a)(\Phi)) = (a \circ \Phi)(0) = \Phi(0)(0) = \mu\_A(\Phi)(0) = a(\mu\_A(\Phi))\\). Se cumplen los dos axiomas de la Definición 10.10.

*Puntaje:* 1 por inciso; en d), 0.5 por el cálculo de \\(\mu\_X(\Phi)\\) y 0.5 por la verificación del álgebra.

**Reactivo 27.**

- a) \\(\mathcal{D}(g)\\) envía \\(f(x)\\) a una distribución sobre distribuciones, y \\(\mu\\) la promedia: \\((g \circ\_{\mathcal{D}} f)(z \mid x) = \sum\_y g(z \mid y)\\, f(y \mid x)\\) (Chapman–Kolmogorov). Así:
  - \\((g \circ f)(u \mid a) = 1 \cdot \tfrac{1}{2} + \tfrac{1}{4} \cdot \tfrac{1}{2} + \tfrac{1}{2} \cdot 0 = \tfrac{5}{8}\\) y \\((g \circ f)(v \mid a) = \tfrac{3}{8}\\);
  - \\((g \circ f)(u \mid b) = 1 \cdot 0 + \tfrac{1}{4} \cdot \tfrac{1}{3} + \tfrac{1}{2} \cdot \tfrac{2}{3} = \tfrac{5}{12}\\) y \\((g \circ f)(v \mid b) = \tfrac{7}{12}\\).
- b) Con filas indexadas por el codominio y columnas por el dominio,
  \\[
G\\,F = \begin{pmatrix} 1 & \tfrac{1}{4} & \tfrac{1}{2} \\\\ 0 & \tfrac{3}{4} & \tfrac{1}{2} \end{pmatrix} \begin{pmatrix} \tfrac{1}{2} & 0 \\\\ \tfrac{1}{2} & \tfrac{1}{3} \\\\ 0 & \tfrac{2}{3} \end{pmatrix} = \begin{pmatrix} \tfrac{5}{8} & \tfrac{5}{12} \\\\ \tfrac{3}{8} & \tfrac{7}{12} \end{pmatrix},
\\]
  y cada columna suma 1.
- c) Primera manera: \\(\tfrac{1}{3} \cdot \tfrac{5}{8} + \tfrac{2}{3} \cdot \tfrac{5}{12} = \tfrac{5}{24} + \tfrac{5}{18} = \tfrac{35}{72}\\) para \\(u\\), y \\(\tfrac{37}{72}\\) para \\(v\\). Segunda manera: \\(f \circ p = \left(\tfrac{1}{6}, \tfrac{7}{18}, \tfrac{4}{9}\right)\\) sobre \\(\\{1, 2, 3\\}\\), y luego \\(1 \cdot \tfrac{1}{6} + \tfrac{1}{4} \cdot \tfrac{7}{18} + \tfrac{1}{2} \cdot \tfrac{4}{9} = \tfrac{35}{72}\\) para \\(u\\). Coinciden por la **asociatividad** de la composición de Kleisli, que proviene de la naturalidad y la asociatividad de \\(\mu\\).
- d) \\((\beta \circ\_T \alpha)(10) = \beta(5) = 2\\); \\((\beta \circ\_T \alpha)(4) = \beta(2) = \bot\\); \\((\alpha \circ\_T \beta)(9) = \alpha(6) = 3\\). En cuanto un paso falla, el compuesto falla: es la composición de funciones parciales (Ejemplo 11.3).

*Puntaje:* 1.5 por a), 0.5 por b), 1 por c) (0.5 por cada manera, incluyendo la mención de la asociatividad), 1 por d).

**Reactivo 28.**

- a) Como \\(e\_1^j = \delta^{j-1} e\_1\\) y la cerradura de \\(e\_1\\) es un círculo, un estado con \\(j \ge 1\\) suavizados B tiene \\(j\\) círculos; el estado sin suavizados B (la identidad) tiene 2. El peso es \\(A^{(4-j) - j} = A^{4 - 2j}\\).

| \\(j\\) | Estados | Peso | Círculos | Contribución \\(A^{4-2j}\\,\delta^{(\text{círculos}) - 1}\\) |
| :---: | :---: | :---: | :---: | :--- |
| 0 | 1 | \\(A^{4}\\) | 2 | \\(A^4 \delta\\) |
| 1 | 4 | \\(A^{2}\\) | 1 | \\(4A^2\\) |
| 2 | 6 | \\(A^{0}\\) | 2 | \\(6\delta\\) |
| 3 | 4 | \\(A^{-2}\\) | 3 | \\(4A^{-2}\delta^2\\) |
| 4 | 1 | \\(A^{-4}\\) | 4 | \\(A^{-4}\delta^3\\) |

- b) Con \\(\delta = -A^2 - A^{-2}\\), \\(\delta^2 = A^4 + 2 + A^{-4}\\) y \\(\delta^3 = -A^6 - 3A^2 - 3A^{-2} - A^{-6}\\):
  \\[
\begin{aligned}
  \langle D \rangle &= (-A^6 - A^2) + 4A^2 + (-6A^2 - 6A^{-2}) + (4A^2 + 8A^{-2} + 4A^{-6}) + (-A^2 - 3A^{-2} - 3A^{-6} - A^{-10}) \\\\
  &= -A^6 - A^{-2} + A^{-6} - A^{-10}.
  \end{aligned}
\\]
- c) \\(w(D) = 4\\) y
  \\[
X(L) = (-A^3)^{-4} \langle D \rangle = A^{-12} \langle D \rangle = -A^{-6} - A^{-14} + A^{-18} - A^{-22}.
\\]
  Con \\(A = t^{-1/4}\\): \\(V\_L(t) = -t^{3/2} - t^{7/2} + t^{9/2} - t^{11/2}\\). (Comprobación: \\(V\_L(1) = -2 = (-2)^{c-1}\\) con \\(c = 2\\) componentes.)
- d) Para la imagen especular, \\(\langle D^{\ast} \rangle(A) = \langle D \rangle(A^{-1}) = -A^{-6} - A^{2} + A^{6} - A^{10}\\) y \\(w(D^{\ast}) = -4\\), así que \\(X(L^{\ast}) = A^{12} \langle D^{\ast} \rangle = -A^{6} - A^{14} + A^{18} - A^{22}\\), que es \\(X(L)\\) con \\(A\\) cambiado por \\(A^{-1}\\). Son polinomios distintos, así que \\(X\\) distingue a este enlace orientado de su imagen especular. También lo distingue del enlace de Hopf, cuyo \\(X\\) es \\(-A^{-2} - A^{-10}\\).

*Puntaje:* 1 por a), 1.5 por b), 1 por c) (0.5 por \\(X\\) y 0.5 por \\(V\\)), 0.5 por d).

</details>

<details>
<summary><strong>Mostrar / ocultar las soluciones y rúbricas de la Sección III</strong></summary>

### Rúbrica general (8 puntos por demostración)

| Criterio | Puntos | Se otorga cuando… |
| :--- | :---: | :--- |
| Estructura | 2 | Queda claro qué se supone y qué se quiere probar; las categorías, funtores y flechas están declarados con dominio y codominio. |
| Desarrollo | 4 | Cada paso es correcto y está justificado por una definición, un axioma o un resultado del libro citado con precisión. |
| Cierre y redacción | 2 | Se enuncia la conclusión y no se usa como hipótesis lo que se quiere probar. |

**Errores que cuestan puntos:** componer en el orden equivocado; confundir la existencia con la unicidad en una propiedad universal; dualizar mal (usar la propiedad del límite para un colímite); invertir el sentido de la adjunción o de la transposición; "verificar" una igualdad de transformaciones naturales en un solo objeto; usar el resultado que se pide demostrar (por ejemplo, citar el Teorema 9.2 en el reactivo 32).

La rúbrica específica de cada demostración reparte los 8 puntos por incisos; dentro de cada inciso se aplican los tres criterios generales.

**Demostración 29.**

a) Como \\((A, \eta)\\) es universal y \\(\eta'\colon C \to UA'\\) es una flecha de \\(\mathcal{C}\\), existe una única \\(\varphi\colon A \to A'\\) con \\(U(\varphi) \circ \eta = \eta'\\). Del mismo modo, por la universalidad de \\((A', \eta')\\) aplicada a \\(\eta\colon C \to UA\\), existe una única \\(\psi\colon A' \to A\\) con \\(U(\psi) \circ \eta' = \eta\\).

b) Por la funtorialidad de \\(U\\),

\\[
U(\psi \circ \varphi) \circ \eta = U(\psi) \circ U(\varphi) \circ \eta = U(\psi) \circ \eta' = \eta.
\\]

Pero también \\(U(1\_A) \circ \eta = 1\_{UA} \circ \eta = \eta\\). Por la **unicidad** en la propiedad universal de \\((A, \eta)\\), aplicada a la flecha \\(\eta\colon C \to UA\\), las dos flechas \\(\psi \circ \varphi\\) y \\(1\_A\\) coinciden. El mismo argumento con \\((A', \eta')\\) da \\(\varphi \circ \psi = 1\_{A'}\\). Luego \\(\varphi\\) es un isomorfismo con inversa \\(\psi\\).

c) Si \\(\varphi'\colon A \to A'\\) es otro isomorfismo con \\(U(\varphi') \circ \eta = \eta'\\), entonces \\(\varphi\\) y \\(\varphi'\\) son dos flechas que factorizan \\(\eta'\\) a través de \\(\eta\\); por la unicidad en la universalidad de \\((A, \eta)\\), \\(\varphi' = \varphi\\). (De hecho no hace falta suponer que \\(\varphi'\\) sea isomorfismo.)

d) Con \\(U = i\colon \mathbf{Ab} \to \mathbf{Grp}\\) y \\(C = G\\), tanto \\((G^{\mathrm{ab}}, q\_G)\\) (Ejemplo 4.11) como \\((Q, q)\\) son flechas universales de \\(G\\) a \\(i\\). Por a)–c), existe un único isomorfismo \\(\varphi\colon G^{\mathrm{ab}} \to Q\\) con \\(\varphi \circ q\_G = q\\). Cualquier construcción de la abelianización da el mismo grupo salvo isomorfismo único compatible con el cociente. \\(\blacksquare\\)

*Rúbrica específica:* a) vale 2 puntos (1 por cada flecha, citando la universalidad correcta); b) vale 3 (2 por el cálculo con la funtorialidad y 1 por invocar la unicidad en el objeto adecuado); c) vale 2; d) vale 1.

**Demostración 30.**

a) En \\(\mathbf{B}M\\), las flechas son los elementos de \\(M\\) y \\(m \circ n = mn\\). Un prehaz asigna a \\(\star\\) un conjunto \\(X\\) y a cada \\(m\\) una función \\(X(m)\colon X \to X\\), con \\(X(e) = 1\_X\\) y \\(X(m \circ n) = X(n) \circ X(m)\\) (contravariancia). Con \\(x \cdot m = X(m)(x)\\):

\\[
x \cdot (mn) = X(m \circ n)(x) = X(n)\big(X(m)(x)\big) = (x \cdot m) \cdot n, \qquad x \cdot e = x.
\\]

Recíprocamente, una acción derecha define un prehaz con \\(X(m)(x) = x \cdot m\\). El representable \\(\mathbf{B}M(-, \star)\\) es el conjunto \\(M\\) con \\(\mathbf{B}M(m, \star)(v) = v \circ m = vm\\): la acción derecha por multiplicación. Una transformación natural tiene una sola componente \\(\alpha\colon M \to X\\), y el cuadrado de naturalidad respecto de \\(m\\) dice \\(X(m) \circ \alpha = \alpha \circ \mathbf{B}M(m, \star)\\), es decir, \\(\alpha(v) \cdot m = \alpha(vm)\\).

b) Sea \\(\Phi(\alpha) = \alpha(e)\\) y, para \\(x \in X\\), sea \\(\Psi(x)(v) = x \cdot v\\).

- \\(\Psi(x)\\) es natural: \\(\Psi(x)(vm) = x \cdot (vm) = (x \cdot v) \cdot m = \Psi(x)(v) \cdot m\\).
- \\(\Phi(\Psi(x)) = x \cdot e = x\\).
- \\(\Psi(\Phi(\alpha))(v) = \alpha(e) \cdot v = \alpha(e v) = \alpha(v)\\), por la naturalidad de \\(\alpha\\) aplicada a \\(e\\) y \\(v\\).

Luego \\(\Phi\\) y \\(\Psi\\) son biyecciones inversas. Toda la información de \\(\alpha\\) está en \\(\alpha(e) = \alpha(1\_\star)\\), como en el paso (3) de la prueba del lema.

c) Se aplica b) con \\(X = M\\) y la acción derecha por multiplicación: las funciones \\(\alpha\\) con \\(\alpha(vm) = \alpha(v)m\\) corresponden biyectivamente a los \\(a = \alpha(e) \in M\\), y \\(\alpha = \Psi(a)\\) es \\(v \mapsto av\\), la multiplicación por la izquierda \\(\lambda\_a\\). Además, \\(\lambda\_a \circ \lambda\_b(v) = a(bv) = (ab)v = \lambda\_{ab}(v)\\), así que la composición corresponde al producto de \\(M\\), y \\(\lambda\_e = 1\_M\\). Es la versión para monoides del teorema de Cayley (Ejemplo 5.8). \\(\blacksquare\\)

*Rúbrica específica:* a) vale 2 puntos (1 por la acción derecha con la contravariancia bien usada, 1 por la condición de naturalidad); b) vale 3 (1 por la naturalidad de \\(\Psi(x)\\), 0.5 por \\(\Phi \circ \Psi\\), 1.5 por \\(\Psi \circ \Phi\\) señalando dónde se usa la naturalidad); c) vale 3 (2 por la identificación con \\(\lambda\_a\\) y 1 por la compatibilidad con el producto).

**Demostración 31.**

a) El cuadrado conmuta siempre: \\(m \circ 1\_A = m \circ 1\_A\\). Que sea un producto fibrado significa: para todo par \\(x, y\colon X \to A\\) con \\(m \circ x = m \circ y\\), existe una única \\(h\colon X \to A\\) con \\(1\_A \circ h = x\\) y \\(1\_A \circ h = y\\).

(\\(\Rightarrow\\)) Si \\(m\\) es mono y \\(m \circ x = m \circ y\\), entonces \\(x = y\\), y \\(h = x\\) cumple las dos condiciones. Es la única: cualquier \\(h\\) que las cumpla es igual a \\(x\\).

(\\(\Leftarrow\\)) Si el cuadrado es producto fibrado y \\(m \circ x = m \circ y\\), existe \\(h\\) con \\(h = x\\) y \\(h = y\\); luego \\(x = y\\), y \\(m\\) es mono.

b) Sea \\(H\colon \mathcal{C} \to \mathcal{E}\\) un funtor que preserva productos fibrados y \\(m\\) un monomorfismo. Por a), el cuadrado de a) es producto fibrado. Al aplicar \\(H\\), y como \\(H(1\_A) = 1\_{HA}\\), se obtiene el cuadrado con lados \\(1\_{HA}\\), \\(1\_{HA}\\), \\(Hm\\), \\(Hm\\), que es producto fibrado porque \\(H\\) los preserva. Por a), aplicado ahora en \\(\mathcal{E}\\), \\(Hm\\) es mono.

c) Un producto fibrado es un límite (de forma coespán). Por el Teorema 9.2, un adjunto derecho preserva todos los límites que existen; en particular, el producto fibrado de a), que existe porque \\(m\\) es mono. Por b), un adjunto derecho preserva monomorfismos. Por ejemplo, el olvidadizo \\(U\colon \mathbf{Grp} \to \mathbf{Set}\\) envía monos en funciones inyectivas. \\(\blacksquare\\)

*Rúbrica específica:* a) vale 4 puntos (2 por cada dirección); b) vale 2 (1 por usar \\(H(1\_A) = 1\_{HA}\\) y 1 por aplicar a) en la categoría de llegada); c) vale 2 (1 por reconocer el producto fibrado como límite y 1 por citar el Teorema 9.2).

**Demostración 32.**

Se usa la regla de naturalidad de la Definición 8.1: \\(\overline{h \circ g \circ F(k)} = G(h) \circ \overline{g} \circ k\\) y, como la transposición es biyectiva en ambos sentidos, \\(\overline{G(h) \circ f \circ k} = h \circ \overline{f} \circ F(k)\\) para \\(f\colon X \to GY\\).

a) *Existencia.* Sean \\(f\colon X \to GA\\) y \\(g\colon X \to GB\\). Sus transpuestas son \\(\overline{f}\colon FX \to A\\) y \\(\overline{g}\colon FX \to B\\). Sea \\(h = \langle \overline{f}, \overline{g} \rangle\colon FX \to A \times B\\) y sea \\(\overline{h}\colon X \to G(A \times B)\\). Entonces

\\[
G(\pi\_1) \circ \overline{h} = \overline{\pi\_1 \circ h} = \overline{\overline{f}} = f, \qquad G(\pi\_2) \circ \overline{h} = \overline{\overline{g}} = g.
\\]

*Unicidad.* Si \\(k\colon X \to G(A \times B)\\) cumple \\(G(\pi\_1) \circ k = f\\) y \\(G(\pi\_2) \circ k = g\\), al transponer se obtiene \\(\pi\_1 \circ \overline{k} = \overline{f}\\) y \\(\pi\_2 \circ \overline{k} = \overline{g}\\). Por la unicidad en la propiedad universal de \\(A \times B\\), \\(\overline{k} = h\\), y al transponer de regreso, \\(k = \overline{h}\\). Luego \\((G(A \times B), G\pi\_1, G\pi\_2)\\) es un producto de \\(GA\\) y \\(GB\\).

b) Para todo \\(X\\) en \\(\mathcal{C}\\), \\(\mathcal{C}(X, G1) \cong \mathcal{D}(FX, 1)\\), y el lado derecho tiene exactamente un elemento porque \\(1\\) es terminal. Luego hay exactamente una flecha \\(X \to G1\\): \\(G1\\) es terminal.

c) Si \\(\mathcal{P}\\) tuviera adjunto izquierdo, sería adjunto derecho y, por b), \\(\mathcal{P}(\\{\star\\}) = \\{\emptyset, \\{\star\\}\\}\\) sería terminal en \\(\mathbf{Set}\\); pero tiene dos elementos. Si \\(\mathcal{P}\\) tuviera adjunto derecho, sería adjunto izquierdo y preservaría el objeto inicial; pero \\(\mathcal{P}(\emptyset) = \\{\emptyset\\}\\) no es vacío. Luego \\(\mathcal{P}\\) no tiene ningún adjunto. \\(\blacksquare\\)

*Rúbrica específica:* a) vale 4 puntos (2 por la existencia y 2 por la unicidad, que exige transponer de regreso); b) vale 2; c) vale 2 (1 por cada adjunto descartado, con el sentido correcto).

**Demostración 33.**

a) La componente en \\(X\\) de \\(\mu\\) es \\(\mu\_X = G(\varepsilon\_{FX})\colon GFGFX \to GFX\\). Por la segunda identidad triangular en \\(Y = FX\\),

\\[
\mu\_X \circ \eta\_{TX} = G(\varepsilon\_{FX}) \circ \eta\_{GFX} = 1\_{GFX}.
\\]

Por la primera identidad triangular y la funtorialidad de \\(G\\),

\\[
\mu\_X \circ T(\eta\_X) = G(\varepsilon\_{FX}) \circ GF(\eta\_X) = G\big(\varepsilon\_{FX} \circ F(\eta\_X)\big) = G(1\_{FX}) = 1\_{GFX}.
\\]

b) Hay que comparar \\(\mu\_X \circ T(\mu\_X) = G\big(\varepsilon\_{FX} \circ FG(\varepsilon\_{FX})\big)\\) y \\(\mu\_X \circ \mu\_{TX} = G\big(\varepsilon\_{FX} \circ \varepsilon\_{FGFX}\big)\\). La naturalidad de \\(\varepsilon\colon FG \Rightarrow 1\\) respecto de la flecha \\(\varepsilon\_{FX}\colon FGFX \to FX\\) dice

\\[
\varepsilon\_{FX} \circ FG(\varepsilon\_{FX}) = \varepsilon\_{FX} \circ \varepsilon\_{FGFX}.
\\]

Al aplicar \\(G\\) se obtiene la asociatividad.

c) Sea \\(a = G(\varepsilon\_Y)\colon TGY = GFGY \to GY\\). *Unidad:* \\(a \circ \eta\_{GY} = G(\varepsilon\_Y) \circ \eta\_{GY} = 1\_{GY}\\), por la segunda identidad triangular. *Asociatividad:* \\(a \circ T(a) = G\big(\varepsilon\_Y \circ FG(\varepsilon\_Y)\big)\\) y \\(a \circ \mu\_{GY} = G\big(\varepsilon\_Y \circ \varepsilon\_{FGY}\big)\\). Son iguales por la naturalidad de \\(\varepsilon\\) respecto de \\(\varepsilon\_Y\colon FGY \to Y\\).

d) Por la naturalidad de \\(\varepsilon\\) respecto de \\(h\\), \\(h \circ \varepsilon\_Y = \varepsilon\_{Y'} \circ FG(h)\\). Al aplicar \\(G\\):

\\[
G(h) \circ G(\varepsilon\_Y) = G(\varepsilon\_{Y'}) \circ GFG(h) = G(\varepsilon\_{Y'}) \circ T(G(h)),
\\]

que es la condición de morfismo de álgebras. Así, c) y d) definen el **funtor de comparación** \\(\mathcal{D} \to \mathcal{C}^T\\) de la Definición 11.6. \\(\blacksquare\\)

*Rúbrica específica:* a) vale 2 puntos (1 por cada ley, citando la identidad triangular correcta); b) vale 2; c) vale 3 (1 por la unidad y 2 por la asociatividad); d) vale 1.

**Demostración 34.**

a) La naturalidad de \\(c\_{-, A}\\) respecto de la flecha \\(c\colon A \otimes A \to A \otimes A\\) da

\\[
c\_{A \otimes A, A} \circ (c \otimes 1\_A) = (1\_A \otimes c) \circ c\_{A \otimes A, A}.
\\]

El segundo hexágono con los tres objetos iguales a \\(A\\) dice \\(c\_{A \otimes A, A} = (c \otimes 1\_A) \circ (1\_A \otimes c)\\). Al sustituir en los dos lados:

\\[
(c \otimes 1\_A) \circ (1\_A \otimes c) \circ (c \otimes 1\_A) = (1\_A \otimes c) \circ (c \otimes 1\_A) \circ (1\_A \otimes c),
\\]

que es \\(\rho(\sigma\_1) \rho(\sigma\_2) \rho(\sigma\_1) = \rho(\sigma\_2) \rho(\sigma\_1) \rho(\sigma\_2)\\).

b) Por la funtorialidad de \\(\otimes\\) (ley de intercambio), \\((f \otimes g) \circ (f' \otimes g') = (f \circ f') \otimes (g \circ g')\\). Con \\(f = c\\), \\(g = 1\_{A \otimes A}\\), \\(f' = 1\_{A \otimes A}\\), \\(g' = c\\):

\\[
(c \otimes 1\_{A \otimes A}) \circ (1\_{A \otimes A} \otimes c) = c \otimes c = (1\_{A \otimes A} \otimes c) \circ (c \otimes 1\_{A \otimes A}).
\\]

c) Cada \\(\rho(\sigma\_i)\\) es invertible, con inversa \\(1 \otimes c^{-1} \otimes 1\\), porque el trenzado es un isomorfismo natural y \\(\otimes\\) es un funtor. Así, \\(\rho\\) asigna a cada generador un elemento del grupo \\(\mathrm{Aut}(A^{\otimes 4})\\). La igualdad de a), tensorizada con \\(1\_A\\) a la derecha, da la relación de Artin para \\(\sigma\_1, \sigma\_2\\) en \\(A^{\otimes 4}\\); tensorizada con \\(1\_A\\) a la izquierda, da la de \\(\sigma\_2, \sigma\_3\\). Junto con b), que da la única relación de hebras lejanas en \\(B\_4\\), esos elementos cumplen todas las relaciones de Artin. Por la propiedad universal de un grupo presentado por generadores y relaciones (un coecualizador, Ejemplo 6.9), \\(\rho\\) se extiende de manera única a un homomorfismo \\(B\_4 \to \mathrm{Aut}(A^{\otimes 4})\\). Es el Corolario 13.6 para \\(n = 4\\).

d) Si \\(\mathcal{V}\\) es simétrica, \\(c\_{A,A} \circ c\_{A,A} = 1\_{A \otimes A}\\), y por la funtorialidad de \\(\otimes\\), \\(\rho(\sigma\_i)^2 = 1 \otimes (c \circ c) \otimes 1 = 1\\). Entonces \\(\rho\\) se anula en el subgrupo normal generado por los \\(\sigma\_i^2\\), y se factoriza por el cociente de \\(B\_4\\) que se obtiene al agregar las relaciones \\(\sigma\_i^2 = 1\\), que es el grupo simétrico \\(S\_4\\). Por eso, para obtener representaciones genuinas de los grupos de trenzas, hace falta un trenzado no simétrico, como una matriz R con \\(R^2 \ne 1\\) (Sección 3 del Capítulo 13). \\(\blacksquare\\)

*Rúbrica específica:* a) vale 3 puntos (1 por la naturalidad, 1 por el hexágono correcto, 1 por la sustitución); b) vale 2 (1 por la ley de intercambio y 1 por el cálculo); c) vale 1; d) vale 2 (1 por \\(\rho(\sigma\_i)^2 = 1\\) y 1 por la factorización por \\(S\_4\\) y su consecuencia).

</details>

---

## 📊 Diagnóstico y plan de repaso

### Tabla de diagnóstico

Anota tus puntos por Parte del libro y calcula tu porcentaje de dominio.

| Parte del libro | Reactivos | Puntos posibles | Mis puntos | Mi porcentaje |
| :--- | :--- | :---: | :---: | :---: |
| I. El lenguaje de las categorías | 1 a 4, 21 | 8 | | |
| II. Universalidad y representabilidad | 5 a 8, 22, 29, 30 | 24 | | |
| III. Límites y colímites | 9 a 12, 23, 24, 31 | 20 | | |
| IV. Adjunciones | 13 a 16, 25, 32 | 16 | | |
| V. Mónadas | 17, 18, 26, 27, 33 | 18 | | |
| VI. Hacia los nudos | 19, 20, 28, 34 | 14 | | |
| **Total** | | **100** | | |

Las Partes I a IV son el núcleo del libro y suman 68 puntos. La Parte I tiene pocos puntos propios porque su lenguaje (composición, funtores, naturalidad) se evalúa en todos los demás reactivos; si fallas en ella, el resto del examen también lo reflejará. La Parte II pesa más porque el lema de Yoneda y la unicidad de los objetos universales son las herramientas con las que se demuestran los resultados de las Partes III a V.

### Interpretación del resultado

| Puntaje total | Diagnóstico | Qué hacer |
| :---: | :--- | :--- |
| 85 a 100 | Dominio sólido | Repasa solo los reactivos fallados y resuelve algunos ejercicios de nivel 3 de cada Parte. Puedes dar por terminado el estudio del libro. |
| 70 a 84 | Dominio aceptable con huecos | Repasa las Partes con menos del 70 % y rehaz tus reactivos sin ver las soluciones. |
| 50 a 69 | Dominio insuficiente | Vuelve a las secciones señaladas abajo, resuelve los ejercicios clave del Apéndice A de esas Partes y repite el auto-examen en dos o tres semanas. |
| Menos de 50 | Se requiere repetir el plan de estudio | Recorre de nuevo el plan de 12 semanas del Apéndice A desde la Parte I, sin saltar los puntos de control. |

Más allá del total, **cualquier Parte por debajo del 60 %** merece atención prioritaria, aunque tu puntaje global sea bueno. Si la Parte II o la Parte IV quedan por debajo de ese umbral, conviene repasarlas antes que las demás: el Apéndice A señala Yoneda y adjunciones como las semanas que más cambian la forma de pensar.

### Mapa de repaso

| Si fallaste el reactivo… | Repasa la sección |
| :--- | :--- |
| 1 | [Capítulo 1, §4: Construcciones con categorías (categoría opuesta)](../parte1/01-categorias.md) |
| 2 | [Capítulo 1, §5: Flechas especiales (monomorfismos y epimorfismos)](../parte1/01-categorias.md) |
| 21 (funtores \\(L\\), \\(\mathcal{P}\\) y \\(\mathcal{P}^{-}\\)) | [Capítulo 2, §2 y §3: Catálogo de funtores y funtores contravariantes](../parte1/02-funtores.md) |
| 3, 21 | [Capítulo 3, §1 y §2: Transformaciones naturales y ejemplos](../parte1/03-transformaciones-naturales.md) |
| 4 | [Capítulo 3, §4: Equivalencia de categorías](../parte1/03-transformaciones-naturales.md) |
| 5, 29 | [Capítulo 4, §1, §4 y §5: Objetos iniciales y terminales; flechas universales; categoría coma](../parte2/04-propiedades-universales.md) |
| 6, 8 (coproducto) | [Capítulo 4, §2 y §3: Productos y coproductos](../parte2/04-propiedades-universales.md) |
| 7, 8, 22, 30 | [Capítulo 5: Funtores representables y el lema de Yoneda](../parte2/05-lema-de-yoneda.md) |
| 9, 10, 23, 24 (a, b) | [Capítulo 6, §1, §2 y §5: Diagramas, ecualizadores y colímites](../parte3/06-limites-y-colimites.md) |
| 23 (a), 24 (c), 31 (a) | [Capítulo 6, §3: Productos fibrados](../parte3/06-limites-y-colimites.md) |
| 11, 12, 24 (c) | [Capítulo 7, §1, §3 y §4: Existencia, creación de límites y límites en categorías de funtores](../parte3/07-existencia-preservacion-limites.md) |
| 13, 15 | [Capítulo 8, §2 B: Adjunciones entre órdenes y conexiones de Galois](../parte4/08-adjunciones.md) |
| 14, 25 | [Capítulo 8, §1 y §3: Definición de adjunción, unidad y counidad](../parte4/08-adjunciones.md) |
| 15, 25 (d), 31 (c), 32 | [Capítulo 9, §2: Los adjuntos derechos preservan límites](../parte4/09-adjunciones-limites.md) |
| 16 | [Capítulo 9, §4: Adjunciones, subcategorías reflexivas y equivalencias](../parte4/09-adjunciones-limites.md) |
| 18, 26 | [Capítulo 10, §1, §2 y §4: Mónadas, ejemplos y álgebras de Eilenberg–Moore](../parte5/10-monadas-y-algebras.md) |
| 33 | [Capítulo 10, §3 y §4: Toda adjunción produce una mónada; álgebras](../parte5/10-monadas-y-algebras.md) |
| 17, 27, 33 (d) | [Capítulo 11, §1 a §3: Kleisli, monadicidad y núcleos de Markov](../parte5/11-kleisli-probabilidad.md) |
| 19 | [Capítulo 12, §1 y §2: Categorías monoidales y monoides](../parte6/12-categorias-monoidales.md) |
| 20, 34 | [Capítulo 13, §1 a §3: Categorías trenzadas, trenzas y matrices R](../parte6/13-trenzadas-y-nudos.md) |
| 28 | [Capítulo 13, §4: Enredos, invariantes de nudos y el corchete de Kauffman](../parte6/13-trenzadas-y-nudos.md) |

Para practicar con problemas resueltos, consulta el [Apéndice E. Soluciones de los ejercicios de niveles 1 y 2](../apendices/e-soluciones.md). Los más cercanos a este examen son: la unicidad del producto ([Parte II, Ejercicio 2](../apendices/e-soluciones/parte2.md)); el lema de Yoneda covariante ([Parte II, Ejercicio 7](../apendices/e-soluciones/parte2.md)); los productos fibrados y monomorfismos ([Parte III, Ejercicio 6](../apendices/e-soluciones/parte3.md)); la adjunción del funtor diagonal y la no existencia de adjuntos ([Parte IV, Ejercicios 5 y 10](../apendices/e-soluciones/parte4.md)); la composición de Kleisli y las mónadas de acción ([Parte V, Ejercicios 3, 4 y 8](../apendices/e-soluciones/parte5.md)); y el corchete de Kauffman del enlace de Hopf y del trébol ([Parte VI, Ejercicios 9 y 10](../apendices/e-soluciones/parte6.md)). Para reorganizar tu repaso por semanas, vuelve al [Apéndice A. Plan de estudio de 12 semanas y puntos de control](../apendices/a-plan-de-estudio.md).
