import tiktoken
import unicodedata

enc = tiktoken.get_encoding("gpt2")


def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = []
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            lines.append(unicodedata.normalize("NFC", raw))
        return lines


def calculate(path):
    lines = read_lines(path)

    per_line_fertility = []
    total_tokens = 0
    total_words = 0

    for line in lines:
        line = line.lower()

        tokens = enc.encode(line)
        words = line.split(" ")

        token_count = len(tokens)
        word_count = len(words)

        per_line_fertility.append(token_count / word_count)

        total_tokens += token_count
        total_words += word_count

    macro_average = sum(per_line_fertility) / len(per_line_fertility)
    corpus_ratio = total_tokens / total_words

    return macro_average, corpus_ratio, total_tokens, total_words


for language, path in [
    ("English", "corpus/eng_sample.txt"),
    ("Hindi", "corpus/hin_sample.txt")
]:
    macro, micro, tokens, words = calculate(path)

    print(language)
    print("Total tokens:", tokens)
    print("Total words:", words)
    print("Per-line average fertility:", macro)
    print("Corpus-level fertility:", micro)
    print("Difference:", macro - micro)
    print("Percentage difference:", ((macro - micro) / micro) * 100)
    print()