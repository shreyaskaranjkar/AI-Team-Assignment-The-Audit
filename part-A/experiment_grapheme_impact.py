import tiktoken
import regex

files = {
    "English": "corpus/eng_sample.txt",
    "Hindi": "corpus/hin_sample.txt",
}

enc = tiktoken.get_encoding("gpt2")

for language, path in files.items():
    total_tokens = 0
    total_codepoints = 0
    total_graphemes = 0

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            line = line.lower()
            tokens = enc.encode(line)

            total_tokens += len(tokens)
            total_codepoints += len(line)
            total_graphemes += len(regex.findall(r"\X", line))

    tok_per_codepoint = total_tokens / total_codepoints
    tok_per_grapheme = total_tokens / total_graphemes

    print(language)
    print(f"Total tokens: {total_tokens}")
    print(f"Code points: {total_codepoints}")
    print(f"Grapheme clusters: {total_graphemes}")
    print(f"Tok/code point: {tok_per_codepoint}")
    print(f"Tok/grapheme: {tok_per_grapheme}")
    print()