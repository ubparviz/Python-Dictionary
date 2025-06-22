# Task 26: 2 ta dictni birlashtirish
# Funksiya yarat:

# def merge_dicts(a: dict, b: dict) -> dict:
# Shart: Berilgan ikkita dictni birlashtir. Agar bir xil kalit bo‘lsa, b dagi qiymat ustun bo‘lsin.

def merge_dicts(a: dict, b: dict) -> dict:
    merged = a.copy()
    merged.update(b)
    return merged

a = {"name": "Ali", "age": 25}
b = {"age": 26, "city": "Tashkent"}

result = merge_dicts(a, b)
print(result)
