def czy_cyfra(str):
    try:
        digit = int(str)
        return isinstance(digit, int)
    except ValueError:
        return False


def replace_word(tekst):
    for i in range(len(tekst)):
        if tekst[i:i + len("zero")] == "zero":
            tekst = tekst[:i] + "0" + tekst[i + len("zero"):]

        if tekst[i:i + len("one")] == "one":
            tekst = tekst[:i] + "1" + tekst[i + len("one"):]

        if tekst[i:i + len("two")] == "two":
            tekst = tekst[:i] + "2" + tekst[i + len("two"):]

        if tekst[i:i + len("three")] == "three":
            tekst = tekst[:i] + "3" + tekst[i + len("three"):]

        if tekst[i:i + len("four")] == "four":
            tekst = tekst[:i] + "4" + tekst[i + len("four"):]

        if tekst[i:i + len("five")] == "five":
            tekst = tekst[:i] + "5" + tekst[i + len("five"):]

        if tekst[i:i + len("six")] == "six":
            tekst = tekst[:i] + "6" + tekst[i + len("six"):]

        if tekst[i:i + len("seven")] == "seven":
            tekst = tekst[:i] + "7" + tekst[i + len("seven"):]

        if tekst[i:i + len("eight")] == "eight":
            tekst = tekst[:i] + "8" + tekst[i + len("eight"):]

        if tekst[i:i + len("nine")] == "nine":
            tekst = tekst[:i] + "9" + tekst[i + len("nine"):]

    return tekst


suma = 0

with open('------', 'r') as file:
    lines = file.readlines()
    for line in lines:
        match = replace_word(line)
        su = 0
        for c in match:
            if czy_cyfra(c):
                suma += int(c) * 10
                su = int(c) * 10
                break

        for c in reversed(match):
            if czy_cyfra(c):
                suma += int(c)
                su += int(c)
                break
        print(match + " liczba " + str(su))
print(suma)
