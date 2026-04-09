from .llm_client import call_llm

def refactor_code(code, analysis, lang):
    prompt = f"""
You are a senior software engineer.

Refactor the following {lang} code using SOLID principles.

Rules:
- Improve naming
- Improve structure
- Do NOT change functionality

Analysis:
{analysis}

Code:
{code}
"""
    return call_llm(prompt)