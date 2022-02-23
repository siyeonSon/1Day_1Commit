def newScoring(score, max):
    return score/max*100


n = int(input())
scores = list(map(int, input().split()))
total = 0
for score in scores:
    total += newScoring(score, max(scores))
print(total/n)
