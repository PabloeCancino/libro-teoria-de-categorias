# Teoría de Categorías desde Cero — De los objetos y las flechas a las mónadas y los nudos

[![Deploy mdBook](https://github.com/PabloeCancino/libro-teoria-de-categorias/actions/workflows/deploy.yml/badge.svg)](https://github.com/PabloeCancino/libro-teoria-de-categorias/actions/workflows/deploy.yml)
[![Libro Digital](https://img.shields.io/badge/Leer-Libro%20Digital%20Online-blue?style=for-the-badge&logo=gitbook)](https://pabloecancino.github.io/libro-teoria-de-categorias/)
[![Licencia CC BY-NC-ND 4.0](https://img.shields.io/badge/Licencia-CC%20BY--NC--ND%204.0-lightgrey?style=for-the-badge)](LICENSE.md)

**Autor:** Dr. Pablo Eduardo Cancino Marentes  
**Institución:** Universidad Autónoma de Nayarit (UAN), Unidad Académica de Ciencias Básicas e Ingenierías, Programa Académico de Licenciatura en Matemáticas (PALMAT).

---

## 📖 Acerca de este libro

Este repositorio contiene, en formato [mdBook](https://rust-lang.github.io/mdBook/), un texto de estudio autodidacta de **teoría de categorías** que parte de cero y llega hasta las mónadas, las categorías monoidales trenzadas y su aplicación a los invariantes de nudos. Nació como preparación para seguir la plática "Mónadas" del Dr. Francisco Marmolejo (Instituto de Matemáticas de la UNAM, octubre de 2026).

El hilo del libro es que cada concepto categórico **cristaliza conceptos preliminares** que el lector ya conoce de álgebra, topología y lógica. Está organizado en seis partes y cuatro apéndices:

1. **El lenguaje de las categorías:** categorías, funtores, transformaciones naturales y equivalencias.
2. **Universalidad y representabilidad:** propiedades universales, funtores representables y el lema de Yoneda.
3. **Límites y colímites:** productos, ecualizadores, productos fibrados, cocientes, pegados; existencia y preservación.
4. **Adjunciones:** libre y olvidadizo, cuantificadores como adjuntos, unidad y counidad; los adjuntos derechos preservan límites.
5. **Mónadas:** álgebras de Eilenberg–Moore, categoría de Kleisli, monadicidad y mónadas de probabilidad.
6. **Hacia los nudos:** categorías monoidales, diagramas de cuerdas, categorías trenzadas, trenzas, enredos, el corchete de Kauffman y un epílogo sobre seudo-mónadas.
7. **Apéndices:** plan de estudio de 12 semanas con puntos de control, formalizaciones en Lean 4 con Mathlib, glosario español–inglés, bibliografía comentada y soluciones completas de los ejercicios de niveles 1 y 2.

Cada parte cierra con ejercicios graduados en tres niveles (verificación, construcción y exploración) y soluciones seleccionadas. El Apéndice E reúne las soluciones completas de todos los ejercicios de niveles 1 y 2.

---

## 🌐 Lectura en línea

👉 **[https://pabloecancino.github.io/libro-teoria-de-categorias/](https://pabloecancino.github.io/libro-teoria-de-categorias/)**

---

## 🛠️ Compilación local

```bash
# 1. Instalar mdBook (requiere Rust/Cargo)
cargo install mdbook

# 2. Clonar el repositorio
git clone https://github.com/PabloeCancino/libro-teoria-de-categorias.git
cd libro-teoria-de-categorias

# 3. Servir localmente con recarga en vivo
mdbook serve --open
```

Antes de publicar cambios, conviene ejecutar la suite de calidad matemática:

```bash
python codigo/run_all_math_linters.py
```

---

## ✍️ Convenciones de escritura matemática

Las fórmulas se escriben para MathJax dentro de Markdown, con las mismas reglas que los demás libros del autor:

- En línea: `\\( ... \\)`; en bloque: `\\[ ... \\]` en líneas propias.
- Llaves de conjuntos: `\\{` y `\\}`.
- Saltos de línea dentro de una fórmula (matrices, diagramas): `\\\\`.
- Macros cuyo nombre es un signo de puntuación (espacio fino `\,`, etc.): con doble diagonal, `\\,`. Con una sola diagonal, Markdown la consume.
- Diagramas conmutativos cuadrados: entorno `CD` de MathJax, cargado con `\require{AMScd}`.

---

## 📄 Licencia y cita

Publicado bajo la licencia **[Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)](LICENSE.md)**.

**Cómo citar:**
> Cancino Marentes, P. E. (2026). *Teoría de Categorías desde Cero: De los objetos y las flechas a las mónadas y los nudos*. Universidad Autónoma de Nayarit. Publicación abierta en: https://pabloecancino.github.io/libro-teoria-de-categorias/
