# Task 24: Eng ko‘p uchragan harfni topish
# Funksiya yarat:

# def most_common_char(text: str) -> str:
# Shart: Berilgan matndagi eng ko‘p uchraydigan bitta harfni qaytar.

def most_common_char(text: str) -> str:
    freq = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1
    
    most_common = max(freq, key=freq.get)
    return most_common

result = most_common_char("Men Najod Talimda o'qiyapman")
print(result)
