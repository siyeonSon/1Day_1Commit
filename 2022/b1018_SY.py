# 체스판(2차원 배열) 출력
def pprint(array):
    for line in array:
        for l in line:
            print(l, end=" ")
        print()
    print()


# 8X8 올바른 검정색, 흰색 체스판 만들기
def makingStart(a, b):
    chess = []
    for _ in range(4):
        chess.append([a, b] * 4)
        chess.append([b, a] * 4)
    return chess


# 올바른 체스판과 다른 개수 비교(Brute Force)
def checking(ori, new):
    count = 0
    for i in range(8):
        for j in range(8):
            if ori[i][j] != new[i][j]:
                count += 1
    return count


# 검정색, 흰색으로 시작하는 올바른 체스판 형성
black = makingStart("B", "W")
white = makingStart("W", "B")

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
    answer.append(checking(black, part))
    answer.append(checking(white, part))

print(min(answer))
