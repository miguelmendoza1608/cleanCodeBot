from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content
    return clean_llm_output(content)    

def clean_llm_output(text: str) -> str:
    if "```" in text:
        text = text.split("```")
        if len(text) >= 2:
            return text[1].replace("javascript", "").replace("python", "").strip()
    return text.strip()
