from .llm_client import call_llm

def generate_docs(code, lang):
    prompt = f"""
You are a senior developer.

Add clear and professional documentation to this {lang} code.

Include:
- Function descriptions
- Parameters
- Return values

Return only the final code.

Code:
{code}
"""
    return call_llm(prompt)