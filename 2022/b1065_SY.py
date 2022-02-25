# 첫번째 풀이
'''
포인트
  - 각 자리 수의 차가 모두 일치하면 한수
  - 99 이하는 모두 한수
'''


def hansu(num):
    numL = list(str(num))
    tmp, dif, count = 99, 99, 2
    for n in numL:
        n = int(n)
        if dif == n-tmp:
            count += 1
        dif = n-tmp
        tmp = n

    if count == len(numL):
        return True


a = 99
n = int(input())
if n < a:
    print(n)
else:
    for i in range(a+1, n+1):
        if(hansu(i)):
            a += 1
    print(a)


# 두번째 풀이
n = int(input())
count = 99
if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        if i//100 + i % 10 == 2*(i // 10 % 10):
            count += 1
    print(count)


# 다른 풀이
print(sum(i < 100 or
          i//10 % 10*2 == i % 10+i//100 for i in range(1, int(input())+1)))
