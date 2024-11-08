numbeer = input()
numbeer =int(numbeer)

def to_base_7(numbeer):
    if numbeer == 0:
        return '0'
    result = ''
    while numbeer > 0:
        result = str(numbeer % 7) + result
        numbeer //= 7
    return result

print(to_base_7(numbeer))