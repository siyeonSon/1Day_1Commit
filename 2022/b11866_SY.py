# 요세푸스 문제 -> 원형 큐

from collections import deque

n, k = map(int, input().split())

deq = deque([i for i in range(1, n+1)])
answer = []

while deq:
    deq.rotate(-k)
    answer.append(str(deq.pop()))

print("<" + ", ".join(answer) + ">")
