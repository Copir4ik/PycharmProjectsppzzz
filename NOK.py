# НОК в питухоне

a, b = map(int, input().split())

x,y =a,b
while b != 0 :
    if a>b:
        a = a-b
    else:
        b = b-a
if a == 0:
    nd = b
else:
    nd = a

    NOK = x * y / nd

    print(NOK)