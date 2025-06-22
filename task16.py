# Task 16 (Muhim):
# Foydalanuvchidan kalit nomi so‘raladi. 
# Agar dictda mavjud bo‘lsa, o‘chiriladi. 
# Aks holda "Bunday kalit yo‘q" chiqariladi.

person = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent"
}

key = input("O'chirmoqchi bo'lgan kalit nomini kiriting: ")

if key in person:
    person.pop(key)
    print(f"'{key}' kaliti o'chirildi.")
else:
    print("Bunday kalit yo'q.")

print("Yangi dict:", person)
