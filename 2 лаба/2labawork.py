import re

slovar = {
    "0": "ноль", '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

def Ermolaev(text):
    num = []
    # Чётные двоичные числа (заканчиваются на 0), длиной до 11 символов
    pattern = re.compile(r'\b[01]{1,10}0\b')

    with open(text, "r") as file:
        content = file.read()
        for a in pattern.findall(content):
            # Проверка: вторая справа цифра — 0 и число ≤ 2047
            if len(a) >= 2 and a[-2] == '0':
                dec = int(a, 2)
                if dec <= 2047:
                    num.append(dec)

    if num:
        for n in num:
            # Выводим число без нулей (если только нули — выводим "0")
            print("".join(c for c in str(n) if c != "0") or "0")
        avg = (min(num) + max(num)) // 2
        # Выводим среднее прописью
        print(" ".join(slovar[d] for d in str(avg)))
    else:
        print("Подходящих чисел не найдено")

# Пример вызова
Ermolaev("2.txt")
