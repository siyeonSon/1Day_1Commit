from itertools import permutations

countings = []
bulbs = []

n = int(input())
bulbs = [input() for _ in range(n)]

per = list(permutations(bulbs))
for p in per :
    bulb_way = "".join(p)
    countings.append(bulb_way.count("01") + bulb_way.count("10"))
print(min(countings))