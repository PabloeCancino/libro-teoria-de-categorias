import os
import sys

def main():
    codigo_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 70)
    print("🧪 SUITE DE CALIDAD MATEMÁTICA Y FORMATEO mdBook (Teoría de Categorías)")
    print("=" * 70)
    
    # 1. Limpieza de espacios redundantes \;
    print("\n[Paso 1/3] Limpieza de macros manuales redundantes (\\;)...")
    from clean_thick_spaces import clean_file
    import glob
    base_dir = os.path.dirname(codigo_dir)
    src_dir = os.path.join(base_dir, 'src')
    files = sorted(glob.glob(os.path.join(src_dir, '**', '*.md'), recursive=True) + glob.glob(os.path.join(src_dir, '*.md')))
    cleaned = sum(1 for f in files if clean_file(f))
    print(f" -> {cleaned} archivos sanitizados.")
    
    # 2. Formateo de expresiones y escape de subíndices
    print("\n[Paso 2/3] Formateo e idempotencia de ecuaciones y escape de subíndices (\\_)...")
    from format_math import process_file
    formatted = sum(1 for f in files if process_file(f))
    print(f" -> {formatted} archivos formateados.")
    
    # 3. Auditoría estricta de delimitadores
    print("\n[Paso 3/3] Auditoría estricta de delimitadores KaTeX/MathJax...")
    from check_delimiters import audit_file, audit_math_braces
    total_issues = 0
    for f in files:
        issues = audit_file(f)
        if issues:
            rel = os.path.relpath(f, base_dir)
            print(f"  ❌ {rel}: {len(issues)} delimitadores con diagonal simple.")
            total_issues += len(issues)
        bissues = audit_math_braces(f)
        if bissues:
            rel = os.path.relpath(f, base_dir)
            print(f"  ❌ {rel}: {len(bissues)} llaves con diagonal simple (deben ser \\\\{{ y \\\\}}).")
            total_issues += len(bissues)
            
    print("\n" + "=" * 70)
    if total_issues == 0:
        print("🎉 ESTADO: 100% CORRECTO. Todos los archivos están listos para publicación.")
        print("=" * 70)
        sys.exit(0)
    else:
        print(f"⚠️ ADVERTENCIA: Se detectaron {total_issues} problemas que requieren corrección.")
        print("=" * 70)
        sys.exit(1)

if __name__ == '__main__':
    main()
