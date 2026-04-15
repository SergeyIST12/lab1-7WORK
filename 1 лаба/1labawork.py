import re

slovar = {"0": "ноль", '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', 
          '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

def Ermolaev(text):
    num = []
    pattern = re.compile(r'\b[01]+\b')
    with open(text, "r") as file:
        while (line := file.readline().strip()):
            for a in pattern.findall(line):
                if len(a) > 1 and a[-2:] == "00" and int(a, 2) <= 2047 and int(a, 2) % 2 == 0:
                    num.append(int(a, 2))

    if num:
        for n in num:
            print("".join(c for c in str(n) if c != "0") or "0")
        avg = (min(num) + max(num)) // 2
        print(" ".join(slovar[d] for d in str(avg)))

Ermolaev("1.txt")
