from pathlib import Path
import tiktoken

file = Path("corpus/eng_sample.txt")

lines = [
    line.strip()
    for line in file.read_text(encoding="utf-8").splitlines()
    if line.strip()
]

enc = tiktoken.get_encoding("gpt2")

total_tokens = 0
original_words = 0
corrected_words = 0

for line in lines:
    total_tokens += len(enc.encode(line.lower()))
    original_words += len(line.split(" "))
    corrected_words += len(line.split())

original_fertility = total_tokens / original_words
corrected_fertility = total_tokens / corrected_words

difference = corrected_fertility - original_fertility
percentage_change = difference / original_fertility * 100

print("Total tokens:", total_tokens)
print("Original word count (split(' ')):", original_words)
print("Corrected word count (split()):  ", corrected_words)
print()
print("Original fertility:", original_fertility)
print("Corrected fertility:", corrected_fertility)
print("Difference:", difference)
print("Percentage change:", percentage_change, "%")