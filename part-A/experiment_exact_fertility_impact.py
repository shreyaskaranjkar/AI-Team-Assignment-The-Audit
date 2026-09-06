from pathlib import Path
import unicodedata
import tiktoken

file = Path("corpus/eng_sample.txt")

# Reproduce fertility.py's line preprocessing
lines = []
for raw in file.read_text(encoding="utf-8").splitlines():
    raw = raw.strip()
    if raw:
        lines.append(unicodedata.normalize("NFC", raw))

enc = tiktoken.get_encoding("gpt2")

original_values = []
corrected_values = []

for line in lines:
    line = line.lower()

    tokens = enc.encode(line)

    original_words = line.split(" ")
    corrected_words = line.split()

    original_values.append(len(tokens) / len(original_words))
    corrected_values.append(len(tokens) / len(corrected_words))

original_fertility = sum(original_values) / len(original_values)
corrected_fertility = sum(corrected_values) / len(corrected_values)

difference = corrected_fertility - original_fertility
percentage_change = difference / original_fertility * 100

print("Number of lines:", len(lines))
print()
print("Original fertility (split(' ')):", original_fertility)
print("Corrected fertility (split()):  ", corrected_fertility)
print()
print("Absolute difference:", difference)
print("Percentage change:", percentage_change, "%")