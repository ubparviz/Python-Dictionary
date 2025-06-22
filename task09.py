# Task 9:
# Ro‘yxatdagi har bir user ning active qiymatini False qilib chiq:

# users = [
#   {"id": 1, "active": True},
#   {"id": 2, "active": True},
# ]

users = [
    {"id": 1, "active": True},
    {"id": 2, "active": True},
]

for user in users:
    user["active"] = False

print(users)
