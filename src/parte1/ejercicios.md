# Ejercicios de la Parte I

Los ejercicios están graduados. El nivel 1 verifica definiciones; el nivel 2 pide construir objetos o demostraciones; el nivel 3 conecta con otras áreas. Al final hay soluciones seleccionadas.

---

## 📝 Nivel 1. Verificación

1. Verifique que \\(\mathbf{Rel}\\) (Ejemplo 1.3) es una categoría: la composición de relaciones es asociativa y la diagonal es neutra.

2. Sea \\((P, \le)\\) un preorden visto como categoría. Demuestre que dos objetos \\(x, y\\) son isomorfos si y solo si \\(x \le y\\) y \\(y \le x\\). Concluya que en un orden parcial los únicos isomorfismos son las identidades.

3. Demuestre que en \\(\mathbf{Grp}\\) un homomorfismo es un monomorfismo si y solo si es inyectivo. *(Sugerencia: use el grupo \\(\mathbb{Z}\\) como objeto de prueba, en el papel que tuvo el conjunto con un elemento en la Proposición 1.13.)*

4. Verifique que la potencia contravariante \\(\mathcal{P}^{-}\\) (Ejemplo 2.11) cumple \\(\mathcal{P}^{-}(g \circ f) = \mathcal{P}^{-}(f) \circ \mathcal{P}^{-}(g)\\).

5. Sean \\(P, Q\\) órdenes parciales vistos como categorías y \\(f, g\colon P \to Q\\) funciones monótonas. Demuestre que existe a lo más una transformación natural \\(f \Rightarrow g\\), y que existe si y solo si \\(f(x) \le g(x)\\) para todo \\(x \in P\\).

---

## 📝 Nivel 2. Construcción

6. Demuestre que la composición de monomorfismos es un monomorfismo y que, si \\(g \circ f\\) es un monomorfismo, entonces \\(f\\) es un monomorfismo. Enuncie los resultados duales para epimorfismos sin demostrarlos de nuevo.

7. Encuentre en \\(\mathbf{Top}\\) un epimorfismo que no sea sobreyectivo, o demuestre que no existe. *(Sugerencia: use espacios con dos puntos y topologías distintas como objetos de prueba.)* Repita la pregunta en la subcategoría plena de espacios de Hausdorff, considerando la inclusión \\(\mathbb{Q} \to \mathbb{R}\\).

8. Demuestre que toda transformación natural \\(\alpha\colon 1\_{\mathbf{Set}} \Rightarrow 1\_{\mathbf{Set}}\\) es la identidad. *(Sugerencia: un elemento \\(x \in X\\) es una flecha \\(\\{\star\\} \to X\\).)*

9. Sea \\(G\\) un grupo. Demuestre que el conjunto de transformaciones naturales \\(1\_{\mathbf{B}G} \Rightarrow 1\_{\mathbf{B}G}\\) está en biyección con el centro de \\(G\\).

10. Demuestre que el subgrupo conmutador define un funtor \\(\mathbf{Grp} \to \mathbf{Grp}\\), \\(G \mapsto [G,G]\\), y que las inclusiones \\([G,G] \to G\\) forman una transformación natural.

---

## 📝 Nivel 3. Exploración

11. **Nudos y funtorialidad.** El grupo de un nudo es un invariante gracias a la Proposición 2.2. El número de cruces mínimo también es un invariante. ¿Puede presentarse este último como un funtor desde alguna categoría de nudos? Formule una categoría de nudos con flechas razonables y discuta qué invariantes son funtoriales en ella y cuáles no.

12. **Instrumentos y versiones.** Considere una categoría cuyos objetos son las versiones de un instrumento psicométrico y cuyas flechas \\(V \to V'\\) son correspondencias de reactivos que conservan el constructo medido. ¿Es una categoría? ¿Qué serían en ella los isomorfismos y los monomorfismos? ¿Qué condiciones habría que imponer para que la composición sea asociativa? El objetivo no es obtener un resultado, sino ensayar la traducción de una situación aplicada al lenguaje categórico y detectar dónde falla.

13. Demuestre que la categoría de conjuntos finitos y funciones es equivalente a la subcategoría plena cuyos objetos son los conjuntos \\(\\{1, \dots, n\\}\\), \\(n \in \mathbb{N}\\). ¿Son isomorfas?

---

## 💡 Soluciones seleccionadas

> **Solución al Ejercicio 3.**
> Si \\(f\colon G \to H\\) es inyectivo, cancela por la izquierda como en \\(\mathbf{Set}\\), porque dos homomorfismos son iguales si sus funciones subyacentes lo son. Recíprocamente, supongamos que \\(f\\) es monomorfismo y que \\(f(a) = f(a')\\). Los homomorfismos \\(g, h\colon \mathbb{Z} \to G\\) determinados por \\(g(1) = a\\) y \\(h(1) = a'\\) cumplen \\(f \circ g = f \circ h\\), porque coinciden en el generador. Luego \\(g = h\\) y \\(a = a'\\). El papel de \\(\mathbb{Z}\\) es el del conjunto con un elemento en \\(\mathbf{Set}\\): los homomorfismos \\(\mathbb{Z} \to G\\) corresponden a los elementos de \\(G\\). Esta correspondencia se llamará **representabilidad** en el Capítulo 5.

> **Solución al Ejercicio 8.**
> Sea \\(x \in X\\) y sea \\(\bar{x}\colon \\{\star\\} \to X\\) la función con valor \\(x\\). La naturalidad de \\(\alpha\\) en \\(\bar{x}\\) dice \\(\alpha\_X \circ \bar{x} = \bar{x} \circ \alpha\_{\\{\star\\}}\\). Pero \\(\alpha\_{\\{\star\\}}\\) es la única función de \\(\\{\star\\}\\) en sí mismo, es decir, la identidad. Entonces \\(\alpha\_X(x) = x\\) para todo \\(x\\). \\(\blacksquare\\)

> **Solución al Ejercicio 9.**
> Una transformación natural \\(\alpha\colon 1 \Rightarrow 1\\) en \\(\mathbf{B}G\\) tiene una sola componente \\(\alpha\_\star = z \in G\\). La naturalidad respecto de cada flecha \\(g\\) dice \\(g \circ z = z \circ g\\), es decir, \\(gz = zg\\). Luego las transformaciones naturales son exactamente los elementos del centro. Compare con el Ejemplo 2.15: el centro no es funtorial, pero sí aparece como un objeto natural asociado a cada grupo.

> **Guía para el Ejercicio 13.**
> La inclusión es plenamente fiel por ser subcategoría plena, y esencialmente sobreyectiva porque todo conjunto finito con \\(n\\) elementos está en biyección con \\(\\{1, \dots, n\\}\\). Por el Teorema 3.11 es una equivalencia. No son isomorfas: la categoría de todos los conjuntos finitos tiene muchos objetos distintos con dos elementos, mientras que la subcategoría tiene solo uno.
