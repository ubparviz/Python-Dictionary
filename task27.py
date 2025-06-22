#  Task 27: Telefon daftari (Mini loyihacha)
# Funksiya yarat:

# def phonebook_menu(phonebook: dict[str, str]) -> None:
# Shart:

# 1: Kontakt qo‘shish (ism → telefon)
# 2: Barcha kontaktlarni chiqarish
# 3: Ism bo‘yicha telefon qidirish
# dict bilan menu (input orqali) ishlash ko‘nikmasini beradi.

def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("\nTelefon daftari menyusi:")
        print("1 - Kontakt qo'shish")
        print("2 - Barcha kontaktlarni chiqarish")
        print("3 - Ism bo'yicha telefon qidirish")
        print("0 - Chiqish")

        choice = input("Tanlang (0-3): ")

        if choice == "1":
            name = input("Ismni kiriting: ")
            phone = input("Telefon raqamini kiriting: ")
            phonebook[name] = phone
            print(f"{name} kontakt saqlandi.")
        
        elif choice == "2":
            if phonebook:
                print("\nKontaktlar ro'yxati:")
                for name, phone in phonebook.items():
                    print(f"{name} → {phone}")
            else:
                print("Kontaktlar mavjud emas.")
        
        elif choice == "3":
            name = input("Qidirilayotgan ismni kiriting: ")
            phone = phonebook.get(name)
            if phone:
                print(f"{name} → {phone}")
            else:
                print("Kontakt topilmadi.")
        
        elif choice == "0":
            print("Dasturdan chiqildi.")
            break
        
        else:
            print("Noto'g'ri tanlov. Iltimos, 0 dan 3 gacha raqam kiriting.")

my_phonebook = {}
phonebook_menu(my_phonebook)
