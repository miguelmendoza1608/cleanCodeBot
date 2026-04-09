from .sanitizer import sanitize_input
from .analyzer import analyze_code
from .refactorer import refactor_code
from .documenter import generate_docs

def detect_language(code):
    if "function" in code:
        return "javascript"
    if "def " in code:
        return "python"
    return "unknown"

def process_code(code, lang=None):
    clean_code = sanitize_input(code)

    language = lang or detect_language(clean_code)

    analysis = analyze_code(clean_code, language)
    refactored = refactor_code(clean_code, analysis, language)
    documented = generate_docs(refactored, language)

    return documented