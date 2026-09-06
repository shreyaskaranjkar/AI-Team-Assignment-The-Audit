import subprocess
import sys

script = "fertility.py"

print("Run 1: Original fertility.py")
result1 = subprocess.run(
    [sys.executable, script, "gpt2", "corpus/eng_sample.txt", "corpus/hin_sample.txt"],
    capture_output=True,
    text=True
)
print(result1.stdout)

print("Run 2: Same fertility.py")
result2 = subprocess.run(
    [sys.executable, script, "gpt2", "corpus/eng_sample.txt", "corpus/hin_sample.txt"],
    capture_output=True,
    text=True
)
print(result2.stdout)

print("Outputs identical:", result1.stdout == result2.stdout)