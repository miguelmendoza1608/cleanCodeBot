def sanitize_input(code: str) -> str:
    forbidden_patterns = [
        "ignore previous instructions",
        "system:",
        "assistant:",
        "<script>",
    ]

    for pattern in forbidden_patterns:
        if pattern.lower() in code.lower():
            raise ValueError("Potential prompt injection detected")

    if len(code) > 10000:
        raise ValueError("Input too large")

    return code