# b2805
import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
array = []

for i in range(max(trees)) :
    weight = 0
    for t in trees :
        tmp = t - i
        if(tmp > 0) :
            if(tmp >= i) :
                while(tmp >= i) :
                    tmp = tmp - i
            weight += tmp
        array.append(weight)
print(array)

