def element_ranking(list):
    n = len(list)
    score = [0] * n
    for i in range(n-1):
        for j in range(i+1, n):
            if list[i] > list[j]:
                score[i] += 1
            elif list[i] < list[j]:
                score[j] += 1
            else:
                score[i] += 0.5
                score[j] += 0.5
    return score


n = int(input())
answer = [0] * n

xList, yList = [], []
list = [i for i in range(n)]
for _ in range(n):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

rank = [xR+yR for xR,
        yR in zip(element_ranking(xList), element_ranking(yList))]

rank_num = []
for i in range(n):
    rank_num.append([rank[i], list[i]])
rank_num.sort(reverse=True)
# print(rank_num)

tmp = [0, 0]  # [ranking하여 얻은 값, 등수]
for i in range(1, n+1):
    num = rank_num.pop(0)
    # print(num)
    if tmp[0] == num[0]:
        answer[num[1]] = tmp[1]
    else:
        answer[num[1]] = i
        tmp = [num[0], i]

for a in answer:
    print(a, end=" ")
