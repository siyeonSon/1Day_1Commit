import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop(-1)
print(sum(stack))
