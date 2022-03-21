def whereisX(x):
    n, tmp = 0, 0
    while True:
        an = (n**2 + n + 2) // 2
        if tmp <= x < an:
            return [n, x-tmp]
            break
        n += 1
        tmp = an


x = int(input())
list = whereisX(x)
level = list.pop(0)
distance = list.pop(0)
if level % 2 == 1:
    print(str(level-distance) + "/" + str(distance+1))
else:
    print(str(distance+1) + "/" + str(level-distance))
