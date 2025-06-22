# Task 29: Active foydalanuvchilarni chiqarish

# def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
# Shart: Faqat "active": True bo‘lgan foydalanuvchilarning ismini ro‘yxat qilib qaytar.

def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_users = []
    for name, info in users.items():
        if info.get("active") == True:
            active_users.append(name)
    return active_users

users = {
    "Ali": {"email": "ali@example.com", "active": True},
    "Vali": {"email": "vali@example.com", "active": False},
    "Baxti": {"email": "baxti@example.com", "active": True},
}

result = get_active_users(users)
print(result)
