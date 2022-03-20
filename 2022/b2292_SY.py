def 등차수열의합(n):
    r = 6
    return r * (n-1)


i, accum = 1, 1
n = int(input())
while True:
    accum += 등차수열의합(i)
    if n <= accum:
        print(i)
        break
    i += 1
