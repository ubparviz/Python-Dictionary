# Task 21: Ismlar sonini sanash
# Funksiya yarat:

# def count_names(names: list[str]) -> dict[str, int]:
# Natija: {"Ali": 3, "Vali": 2, "Sami": 1}

def count_names(names: list[str]) -> dict[str, int]:
    counts = {}
    for name in names:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    return counts

names = ["Ali", "Vali", "Ali", "Sami", "Vali", "Ali", "Parviz", "Aziz", "Parviz"]
result = count_names(names)
print(result)
