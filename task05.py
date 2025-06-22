# Task 5:
# .get() metodi orqali year degan kalitni o‘qishga harakat qil. U mavjud emas. Default qiymat ber.

car = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "color": "white"
}

year = car.get("year", 2025)

print("Year:", year)
