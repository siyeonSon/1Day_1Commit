import sys


def home(k, n):
    people = 0
    if k == 0:
        return n
    else:
        for i in range(1, n+1):
            people += home(k-1, i)
        return people


t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())  # 층
    n = int(sys.stdin.readline())  # 호
    print(home(k, n))
