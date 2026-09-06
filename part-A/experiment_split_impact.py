from pathlib import Path

file = Path("corpus/eng_sample.txt")

lines = [line.strip() for line in file.read_text(encoding="utf-8").splitlines() if line.strip()]

original_words = 0
corrected_words = 0

for line in lines:
    original_words += len(line.split(" "))
    corrected_words += len(line.split())

print("Total word count using split(' '):", original_words)
print("Total word count using split():  ", corrected_words)

print()
print("Difference:", original_words - corrected_words)
print("Percentage increase in denominator:",
      (original_words - corrected_words) / corrected_words * 100)