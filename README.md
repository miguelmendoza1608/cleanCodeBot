# Clean Code Bot

CLI tool that analyzes, refactors, and documents code using an LLM (Groq).

## 🚀 How it works

The tool uses a multi-step LLM pipeline:

1. **Analysis**  
   Detects code smells, SOLID violations, and readability issues.

2. **Refactoring**  
   Improves code structure, naming, and applies clean code principles.

3. **Documentation**  
   Adds JSDoc (JavaScript) or docstrings (Python).

---

## ⚙️ Setup

### Recommended (using virtual environment)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
----

## Set API Key
export GROQ_API_KEY=your_api_key
## Usage
python cli.py examples/js/before.js
