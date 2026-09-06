from pathlib import Path
import tiktoken
from transformers import AutoTokenizer

files = {
    "English": "eng_Latn.dev",
    "Hindi": "hin_Deva.dev",
    "Kannada": "kan_Knda.dev",
    "Tamil": "tam_Taml.dev",
}

gpt2 = tiktoken.get_encoding("gpt2")
muril = AutoTokenizer.from_pretrained("google/muril-base-cased")

print("=== A3: TOKEN REDUCTION ===")

for language, filename in files.items():
    path = Path("corpus", filename)
    lines = path.read_text(encoding="utf-8").splitlines()

    gpt2_tokens = sum(len(gpt2.encode(line)) for line in lines)

    muril_tokens = sum(
        len(muril.encode(line, add_special_tokens=False))
        for line in lines
    )

    reduction = (gpt2_tokens - muril_tokens) / gpt2_tokens * 100

    print(f"\n{language}")
    print(f"  GPT-2 tokens:       {gpt2_tokens}")
    print(f"  MuRIL tokens:       {muril_tokens}")
    print(f"  Token reduction:    {reduction:.2f}%")