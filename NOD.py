# НОД в пайтоне 

a, b = map(int, input().split())
while b != 0 :
    if a>b:
        a = a-b
    else:
        b = b-a

print(a, b)