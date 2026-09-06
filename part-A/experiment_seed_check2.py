import subprocess
import sys
import shutil

original = "fertility.py"
copy = "fertility_no_seed.py"

shutil.copyfile(original, copy)

with open(copy, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("random.seed(1337)", "# random.seed(1337)")

with open(copy, "w", encoding="utf-8") as f:
    f.write(content)

command_args = [
    "--corpus", "English=corpus/eng_sample.txt",
    "--corpus", "Hindi=corpus/hin_sample.txt",
    "--tokenizer", "gpt2"
]

print("Run 1: Original fertility.py")
result1 = subprocess.run(
    [sys.executable, original] + command_args,
    capture_output=True,
    text=True
)
print(result1.stdout)
print(result1.stderr)

print("Run 2: fertility.py without random.seed(1337)")
result2 = subprocess.run(
    [sys.executable, copy] + command_args,
    capture_output=True,
    text=True
)
print(result2.stdout)
print(result2.stderr)

print("Outputs identical:", result1.stdout == result2.stdout)