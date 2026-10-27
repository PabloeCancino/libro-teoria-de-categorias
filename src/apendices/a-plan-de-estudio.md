# Apéndice A. Plan de estudio de 12 semanas y puntos de control

El plan supone **unas 5 horas por semana**: tres sesiones de 90 minutos y una de repaso breve. Con 3 horas semanales, el plan dura unas 20 semanas; con 8, caben 8 o 9. Lo que no conviene hacer es saltar los puntos de control.

---

## 🗓️ Cronograma

| Semana | Capítulo | Tema | Ejercicios clave | Producto semanal |
| :---: | :--- | :--- | :--- | :--- |
| 1 | 1 | Categorías y ejemplos; isomorfismos, monos y epis | Parte I: 1, 2, 3, 6 | Tabla de 6 categorías con objetos y flechas |
| 2 | 2–3 | Funtores; transformaciones naturales; equivalencias | Parte I: 4, 5, 8, 9, 13 | Una transformación natural no trivial, explicada |
| 3 | 4 | Propiedades universales | Parte II: 1, 2, 3, 5 | Producto y coproducto en tres categorías, comparados |
| 4 | 5 | Funtores representables y lema de Yoneda | Parte II: 4, 6, 7, 8 | Enunciado y prueba de Yoneda con palabras propias |
| 5 | 6 | Diagramas, límites y colímites | Parte III: 1–5 | Un límite y un colímite calculados explícitamente |
| 6 | 7 | Existencia y preservación de límites | Parte III: 6, 7, 8, 10 | Por qué el olvidadizo de grupos preserva límites |
| 7 | 8 | Adjunciones: definición y ejemplos | Parte IV: 1, 2, 3, 5 | Tres adjunciones conocidas reconocidas como tales |
| 8 | 9 | Adjunciones, límites y equivalencias | Parte IV: 4, 6, 9, 10 | Por qué los adjuntos izquierdos preservan colímites |
| 9 | 10 | Mónadas y sus álgebras | Parte V: 1, 2, 5, 6, 8 | Una mónada descrita como funtor, unidad y multiplicación |
| 10 | 11 | Kleisli, monadicidad y probabilidad | Parte V: 3, 4, 7, 9, 11 | Comparación de las álgebras de tres mónadas |
| 11 | 12 | Categorías monoidales | Parte VI: 1, 2, 5, 6, 7 | Qué es un monoide en una categoría monoidal |
| 12 | 13 y Epílogo | Trenzadas, trenzas y nudos; seudo-mónadas | Parte VI: 3, 4, 9, 12 | Un párrafo propio sobre categorías y nudos; ver la plática |

---

## ✅ Puntos de control

Al final de las semanas 4, 8 y 12, conviene hacer una prueba **sin libro**. Si se fallan dos de los tres puntos, se repite el bloque antes de avanzar.

### Semana 4: el lenguaje

- Definir categoría, funtor y transformación natural, con un ejemplo propio de cada uno.
- Enunciar y demostrar el lema de Yoneda.
- Explicar qué significa "propiedad universal" y por qué implica unicidad salvo isomorfismo único.

### Semana 8: la maquinaria

- Calcular un límite y un colímite concretos en una categoría distinta de \\(\mathbf{Set}\\).
- Reconocer una adjunción en un ejemplo no visto en el libro.
- Explicar por qué los adjuntos izquierdos preservan colímites.

### Semana 12: los destinos

- Dar la definición de mónada y tres ejemplos con sus álgebras.
- Definir categoría monoidal y monoide interno; explicar por qué una mónada es un monoide.
- Explicar con palabras propias por qué las trenzas satisfacen la ecuación de Yang–Baxter y qué relación tiene con el tercer movimiento de Reidemeister.

---

## ⚠️ Señales de alerta

- **Avanzar leyendo sin resolver ejercicios.** Es la señal más clara de que se está acumulando vocabulario sin destreza.
- **Dar solo ejemplos tomados del libro.** La regla de los tres ejemplos exige ejemplos propios.
- **Posponer la semana de Yoneda o la de adjunciones.** Son las dos que más cambian la forma de pensar. Si cuestan, se les dedica una semana extra en lugar de saltarlas.

---

## 🧪 Verificación en Lean 4

Una vez al final de cada bloque (semanas 4, 8 y 12) se formaliza un resultado pequeño con el [Apéndice B](b-lean4-mathlib.md). El orden sugerido: la unicidad del inverso y la preservación de isomorfismos (semana 4), el lema de Yoneda y la biyección de una adjunción (semana 8), la mónada de una adjunción (semana 12).
