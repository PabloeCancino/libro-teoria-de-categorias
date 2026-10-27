# Ejercicios de la Parte III

> **Soluciones completas.** Las soluciones de todos los ejercicios de niveles 1 y 2 de esta parte están en el [Apéndice E, Parte III](../apendices/e-soluciones/parte3.md). Las de abajo son solo una selección.


---

## 📝 Nivel 1. Verificación

1. Calcule en \\(\mathbf{Set}\\) el ecualizador de \\(f, g\colon \mathbb{R} \to \mathbb{R}\\), \\(f(x) = x^2\\), \\(g(x) = x + 2\\). ¿Qué es, en esta lengua, "resolver una ecuación"?

2. Verifique que el núcleo de una transformación lineal \\(T\colon V \to W\\) es el ecualizador de \\(T\\) y de la transformación cero, y que el conúcleo \\(W/\mathrm{im}\\, T\\) es su coecualizador.

3. Sea \\(f\colon X \to Y\\) una función y \\(y \in Y\\). Escriba la fibra \\(f^{-1}(y)\\) como un producto fibrado y dibuje el cuadrado.

4. Demuestre que en un orden parcial visto como categoría, el producto fibrado de \\(a \le c\\) y \\(b \le c\\) es \\(a \wedge b\\), si existe. ¿Qué papel tiene \\(c\\)?

5. Describa el coecualizador en \\(\mathbf{Top}\\) que produce el círculo \\(S^1\\) a partir del intervalo \\([0,1]\\).

---

## 📝 Nivel 2. Construcción

6. Demuestre que el producto fibrado de un monomorfismo es un monomorfismo: si \\(g\colon B \to C\\) es mono y \\(P = A \times\_C B\\), entonces \\(p\_1\colon P \to A\\) es mono.

7. **Lema del pegado de productos fibrados.** Considere dos cuadrados conmutativos adyacentes. Demuestre que si el cuadrado derecho es un producto fibrado, entonces el cuadrado izquierdo es producto fibrado si y solo si el rectángulo exterior lo es.

8. Demuestre que una categoría con objeto terminal y productos fibrados tiene productos binarios y ecualizadores, y por lo tanto todos los límites finitos.

9. Demuestre que \\(\mathbb{Z}\_p\\) es un dominio entero. *(Sugerencia: use la descripción como sucesiones compatibles.)* ¿Qué propiedad del límite usó, y qué propiedad de cada \\(\mathbb{Z}/p^n\\)?

10. Demuestre que \\(\mathbf{Grp}(\mathrm{colim}\\, D, H) \cong \lim\_j \mathbf{Grp}(D(j), H)\\) y úselo para describir los homomorfismos que salen de un producto libre amalgamado.

---

## 📝 Nivel 3. Exploración

11. **El grupo de un enlace como colímite.** Use Seifert–van Kampen para escribir el grupo del complemento de dos círculos no enlazados como un producto libre. Luego haga lo mismo con el enlace de Hopf y compare. ¿Qué diagrama de espacios produce cada grupo?

12. **Límites inversos en datos longitudinales.** Una base de datos con agregación (estudiante, grupo, programa, unidad académica) define una cadena de proyecciones entre niveles de detalle. Formule el conjunto de "registros consistentes en todos los niveles" como un límite. ¿Qué sucede con ese límite si un nivel contiene un registro huérfano, sin correspondencia en el nivel superior?

13. Investigue qué significa que un funtor sea **continuo** (que preserve límites pequeños) y por qué el teorema del funtor adjunto, que se verá en el Capítulo 9, exige además una condición de tamaño.

---

## 💡 Soluciones seleccionadas

> **Solución al Ejercicio 6.**
> Sean \\(x, y\colon X \to P\\) con \\(p\_1 x = p\_1 y\\). Entonces \\(g p\_2 x = f p\_1 x = f p\_1 y = g p\_2 y\\), y como \\(g\\) es mono, \\(p\_2 x = p\_2 y\\). Así, \\(x\\) e \\(y\\) son dos factorizaciones del mismo cono \\((X, p\_1 x, p\_2 x)\\) a través del producto fibrado. Por la unicidad de la propiedad universal, \\(x = y\\). \\(\blacksquare\\)

> **Solución al Ejercicio 8.**
> El producto \\(A \times B\\) es el producto fibrado de \\(A \to 1\\) y \\(B \to 1\\): un cuadrado sobre \\(1\\) no impone ninguna condición, porque hay una sola flecha hacia \\(1\\). Para el ecualizador de \\(f, g\colon A \rightrightarrows B\\), se toma el producto fibrado de \\(\langle 1\_A, f \rangle\colon A \to A \times B\\) y \\(\langle 1\_A, g \rangle\colon A \to A \times B\\). Un elemento generalizado del producto fibrado es un par \\((x, x')\\) con \\(x = x'\\) y \\(f x = g x'\\), es decir, un \\(x\\) con \\(f x = g x\\). Se verifica la propiedad universal con la misma idea. Por el Teorema 7.2, en su versión finita, se obtienen todos los límites finitos. \\(\blacksquare\\)

> **Guía para el Ejercicio 11.**
> Para dos círculos no enlazados, el complemento se descompone en dos abiertos, cada uno con un solo círculo, cuya intersección es simplemente conexa. Se obtiene \\(\mathbb{Z} \ast \mathbb{Z}\\). Para el enlace de Hopf, el complemento en \\(S^3\\) se retrae a un toro y el grupo es \\(\mathbb{Z} \times \mathbb{Z}\\); en \\(\mathbb{R}^3\\) el complemento es homotópico a \\(T^2 \vee S^2\\), con el mismo grupo fundamental. Que los grupos difieran (uno abeliano, el otro no) **demuestra que el enlace de Hopf está enlazado**. El primer cálculo usa un colímite; el segundo, una retracción.
