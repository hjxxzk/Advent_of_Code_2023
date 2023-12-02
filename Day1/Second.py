def czy_cyfra(str):
    try:
        digit = int(str)
        return isinstance(digit, int)
    except ValueError:
        return False


suma = 0

with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        for c in line:
            if czy_cyfra(c):
                suma += int(c) * 10
                break
        for c in reversed(line):
            if czy_cyfra(c):
                suma += int(c)
                break

print(suma)

