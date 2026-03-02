import os

TARGET_DIR = r"e:\SWDEV\GIMUseek\agenticseek"

# Renaming mapping
RENAMES = [
    ("agentic-seek", "spydra"),
    ("AgenticSeek", "Spydra"),
    ("agentic_seek", "spydra"),
    ("agenticSeek", "spydra"),
    ("fosowl", "spyder_solutions"),
]

ignore_dirs = {".git", "node_modules", "__pycache__", "build", "dist", ".venv", ".pytest_cache"}

def rename_paths():
    # Walk bottom-up so renaming a dir doesn't invalidate paths inside it
    for root, dirs, files in os.walk(TARGET_DIR, topdown=False):
        # Rename files
        for filename in files:
            for old, new in RENAMES:
                if old in filename:
                    old_path = os.path.join(root, filename)
                    new_filename = filename.replace(old, new)
                    new_path = os.path.join(root, new_filename)
                    try:
                        os.rename(old_path, new_path)
                        print(f"Renamed file: {old_path} -> {new_filename}")
                    except Exception as e:
                        print(f"Error renaming {old_path}: {e}")
                    break # Don't try other replacements on the same file if one succeeded

        # Rename directories, excluding ignore_dirs
        for dirname in dirs:
            if dirname in ignore_dirs: continue
            
            for old, new in RENAMES:
                if old in dirname:
                    old_path = os.path.join(root, dirname)
                    new_dirname = dirname.replace(old, new)
                    new_path = os.path.join(root, new_dirname)
                    try:
                        os.rename(old_path, new_path)
                        print(f"Renamed dir: {old_path} -> {new_dirname}")
                    except Exception as e:
                        print(f"Error renaming {old_path}: {e}")
                    break

if __name__ == "__main__":
    rename_paths()
    print("Renaming completed.")
