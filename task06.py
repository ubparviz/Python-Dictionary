# Task 6:
# Foydalanuvchidan kalit nomini input orqali so‘ra. 
# Agar dictda shu kalit bo‘lsa, qiymatini chiqarsin, aks holda "Topilmadi" chiqarsin.

car = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "color": "white"
}

key = input("Kalitni kiriting: ")

value = car.get(key, "Topilmadi")

print(value)
