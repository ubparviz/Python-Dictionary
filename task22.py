# Task 22: Talabalarni guruhlash
# Funksiya yarat:

# def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
# Natija: {"A": ["Ali", "Soli"], "B": ["Vali", "Karim"]}

def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    grouped = {}
    for student in students:
        name = student["name"]
        group = student["group"]
        
        if group not in grouped:
            grouped[group] = []
        
        grouped[group].append(name)
    
    return grouped

students = [
    {"name": "Ali", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Soli", "group": "A"},
    {"name": "Karim", "group": "B"}
]

result = group_students(students)
print(result)
