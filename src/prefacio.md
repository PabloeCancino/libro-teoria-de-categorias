# Prefacio

Este libro nace de una pregunta concreta. En octubre de 2026, el Dr. Francisco Marmolejo dictó en el Instituto de Matemáticas de la UNAM una plática sobre **mónadas**: una idea algebraica que surgió a mediados del siglo XX y que hoy tiene versiones en categorías de dimensión superior, las **seudo-mónadas**. Para seguir esa plática con provecho hace falta un lenguaje previo, y ese lenguaje es la teoría de categorías. Este texto es el camino que lleva desde cero hasta poder escucharla con oído matemático.

---

## 🎯 Propósito: cristalizar lo que ya se sabe

La teoría de categorías no agrega, en primera instancia, objetos matemáticos nuevos. Su aporte es otro: **muestra que muchas construcciones que el lector ya conoce son casos de unas pocas ideas**. El producto cartesiano de conjuntos, el producto directo de grupos, la topología producto y el máximo común divisor resultan ser la misma construcción. El grupo libre, el espacio vectorial con base dada y el anillo de polinomios son tres apariciones de un mismo fenómeno. El cociente de un grupo por un subgrupo normal, la topología cociente y el conjunto cociente por una relación de equivalencia también se dejan describir con una sola frase.

Por eso el libro adopta una regla de trabajo: **cada concepto nuevo se presenta como la cristalización de conceptos preliminares**. Antes de cada definición se recuerda dónde la ha visto ya el lector, aunque no la haya visto con ese nombre. Después se dice qué cambia al nombrarla.

---

## 🧭 Flujo narrativo

El libro avanza por seis partes. Cada una responde una pregunta que la anterior deja abierta.

1. **Parte I. El lenguaje de las categorías.** ¿Qué tienen en común los grupos, los espacios topológicos y los órdenes parciales? Respuesta: objetos, flechas y composición. Luego, las flechas entre categorías (funtores) y las flechas entre funtores (transformaciones naturales).
2. **Parte II. Universalidad y representabilidad.** ¿Cómo se describe un objeto sin mirar sus elementos? Por su relación con todos los demás. Aquí aparecen las propiedades universales y el **lema de Yoneda**, el resultado que más cambia la forma de pensar.
3. **Parte III. Límites y colímites.** ¿Qué tienen en común el producto, el núcleo, la intersección y la imagen inversa? Son límites. El dual reúne coproductos, cocientes y pegados.
4. **Parte IV. Adjunciones.** ¿Por qué lo "libre" y lo "olvidadizo" aparecen siempre en pareja? Porque forman adjunciones, el concepto más ubicuo de toda la teoría.
5. **Parte V. Mónadas.** ¿Qué queda de una adjunción si solo se mira una de las dos categorías? Una mónada. Aquí se llega al tema de la plática que motivó el libro.
6. **Parte VI. Hacia los nudos.** ¿Dónde viven los invariantes de nudos? En las categorías monoidales trenzadas. El libro cierra con un vistazo a las seudo-mónadas y a la matemática de dimensión superior.

---

## 🧠 Enfoque pedagógico

El texto combina tres componentes:

- **Rigor conceptual.** Definiciones precisas y demostraciones completas de los resultados centrales. Cuando una prueba excede el alcance del libro, se enuncia el resultado y se indica dónde estudiarla.
- **Metacognición.** Cada capítulo incluye recuadros **"Para pensar"**, que piden al lector detenerse a examinar su propio proceso: qué está suponiendo, qué ejemplo usaría, qué falla si se quita una hipótesis.
- **Práctica graduada.** Cada parte cierra con ejercicios en tres niveles: verificación, construcción y exploración. Se incluyen soluciones seleccionadas.

---

## 🔗 Destinos de aplicación

El lector previsto trabaja en teoría de nudos y en estadística aplicada al comportamiento humano. El libro es honesto sobre ambas conexiones. El vínculo con los nudos es **directo y maduro**: los invariantes cuánticos de nudos son funtores entre categorías monoidales trenzadas, y la Parte VI lo explica. El vínculo con la estadística es **real pero todavía de investigación**: las mónadas de probabilidad y las categorías de Markov ofrecen un lenguaje para los modelos probabilísticos, y el Capítulo 11 lo presenta, sin prometer que ese lenguaje mejore hoy un análisis psicométrico.

---

## 🙏 Agradecimientos

A la tradición de textos abiertos que hizo posible este trabajo, en especial los libros de Tom Leinster, [*Basic Category Theory*](https://arxiv.org/abs/1612.09375), y de Emily Riehl, [*Category Theory in Context*](https://math.jhu.edu/~eriehl/context), ambos con versión libre en línea. Este texto sigue en buena medida el orden de exposición de Riehl. Las deudas específicas se señalan en la [bibliografía comentada](apendices/d-bibliografia.md).
