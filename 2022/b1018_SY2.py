# 올바른 체스판과 다른 개수 비교(Brute Force)
def checking(chess):
    num = 0
    for i in range(0, 8, 2):
        num += (chess[i][0:8:2].count("W") + chess[i][1:8:2].count("B")
                + chess[i+1][0:8:2].count("B") + chess[i+1][1:8:2].count("W"))
    return min(num, 64-num)


n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input()))

# 8X8 체스판 여러개 만들기
partion = []
partions = []
for i in range(n-7):
    for j in range(m-7):
        for tmp in chess[i:i+8]:
            partion.append(tmp[j:j+8])
        partions.append(partion)
        partion = []

answer = []
for part in partions:
    answer.append(checking(part))

print(min(answer))
