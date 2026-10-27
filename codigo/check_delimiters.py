import os
import sys
import glob

def audit_file(filepath):
    """
    Audita que los delimitadores de KaTeX/MathJax contengan exactamente dos diagonales
    invertidas (\\\\( y \\\\[) y no una sola (\\( o \\[).
    
    En CommonMark (mdBook), una diagonal simple '\\(' o '\\[' se interpreta como el
    escape de un paréntesis o corchete literal, destruyendo la fórmula matemática y
    mostrando texto plano como (P(x)) o [ (\\forall x) ... ].
    """
    with open(filepath, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    bad = []
    i = 0
    while i < len(content):
        if content[i] == '\\':
            # Verificar si es parte de una doble diagonal invertida '\\'
            if i + 1 < len(content) and content[i+1] == '\\':
                i += 2
                continue
            else:
                # Diagonal simple no escapada
                if i + 1 < len(content) and content[i+1] in '()[]':
                    bad.append((content[i+1], content[max(0, i-15):min(len(content), i+25)]))
                i += 1
        else:
            i += 1
    return bad

def audit_math_braces(filepath):
    """
    Detecta llaves con una sola diagonal (\\{ o \\}) dentro de fórmulas \\\\( ... \\\\) o
    \\\\[ ... \\\\]. CommonMark consume esa diagonal y las llaves desaparecen al renderizar;
    deben escribirse como \\\\{ y \\\\}. Se ignoran los bloques de código.
    """
    import re
    with open(filepath, 'r', encoding='utf-8') as fp:
        content = fp.read()
    bad = []
    brace = re.compile(r'(?<!\\)\\([{}])')
    for part in re.split(r'(```.*?```)', content, flags=re.DOTALL):
        if part.startswith('```'):
            continue
        for m in re.finditer(r'\\\\\(.*?\\\\\)|\\\\\[.*?\\\\\]', part, flags=re.DOTALL):
            for b in brace.finditer(m.group(0)):
                s = m.group(0)
                bad.append((b.group(1), s[max(0, b.start() - 15):min(len(s), b.end() + 25)]))
    return bad

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(base_dir, 'src')
    files = sorted(glob.glob(os.path.join(src_dir, '**', '*.md'), recursive=True) + glob.glob(os.path.join(src_dir, '*.md')))
    
    total_issues = 0
    brace_issues = 0
    for f in files:
        bissues = audit_math_braces(f)
        if bissues:
            rel = os.path.relpath(f, base_dir)
            print(f"=== {rel} === (llaves con una sola diagonal: {len(bissues)})")
            for b in bissues[:5]:
                print("  Snippet:", repr(b[1]))
            brace_issues += len(bissues)
        issues = audit_file(f)
        if issues:
            rel = os.path.relpath(f, base_dir)
            print(f"=== {rel} === (total {len(issues)} inconsistencias)")
            for b in issues[:5]:
                print("  Snippet:", repr(b[1]))
            total_issues += len(issues)
            
    total_issues += brace_issues
    if total_issues == 0:
        print("✅ Auditoría exitosa: Todos los delimitadores matemáticos están correctamente escapados (0 errores).")
        sys.exit(0)
    else:
        print(f"❌ Se encontraron {total_issues} problemas (delimitadores o llaves con diagonal simple).")
        sys.exit(1)
