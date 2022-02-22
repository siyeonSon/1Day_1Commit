n, x = map(int, input().split())
a = list(map(int, input().split()))
answer = [i for i in a if i < x]
for a in answer:
    print(a, end=" ")
