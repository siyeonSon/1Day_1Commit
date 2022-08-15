#b1181_SY
import sys
N = int(input())  # sys.stdin.readline().split()
words = []
for i in range(N) :
    w = input()
    words.append(w)

words = list(set(words))
words.sort()
words.sort(key=len)

for wor in words : 
    print(wor, end="\n")













