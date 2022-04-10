leftover = [0, -1, -1, 1, -1, 1, 2, -1, 2, 3, 2, 3, 4]
n = int(input())
portion = n // 5  # 몫
rest = n % 5  # 나머지
if n <= 12:
    print(leftover[n])
else:
    while leftover[rest] == -1:
        portion -= 1
        rest += 5
    print(portion + leftover[rest])
