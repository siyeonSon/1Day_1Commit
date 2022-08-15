# b9095_SY
import itertools
n = int(input())
plus = [1, 2, 3] # itertools.combinations(arr, 2)

three = [[3], [1, 2], [2, 1], [1, 1, 1]]
two = [[2], [1, 1]]
one = [[1]]

for _ in range(n) :
    t = int(input())
    count = 0  # len(list)
    tmp = t // 3
    answer = list(itertools.combinations(three, 3))
    print(answer)
