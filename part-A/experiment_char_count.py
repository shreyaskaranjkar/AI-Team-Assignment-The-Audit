import unicodedata

samples = {
    "English": "hello",
    "Hindi": "नमस्ते",
    "Kannada": "ನಮಸ್ಕಾರ",
    "Tamil": "வணக்கம்",
    "Telugu": "నమస్కారం",
}

for language, text in samples.items():
    code_points = len(text)
    utf8_bytes = len(text.encode("utf-8"))

    print(f"{language}:")
    print(f"  Text: {text}")
    print(f"  Python len(): {code_points}")
    print(f"  UTF-8 bytes: {utf8_bytes}")
    print()