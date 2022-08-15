# b2439_SY

n = int(input())

for i in range(1, n+1):  # 1 2 3 4 5
    for _ in range(n-i):  # 4 3 2 1 0
        print(" ", end="")
    for _ in range(i):  # 1 2 3 4 5
        print("*", end="")
    print()
