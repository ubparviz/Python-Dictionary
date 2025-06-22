# Task 31: Harflar chastotasini hisoblash
# Funksiya yarat:

# def count_letters(text: str) -> dict[str, int]:
# Shart: Berilgan matndagi harflarning necha marta uchrashini hisoblab, dict qaytar.
# Masalan: "assalomu alaykum" → { 'a': 4, 's': 2, 'l': 2, ... }

def count_letters(text: str) -> dict[str, int]:
    letter_counts = {}
    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

result = count_letters("assalomu alaykum")
print(result)
