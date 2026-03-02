import os, re
from collections import Counter

TARGET_DIR = r"e:\SWDEV\Spydra\spydra"
TERMS = [
    r"spydra",
    r"spydra",
    r"spydra",
    r"agentic\s+seek",
    r"spyder-solutions",
    r"Ahmed Arsalan",
    r"spydra"
]
pattern = re.compile("(?i)(" + "|".join(TERMS) + ")")

results = Counter()
ignore_dirs = {".git", "node_modules", "__pycache__", "build", "dist", ".venv", ".pytest_cache"} 

for root, dirs, files in os.walk(TARGET_DIR):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        if file.endswith((".py", ".js", ".md", ".txt", ".json", ".ini", ".yml", ".yaml", ".c", ".go", ".html", ".sh", ".bat", ".css")):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    for match in matches:
                        results[match] += 1
            except Exception:
                pass

for term, count in results.items():
    print(f"Branding term found: '{term}', Count: {count}")
