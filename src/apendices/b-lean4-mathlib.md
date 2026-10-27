# Apéndice B. Formalización en Lean 4 con Mathlib

Este apéndice propone formalizaciones breves para verificar, al final de cada bloque, que lo estudiado se entendió. **No es un curso de Lean**: supone que el lector ya escribe demostraciones en Lean 4.

> **⚠️ Advertencia de verificación.** El código de este apéndice se escribió para la biblioteca de categorías de Mathlib, pero **no se compiló** durante la preparación del libro: el entorno de redacción no tenía acceso a Lean ni a la caché de Mathlib. Los nombres de Mathlib cambian con el tiempo. Antes de usar un fragmento, compílelo con su versión de Mathlib; si un nombre no existe, búsquelo con `#check`, `exact?` o en la [documentación en línea de Mathlib](https://leanprover-community.github.io/mathlib4_docs/) (`Mathlib.CategoryTheory`).

---

## 1. Convenciones de Mathlib que difieren del libro

| Libro | Mathlib | Observación |
| :--- | :--- | :--- |
| \\(f\colon A \to B\\) | `f : A ⟶ B` | Flecha larga para morfismos |
| \\(g \circ f\\) | `f ≫ g` | **Orden diagramático**: primero `f`, luego `g` |
| \\(1\_A\\) | `𝟙 A` | |
| \\(A \cong B\\) | `A ≅ B` | Estructura `Iso` con campos `hom`, `inv` |
| \\(F\colon \mathcal{C} \to \mathcal{D}\\) | `F : C ⥤ D` | `F.obj`, `F.map` |
| \\(\alpha\colon F \Rightarrow G\\) | `α : F ⟶ G` | Flecha en la categoría de funtores; `α.app X` |
| \\(F \dashv G\\) | `adj : F ⊣ G` | |

La diferencia más importante es el **orden diagramático** de `≫`. Toda ecuación del libro se invierte al traducirla.

---

## 2. Semana 4: unicidad del inverso y preservación de isomorfismos

```lean
import Mathlib

open CategoryTheory

universe v₁ v₂ u₁ u₂

variable {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]

-- Proposición 1.11: un inverso izquierdo y uno derecho coinciden.
-- En el libro: g ∘ f = 1 y f ∘ g' = 1. En orden diagramático: f ≫ g = 𝟙 X, g' ≫ f = 𝟙 Y.
example {X Y : C} (f : X ⟶ Y) (g g' : Y ⟶ X)
    (hg : f ≫ g = 𝟙 X) (hg' : g' ≫ f = 𝟙 Y) : g = g' := by
  calc g = 𝟙 Y ≫ g := (Category.id_comp g).symm
    _ = (g' ≫ f) ≫ g := by rw [hg']
    _ = g' ≫ (f ≫ g) := Category.assoc g' f g
    _ = g' ≫ 𝟙 X := by rw [hg]
    _ = g' := Category.comp_id g'

-- Proposición 2.2: los funtores preservan isomorfismos.
example (F : C ⥤ D) {X Y : C} (f : X ≅ Y) : F.obj X ≅ F.obj Y where
  hom := F.map f.hom
  inv := F.map f.inv
  hom_inv_id := by rw [← F.map_comp, f.hom_inv_id, F.map_id]
  inv_hom_id := by rw [← F.map_comp, f.inv_hom_id, F.map_id]
```

**Ejercicio.** Compare la prueba de la Proposición 1.11 con el bloque `calc`. ¿Qué paso del texto corresponde a cada línea? Mathlib ya contiene la segunda construcción con el nombre `Functor.mapIso`; localícela y compare.

---

## 3. Semana 8: el lema de Yoneda y la biyección de una adjunción

```lean
import Mathlib

open CategoryTheory Opposite

universe v₁ v₂ u₁ u₂

variable {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]

-- Teorema 5.4: Nat(C(-, X), F) ≃ F(X).
example (X : C) (F : Cᵒᵖ ⥤ Type v₁) : (yoneda.obj X ⟶ F) ≃ F.obj (op X) :=
  yonedaEquiv

-- Corolario 5.5: el encaje de Yoneda es pleno y fiel.
example : (yoneda : C ⥤ Cᵒᵖ ⥤ Type v₁).Full := inferInstance
example : (yoneda : C ⥤ Cᵒᵖ ⥤ Type v₁).Faithful := inferInstance

-- Definición 8.1: la biyección natural de una adjunción.
example {F : C ⥤ D} {G : D ⥤ C} (adj : F ⊣ G) (X : C) (Y : D) :
    (F.obj X ⟶ Y) ≃ (X ⟶ G.obj Y) :=
  adj.homEquiv X Y
```

**Ejercicio.** Busque el lema que describe `yonedaEquiv` aplicado a una transformación \\(\alpha\\) (en Mathlib se llama, en versiones recientes, `yonedaEquiv_apply`). Verifique que coincide con \\(\alpha \mapsto \alpha\_X(1\_X)\\) del Teorema 5.4, teniendo en cuenta el `op`.

**Ejercicio.** El Teorema 9.2 (los adjuntos derechos preservan límites) está en Mathlib, en los archivos de `CategoryTheory/Adjunction/Limits`. Localice el nombre vigente del resultado y escriba un `example` que lo use para concluir que el olvidadizo de grupos preserva límites.

---

## 4. Semana 12: la mónada de una adjunción

```lean
import Mathlib

open CategoryTheory

universe v₁ v₂ u₁ u₂

variable {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]

-- Teorema 10.8: toda adjunción produce una mónada.
example {F : C ⥤ D} {G : D ⥤ C} (adj : F ⊣ G) : Monad C :=
  adj.toMonad

-- Definición 10.10: las álgebras de Eilenberg–Moore.
example (T : Monad C) : Type _ := Monad.Algebra T
```

**Ejercicio.** Inspeccione con `#check` los campos de `Monad.Algebra` y compárelos con las dos ecuaciones de la Definición 10.10. ¿En qué orden aparecen las composiciones?

**Ejercicio (avanzado).** En Mathlib, las categorías trenzadas están en `CategoryTheory.Monoidal.Braided`. Busque el lema de la ecuación de Yang–Baxter y compare su prueba con la de la Proposición 13.2.

---

## 5. Qué esperar de la formalización

Formalizar teoría de categorías en Lean tiene una dificultad propia: las ecuaciones que en papel se resuelven "por naturalidad" se vuelven largas cadenas de reescritura, y las categorías opuestas obligan a manejar `op` y `unop` explícitamente. Por eso el libro recomienda formalizar **después** de entender, no como vía de entrada. La recompensa es la certeza: un cuadrado de naturalidad verificado en Lean no tiene huecos.
