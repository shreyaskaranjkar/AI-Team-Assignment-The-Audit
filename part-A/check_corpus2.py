from pathlib import Path

files = [
    "eng_Latn.dev",
    "hin_Deva.dev",
    "kan_Knda.dev",
    "tam_Taml.dev"
]

print("=== Sentence 1 from each language ===")

for filename in files:
    path = Path("corpus", filename)
    lines = path.read_text(encoding="utf-8").splitlines()
    print(f"\n{filename}:")
    print(lines[0])