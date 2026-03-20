a = input().split(" ")
b = int(a[1])
a = int(a[0])

if a > b:
    print("Ошибка")
else:
    c = []
    x = 0
    y = 1
    
    while x <= b:
        if x >= a:
            c.append(x)
        s = x + y
        x = y
        y = s
    
    if len(c) > 0:
        for i in range(len(c)):
            print(c[i], end=" ")
    else:
        print("В заданном диапазоне нет чисел Фибоначчи")
