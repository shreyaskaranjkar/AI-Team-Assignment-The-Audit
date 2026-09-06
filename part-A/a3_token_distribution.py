from pathlib import Path
from statistics import mean, median

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

print("=== A3: TOKENS PER SENTENCE DISTRIBUTION ===")

for language, filename in files.items():
    path = Path("corpus", filename)
    lines = path.read_text(encoding="utf-8").splitlines()

    gpt2_counts = [
        len(gpt2.encode(line))
        for line in lines
    ]

    muril_counts = [
        len(muril.encode(line, add_special_tokens=False))
        for line in lines
    ]

    print(f"\n{language}")

    print("  GPT-2")
    print(f"    Min:    {min(gpt2_counts)}")
    print(f"    Max:    {max(gpt2_counts)}")
    print(f"    Mean:   {mean(gpt2_counts):.2f}")
    print(f"    Median: {median(gpt2_counts):.2f}")

    print("  MuRIL")
    print(f"    Min:    {min(muril_counts)}")
    print(f"    Max:    {max(muril_counts)}")
    print(f"    Mean:   {mean(muril_counts):.2f}")
    print(f"    Median: {median(muril_counts):.2f}")