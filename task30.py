# Task 30: Qiymati 0 bo‘lmagan elementlarni ajrat
# Funksiya yarat:

# def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
# Shart: Faqat qiymati 0 dan farq qiladigan kalit-qiymat juftliklarini yangi dict sifatida qaytar.

def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}
    for key, value in d.items():
        if value != 0:
            result[key] = value
    return result

data = {
    "Pepsi": 3,
    "Cola": 0,
    "Fanta": 5,
    "Choy": 0
}

filtered = filter_non_zero(data)
print(filtered)
