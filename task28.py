# Task 28: Satr uzunligi bo‘yicha guruhlash

# def group_by_length(words: list[str]) -> dict[int, list[str]]:
# Shart: Har bir so‘zni uzunligiga qarab dict ichiga guruhlab joylashtir.

def group_by_length(words: list[str]) -> dict[int, list[str]]:
    grouped = {}
    for word in words:
        length = len(word)
        if length not in grouped:
            grouped[length] = []
        grouped[length].append(word)
    return grouped

words = ["salom", "kitob", "daftar", "olma", "non", "kompyuter"]
result = group_by_length(words)
print(result)
