# b2798_SY
import sys
from itertools import combinations

n, m = map(int, input().split())
N = list(map(int, sys.stdin.readline().split()))

com = list(combinations(N, 3))
s = []
for cc in com:
    s.append(sum(cc))

nearest = 0
for ss in s:
    if not(ss > m):
        if abs(m - nearest) > abs(m - ss):
            nearest = ss
print(nearest)
