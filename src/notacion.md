# Notación y convenciones

Este resumen reúne los símbolos que se usan a lo largo del libro. Cada uno se define con precisión en el capítulo indicado.

---

### Categorías, objetos y flechas (Capítulo 1)

| Símbolo | Significado | Lectura |
| :--- | :--- | :--- |
| \\(\mathcal{C}, \mathcal{D}, \mathcal{E}\\) | Categorías arbitrarias | "la categoría C" |
| \\(\mathrm{Ob}(\mathcal{C})\\) | Clase de objetos de \\(\mathcal{C}\\) | "objetos de C" |
| \\(f\colon A \to B\\) | Flecha (morfismo) de dominio \\(A\\) y codominio \\(B\\) | "f va de A a B" |
| \\(\mathcal{C}(A,B)\\) o \\(\mathrm{Hom}\_{\mathcal{C}}(A,B)\\) | Conjunto de flechas de \\(A\\) a \\(B\\) | "hom de A en B" |
| \\(g \circ f\\) o \\(gf\\) | Composición: primero \\(f\\), después \\(g\\) | "g después de f" |
| \\(1\_A\\) o \\(\mathrm{id}\_A\\) | Identidad del objeto \\(A\\) | "identidad de A" |
| \\(A \cong B\\) | \\(A\\) y \\(B\\) son isomorfos | "A es isomorfo a B" |
| \\(\mathcal{C}^{\mathrm{op}}\\) | Categoría opuesta (flechas invertidas) | "C opuesta" |
| \\(\mathcal{C} \times \mathcal{D}\\) | Categoría producto | "C por D" |
| \\(\mathcal{C}/X\\) | Categoría de objetos sobre \\(X\\) (rebanada) | "C sobre X" |

---

### Categorías con nombre propio

| Símbolo | Objetos | Flechas |
| :--- | :--- | :--- |
| \\(\mathbf{Set}\\) | Conjuntos | Funciones |
| \\(\mathbf{Grp}\\) | Grupos | Homomorfismos de grupos |
| \\(\mathbf{Ab}\\) | Grupos abelianos | Homomorfismos |
| \\(\mathbf{Mon}\\) | Monoides | Homomorfismos de monoides |
| \\(\mathbf{Ring}\\) | Anillos con unidad | Homomorfismos que preservan la unidad |
| \\(\mathbf{Vect}\_k\\) | Espacios vectoriales sobre el campo \\(k\\) | Transformaciones lineales |
| \\(\mathbf{Top}\\) | Espacios topológicos | Funciones continuas |
| \\(\mathbf{Pos}\\) | Conjuntos parcialmente ordenados | Funciones monótonas |
| \\(\mathbf{Rel}\\) | Conjuntos | Relaciones binarias |
| \\(\mathbf{Cat}\\) | Categorías pequeñas | Funtores |
| \\(\mathbf{Mat}\_k\\) | Números naturales | Matrices con entradas en \\(k\\) |

---

### Funtores y transformaciones naturales (Capítulos 2 y 3)

| Símbolo | Significado | Lectura |
| :--- | :--- | :--- |
| \\(F\colon \mathcal{C} \to \mathcal{D}\\) | Funtor de \\(\mathcal{C}\\) en \\(\mathcal{D}\\) | "F de C en D" |
| \\(U\\) | Funtor olvidadizo (del inglés *underlying*) | "el olvidadizo" |
| \\(\alpha\colon F \Rightarrow G\\) | Transformación natural de \\(F\\) en \\(G\\) | "alfa de F en G" |
| \\(\alpha\_A\\) | Componente de \\(\alpha\\) en el objeto \\(A\\) | "alfa en A" |
| \\([\mathcal{C},\mathcal{D}]\\) o \\(\mathcal{D}^{\mathcal{C}}\\) | Categoría de funtores de \\(\mathcal{C}\\) en \\(\mathcal{D}\\) | "funtores de C en D" |
| \\(\mathcal{C} \simeq \mathcal{D}\\) | Equivalencia de categorías | "C es equivalente a D" |
| \\(\widehat{\mathcal{C}}\\) | Prehaces: \\([\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]\\) | "prehaces sobre C" |

---

### Universalidad, límites y adjunciones (Capítulos 4 a 9)

| Símbolo | Significado | Lectura |
| :--- | :--- | :--- |
| \\(0\\), \\(1\\) | Objeto inicial, objeto terminal | "inicial", "terminal" |
| \\(A \times B\\), \\(A + B\\) | Producto y coproducto | "producto", "coproducto" |
| \\(\pi\_1, \pi\_2\\); \\(\iota\_1, \iota\_2\\) | Proyecciones; inclusiones | "proyecciones", "inclusiones" |
| \\(\langle f, g \rangle\\); \\([f, g]\\) | Flecha inducida al producto; desde el coproducto | "par f, g"; "copar f, g" |
| \\(\mathcal{C}(-,A)\\), \\(\mathcal{C}(A,-)\\) | Funtores hom (representables) | "hom hacia A", "hom desde A" |
| \\(y\colon \mathcal{C} \to \widehat{\mathcal{C}}\\) | Encaje de Yoneda | "encaje de Yoneda" |
| \\(\lim D\\), \\(\mathrm{colim}\\, D\\) | Límite y colímite del diagrama \\(D\\) | "límite de D", "colímite de D" |
| \\(F \dashv G\\) | \\(F\\) es adjunto izquierdo de \\(G\\) | "F adjunto izquierdo de G" |
| \\(\eta\colon 1 \Rightarrow GF\\) | Unidad de la adjunción | "unidad" |
| \\(\varepsilon\colon FG \Rightarrow 1\\) | Counidad de la adjunción | "counidad" |

---

### Mónadas y estructura monoidal (Capítulos 10 a 13)

| Símbolo | Significado | Lectura |
| :--- | :--- | :--- |
| \\((T, \eta, \mu)\\) | Mónada: endofuntor, unidad y multiplicación | "la mónada T" |
| \\(\mathcal{C}^T\\) | Categoría de Eilenberg–Moore (álgebras de \\(T\\)) | "T-álgebras" |
| \\(\mathcal{C}\_T\\) | Categoría de Kleisli de \\(T\\) | "Kleisli de T" |
| \\(\mathcal{P}\\), \\(L\\), \\(\mathcal{D}\\) | Mónadas de conjunto potencia, de listas y de distribuciones finitas | "potencia", "listas", "distribuciones" |
| \\((\mathcal{V}, \otimes, I)\\) | Categoría monoidal: producto tensorial y unidad | "V con tensor" |
| \\(\alpha, \lambda, \rho\\) | Asociador, unitor izquierdo, unitor derecho | "asociador", "unitores" |
| \\(c\_{A,B}\colon A \otimes B \to B \otimes A\\) | Trenzado | "trenzado de A y B" |
| \\(B\_n\\) | Grupo de trenzas con \\(n\\) hebras | "trenzas de n hebras" |
| \\(\sigma\_i\\) | Generador de Artin: cruce de las hebras \\(i\\) e \\(i+1\\) | "sigma i" |

---

### Convenciones

- **Composición de derecha a izquierda.** \\(g \circ f\\) significa "primero \\(f\\), luego \\(g\\)", como en la composición de funciones.
- **Tamaño.** Se ignoran las sutilezas conjuntistas salvo cuando importan. Una categoría es **pequeña** si sus objetos y flechas forman conjuntos, y **localmente pequeña** si cada \\(\mathcal{C}(A,B)\\) es un conjunto. Todas las categorías del libro son localmente pequeñas.
- **"Salvo isomorfismo único."** Frase que se repite desde el Capítulo 4: significa que dos soluciones a un mismo problema universal están conectadas por exactamente un isomorfismo compatible con la estructura.
- **Naturales.** \\(\mathbb{N} = \\{0, 1, 2, \dots\\}\\) incluye el cero, como es usual en teoría de categorías.
