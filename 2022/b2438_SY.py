# 첫번째 코드
n = int(input())
for i in range(1, n+1):
    print("*" * i)


# 두번째 코드
n = int(input())
for i in range(1, n+1):
    for _ in range(i):
        print("*", end="")
    print()
