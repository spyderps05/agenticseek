import os, re
import shutil

TARGET_DIR = r"e:\SWDEV\GIMUseek\agenticseek"
REPLACEMENTS = [
    (r"AgenticSeek", "Spydra"),
    (r"agenticSeek", "spydra"),
    (r"Agentic Seek", "Spydra"),
    (r"agentic-seek", "spydra"),
    (r"agentic_seek", "spydra"),
    (r"agenticseek", "spydra"),
    (r"GIMUseek", "Spydra"),
    (r"gimuseek", "spydra"),
    (r"Fosowl", "Spyder Solutions"),
    (r"fosowl", "spyder-solutions"),
    (r"Martin993886460", "Ahmed Arsalan"),
    (r"martin993886460", "Ahmed Arsalan"),
]

ignore_dirs = {".git", "node_modules", "__pycache__", "build", "dist", ".venv", ".pytest_cache"}
ignore_extensions = {".png", ".jpg", ".jpeg", ".ico", ".svg", ".lock"}

def replace_in_files():
    for root, dirs, files in os.walk(TARGET_DIR):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            # Check ignored extensions
            if any(file.endswith(ext) for ext in ignore_extensions):
                continue
            
            filepath = os.path.join(root, file)
            # Skip the script itself
            if filepath.endswith("replace_all.py") or filepath.endswith("rename_paths.py") or filepath.endswith("find_branding.py"):
                continue
                
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old, new in REPLACEMENTS:
                    new_content = new_content.replace(old, new)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")
            except Exception as e:
                # Likely binary
                pass

if __name__ == "__main__":
    replace_in_files()
    print("Find and replace completed in all files.")
