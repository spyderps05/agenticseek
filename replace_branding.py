import os, re
import shutil

TARGET_DIR = r"e:\SWDEV\Spydra\spydra"
# Ordered from most specific/longest to shortest to avoid partial replacements
REPLACEMENTS = [
    (r"Spydra", "Spydra"),
    (r"spydra", "spydra"),
    (r"Spydra", "Spydra"),
    (r"spydra", "spydra"),
    (r"spydra", "spydra"),
    (r"spydra", "spydra"),
    (r"Spydra", "Spydra"),
    (r"spydra", "spydra"),
    (r"Spyder Solutions", "Spyder Solutions"),
    (r"spyder-solutions", "spyder-solutions"),
    (r"Ahmed Arsalan", "Ahmed Arsalan"),
    (r"Ahmed Arsalan", "Ahmed Arsalan"),
]

ignore_dirs = {".git", "node_modules", "__pycache__", "build", "dist", ".venv", ".pytest_cache"}

def replace_in_files():
    for root, dirs, files in os.walk(TARGET_DIR):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith((".py", ".js", ".md", ".txt", ".json", ".ini", ".yml", ".yaml", ".c", ".go", ".html", ".sh", ".bat", ".css")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    for old, new in REPLACEMENTS:
                        # Simple string replace works here because our list is ordered properly and covers all case variations
                        new_content = new_content.replace(old, new)
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                except Exception as e:
                    print(f"Failed to process {filepath}: {e}")

if __name__ == "__main__":
    replace_in_files()
    print("Find and replace completed in files.")
