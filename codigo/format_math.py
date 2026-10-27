import os
import glob
import re

def escape_math_braces(math_str):
    """
    Duplica la diagonal de las llaves \\{ y \\} (-> \\\\{ y \\\\}) dentro de fórmulas.
    En CommonMark, \\{ es un escape de Markdown: la diagonal se consume y MathJax recibe
    solo "{", por lo que las llaves de conjuntos desaparecen al renderizar
    ({1, 2} se mostraría como 1, 2). Con \\\\{ MathJax recibe \\{ y dibuja la llave.
    """
    return re.sub(r'(?<!\\)\\([{}])', r'\\\\\1', math_str)

def escape_math_underscores(math_str):
    """
    Escapa los guiones bajos que no estén ya precedidos por diagonal invertida
    y, además, las llaves (ver escape_math_braces).
    Esto previene que CommonMark interprete pares de subíndices (ej. x_1 y x_2, o _{...})
    como etiquetas HTML de cursiva <em>...</em> dentro de fórmulas KaTeX/MathJax.
    """
    math_str = re.sub(r'(?<!\\)_', r'\\_', math_str)
    return escape_math_braces(math_str)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Paso 1: Separar bloques de código (``` ... ```) para no alterar código de programación
    code_block_pattern = re.compile(r'(```.*?```)', re.DOTALL)
    parts = code_block_pattern.split(content)

    for idx in range(len(parts)):
        # Si es un bloque de código, se ignora
        if parts[idx].startswith('```'):
            continue

        text = parts[idx]
        trailing_newline = '\n' if text.endswith('\n') else ''

        # Paso 2: Escapar guiones bajos dentro de fórmulas en línea: \\( ... \\)
        def fix_inline(m):
            math_content = m.group(1)
            fixed = escape_math_underscores(math_content)
            return r'\\(' + fixed + r'\\)'

        text = re.sub(r'\\\\\((.*?)\\\\\)', fix_inline, text, flags=re.DOTALL)

        # Paso 3: Asegurar que todos los bloques display \\[ ... \\] (incluso en citas >)
        # tengan sus guiones bajos escapados y formato estándar
        lines = text.splitlines()
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]

            # Caso A: Display math en una sola línea: \\[ ... \\] o > \\[ ... \\]
            single_match = re.match(r'^(\s*(?:>\s*)?)\\+(\[)(.+?)\\+(\])\s*$', line)
            if single_match:
                prefix = single_match.group(1)
                math_body = single_match.group(3).strip()
                math_body = escape_math_underscores(math_body)

                new_lines.append(f'{prefix}\\\\[')
                new_lines.append(f'{prefix}{math_body}')
                new_lines.append(f'{prefix}\\\\]')
                i += 1
                continue

            # Caso B: Apertura de bloque display math multilínea: \\[ o > \\[
            open_match = re.match(r'^(\s*(?:>\s*)?)\\+(\[)\s*$', line)
            if open_match:
                prefix = open_match.group(1)
                new_lines.append(f'{prefix}\\\\[')
                i += 1
                while i < len(lines):
                    cur_line = lines[i]
                    close_match = re.match(r'^(\s*(?:>\s*)?)\\+(\])\s*$', cur_line)
                    if close_match:
                        new_lines.append(f'{prefix}\\\\]')
                        i += 1
                        break
                    else:
                        escaped_line = escape_math_underscores(cur_line)
                        new_lines.append(escaped_line)
                        i += 1
                continue

            new_lines.append(line)
            i += 1

        parts[idx] = '\n'.join(new_lines) + trailing_newline

    result = ''.join(parts)
    # Limpieza de saltos y citas consecutivas redundantes
    result = re.sub(r'(\n\s*>\s*){2,}\n', '\n>\n', result)
    result = re.sub(r'\n{3,}', '\n\n', result)

    if result != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return True
    return False

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(base_dir, 'src')
    files = sorted(glob.glob(os.path.join(src_dir, '**', '*.md'), recursive=True) + glob.glob(os.path.join(src_dir, '*.md')))
    modified = 0
    for f in files:
        if process_file(f):
            print(f'Modificado: {os.path.relpath(f, base_dir)}')
            modified += 1
    print(f'Total de archivos formateados: {modified}')
