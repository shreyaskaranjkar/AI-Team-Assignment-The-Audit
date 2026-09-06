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

print("=== A3: TOKENS PER WORD ===")

for language, filename in files.items():
    path = Path("corpus", filename)
    lines = path.read_text(encoding="utf-8").splitlines()

    total_words = sum(len(line.split()) for line in lines)

    gpt2_tokens = sum(
        len(gpt2.encode(line))
        for line in lines
    )

    muril_tokens = sum(
        len(muril.encode(line, add_special_tokens=False))
        for line in lines
    )

    gpt2_tpw = gpt2_tokens / total_words
    muril_tpw = muril_tokens / total_words

    print(f"\n{language}")
    print(f"  Words:          {total_words}")
    print(f"  GPT-2 tokens:   {gpt2_tokens}")
    print(f"  MuRIL tokens:   {muril_tokens}")
    print(f"  GPT-2 tok/word: {gpt2_tpw:.4f}")
    print(f"  MuRIL tok/word: {muril_tpw:.4f}")