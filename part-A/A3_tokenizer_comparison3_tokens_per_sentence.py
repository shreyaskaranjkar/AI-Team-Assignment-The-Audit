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

print("=== A3: TOKENS PER PARALLEL SENTENCE ===")

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

    sentence_count = len(lines)

    gpt2_tps = gpt2_tokens / sentence_count
    muril_tps = muril_tokens / sentence_count
    token_ratio = gpt2_tokens / muril_tokens

    print(f"\n{language}")
    print(f"  Sentences:             {sentence_count}")
    print(f"  GPT-2 total tokens:    {gpt2_tokens}")
    print(f"  MuRIL total tokens:    {muril_tokens}")
    print(f"  GPT-2 tok/sentence:    {gpt2_tps:.2f}")
    print(f"  MuRIL tok/sentence:    {muril_tps:.2f}")
    print(f"  GPT-2 / MuRIL ratio:   {token_ratio:.2f}x")