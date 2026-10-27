import os
import glob
import re

# Barra invertida (se construye con chr para evitar secuencias de escape ambiguas)
BS = chr(92)
THICK = BS + ';'   # la macro de espacio grueso de LaTeX: barra invertida + punto y coma

# Segmentos de fórmula en línea (doble barra + paréntesis) o en bloque (doble barra + corchete)
_MATH = re.compile(
    re.escape(BS * 2 + '(') + '.*?' + re.escape(BS * 2 + ')') + '|' +
    re.escape(BS * 2 + '[') + '.*?' + re.escape(BS * 2 + ']'),
    re.DOTALL,
)
_THICK_WITH_SPACES = re.compile(' *' + re.escape(THICK) + ' *')


def clean_text(content):
    """
    Elimina las macros manuales de espacio grueso de LaTeX (barra invertida + punto
    y coma) que generan artefactos de punto y coma literales (ej. '∅;⊆;A;⊆;U')
    cuando se desescapan en el analizador Markdown.

    En TeX/KaTeX/MathJax, los operadores de relación binaria (=, subseteq, equiv,
    iff, implies) ya incluyen espaciado óptico automático (thickmuskip).

    IMPORTANTE: solo actúa DENTRO de las fórmulas y solo sobre cada macro (con los
    espacios que la rodean). No colapsa espacios en el resto del texto: la sangría
    de listas anidadas, los saltos de línea duros de Markdown y la sangría del
    SVG dependen de espacios múltiples y no deben tocarse.
    """
    def fix(m):
        seg = m.group(0)
        if THICK not in seg:
            return seg
        return _THICK_WITH_SPACES.sub(' ', seg)

    parts = re.split(r'(```.*?```)', content, flags=re.DOTALL)
    for i, p in enumerate(parts):
        if p.startswith('```'):
            continue
        parts[i] = _MATH.sub(fix, p)
    return ''.join(parts)


def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', newline='') as fp:
        content = fp.read()

    cleaned = clean_text(content)

    if cleaned != content:
        with open(filepath, 'w', encoding='utf-8', newline='') as fp:
            fp.write(cleaned)
        return True
    return False

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(base_dir, 'src')
    files = sorted(glob.glob(os.path.join(src_dir, '**', '*.md'), recursive=True) + glob.glob(os.path.join(src_dir, '*.md')))
    count = 0
    for f in files:
        if clean_file(f):
            rel = os.path.relpath(f, base_dir)
            print("Limpieza de macros de espacio grueso en: " + rel)
            count += 1
    print("Total de archivos procesados: " + str(count))
