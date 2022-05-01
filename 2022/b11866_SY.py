# 요세푸스 문제 -> 원형 큐
# 풀이 1
from collections import deque

n, k = map(int, input().split())

deq = deque([i for i in range(1, n+1)])
answer = []

while deq:
    deq.rotate(-k)
    answer.append(str(deq.pop()))

print("<" + ", ".join(answer) + ">")


# 풀이 2
n, k = map(int, input().split())
answer = []

nums = [i for i in range(1, n+1)]
pointer = k-1

while nums:
    if len(nums) < pointer:
        pointer %= len(nums)
    answer.append(str(nums.pop(pointer)))
    pointer += k-1

print("<" + ", ".join(answer) + ">")
