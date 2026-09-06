from pathlib import Path

files = [
    "eng_Latn.dev",
    "hin_Deva.dev",
    "kan_Knda.dev",
    "tam_Taml.dev"
]

data = {}

print("=== CORPUS STATISTICS ===")

for filename in files:
    path = Path("corpus", filename)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    data[filename] = lines

    words = sum(len(line.split()) for line in lines)
    characters = sum(len(line) for line in lines)
    size_bytes = path.stat().st_size

    print(f"\n{filename}")
    print(f"  Sentences:  {len(lines)}")
    print(f"  Words:      {words}")
    print(f"  Characters: {characters}")
    print(f"  Size:       {size_bytes} bytes")


print("\n=== PARALLEL ALIGNMENT CHECK ===")

for i in range(3):
    print(f"\nSentence {i + 1}")

    for filename in files:
        print(f"{filename}: {data[filename][i]}")