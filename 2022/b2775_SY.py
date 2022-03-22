# 시간 초과 로직
'''
import sys
def home(k, n):
    if k == 0:
        return n
    elif k == 1:
        return sum([i for i in range(n+1)])
    else:
        people = 0
        for i in range(n+1):
            people += home(k-1, i)
        return people

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(home(k, n))
'''
