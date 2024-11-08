number = input()
number = int(number)
shi = []
p = 1

while number > 0:
    digit = number % 10
    if digit > 0:
        shi.append(digit * p)
    number //= 10
    p *= 10
shi.reverse()

print(shi)