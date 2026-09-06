from pathlib import Path
import tiktoken
from transformers import AutoTokenizer

files = {
    "English": "eng_Latn.dev",
    "Hindi": "hin_Deva.dev",
    "Kannada": "kan_Knda.dev",
    "Tamil": "tam_Taml.dev",
}

print("=== TOKENIZER VERIFICATION ===")

# GPT-2 tokenizer
gpt2 = tiktoken.get_encoding("gpt2")

# MuRIL tokenizer
muril = AutoTokenizer.from_pretrained("google/muril-base-cased")

print("\nBoth tokenizers loaded successfully.")

for language, filename in files.items():
    path = Path("corpus", filename)
    lines = path.read_text(encoding="utf-8").splitlines()

    gpt2_tokens = sum(
        len(gpt2.encode(line))
        for line in lines
    )

    muril_tokens = sum(
        len(muril.encode(line, add_special_tokens=False))
        for line in lines
    )

    print(f"\n{language}")
    print(f"  Sentences:       {len(lines)}")
    print(f"  GPT-2 tokens:    {gpt2_tokens}")
    print(f"  MuRIL tokens:    {muril_tokens}")