n = int(input())
x_y = []
for _ in range(n):
    x_y.append(list(map(int, input().split())))

rank = [0] * n
for i in range(n):
    for j in range(n):
        if x_y[i][0] < x_y[j][0] and x_y[i][1] < x_y[j][1]:
            rank[i] += 1  # 자신보다 덩치가 작은 사람의 수

# 덩치 등수는 자신보다 덩치가 작은 사람의 수 + 1 이다
for r in rank:
    print(r+1, end=" ")


# 등수는 나보다 뛰어난 사람이 위에 몇 명 있는지를 나타내는 것!
