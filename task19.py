# Task 19:
# Quyidagi dictdagi barcha qiymatlar soni bo‘lsa, ularni yig‘indisini hisobla:

# scores = {"math": 90, "english": 85, "science": 92}

scores = {
    "math": 90,
    "english": 85,
    "science": 92
}

total = 0
for value in scores.values():
    if isinstance(value, (int, float)):
        total += value

print("Yig'indi:", total)
