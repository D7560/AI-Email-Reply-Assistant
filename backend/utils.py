import re

SIGNATURE_RE = re.compile(r"(Regards|Best|Thanks|Sincerely)[\s\S]*", re.IGNORECASE)

def preprocess_email(text: str) -> str:
    lines = [l for l in text.splitlines() if not l.strip().startswith(">")]
    cleaned = "\n".join(lines)
    cleaned = SIGNATURE_RE.split(cleaned)[0]
    cleaned = re.sub(r"\n{2,}", "\n\n", cleaned).strip()
    return cleaned
