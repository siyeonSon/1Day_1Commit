# 투 포인터 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
posions = list(map(int, input().split()))

min = posions[0] - posions[1]
answer1, answer2 = posions[0], posions[1]

for i in range(n) :
    for j in range(i+1, n) :
        if min > posions[i] - posions[j] :
            min = posions[i] - posions[j]
            answer1, answer2 = posions[i], posions[j]

if answer1 > answer2 :
    answer1, answer2 = answer2, answer1
print(answer1, answer2)