from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
combin = list(combinations(cards, 3))
list = []
for c in combin:
    tmp = sum(c)
    if tmp <= m:
        list.append(tmp)
print(max(list))
