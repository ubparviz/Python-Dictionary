# Task 12:
# inventory dict bor. Agar mahsulot yo‘q bo‘lsa, uni quantity = 0 bilan qo‘sh.


inventory = {
    "Pepsi": 10,
    "Cola": 5
}
print(inventory)

product = input("Mahsulot nomini kiriting: ").title()

if product not in inventory:
    inventory[product] = 0

print(inventory)
