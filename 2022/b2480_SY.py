# 첫번째 코드
import sys
num1, num2, num3 = map(int, sys.stdin.readline().split())

point = 0
if num1 == num2:
    point += 1
if num1 == num3:
    point += 1
if num2 == num3:
    point += 1

answer = 0
if point >= 2:
    answer = 10000 + 1000*num1
elif point == 1:
    if num1 == num2:
        answer = 1000 + 100*num1
    else:
        answer = 1000 + 100*num3
else:
    answer = 100 * max([num1, num2, num3])

print(answer)


# 두번째 코드
a, b, c = sorted(map(int, input().split()))
print([100*c, 1000+100*b, 10000+1000*a][[a, b, c].count(b)-1])
