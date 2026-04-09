from .llm_client import call_llm

def analyze_code(code, lang):
    prompt = f"""
You are a senior software engineer.

Think step by step:

1. Identify code smells
2. Identify SOLID violations
3. Identify readability issues
4. Identify naming issues

Return ONLY valid JSON in this format:
{{
  "issues": [],
  "improvements": []
}}

Code:
{code}
"""
    return call_llm(prompt)