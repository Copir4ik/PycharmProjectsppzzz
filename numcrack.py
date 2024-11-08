

number = input("Введите число: ")
number = int(number)
factors = []

place = 1
while number > 0:
    digit = number % 10
    if digit > 0:
        factors.append(digit * place)
    number //= 10
    place *= 10
factors.reverse()

print("Разделенные множители:", factors)