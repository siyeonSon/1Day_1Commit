import sys
from collections import deque
input = sys.stdin.readline
deq = deque()


t = int(input())
for _ in range(t):
    answer = 0
    n, m = map(int, input().split())  # m : index
    deq = deque(map(int, input().split()))
    while deq:
        if deq[0] == max(deq):
            deq.popleft()
            answer += 1
            if not m:  # m==0
                print(answer)
                break
        else:
            deq.rotate(-1)
        if m:  # m!=0
            m -= 1
        else:
            m = len(deq)-1
