# Task 25: Yosh bo‘yicha guruhlash
# Funksiya yarat:

# def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
# Shart: Har bir odamni age bo‘yicha guruhlab, ismlarini list ko‘rinishida qaytar.


def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    grouped = {}
    for person in people:
        name = person["name"]
        age = person["age"]
        
        if age not in grouped:
            grouped[age] = []
        
        grouped[age].append(name)
    
    return grouped

people = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 30},
    {"name": "Sami", "age": 25},
    {"name": "Karim", "age": 30},
    {"name": "Doni", "age": 22}
]

result = group_by_age(people)
print(result)
