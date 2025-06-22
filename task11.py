# Task 11:
# Bo‘sh config dict yarat. Foydalanuvchidan 3 ta setting nomi va qiymati so‘raladi. 
# Ularni dictga joyla.

config = {}

for i in range(3):
    key = input(f"{i+1}-kalit soz kiriting: ")
    value = input(f"{key} uchun qiymatni kiriting: ")
    config[key] = value

print(config)
