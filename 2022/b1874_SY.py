import sys
n = int(sys.stdin.readline())
nums = [i for i in range(1, n+1)]  # sorted array(1 ~ n)
seq = []  # input numbers
list = []

for _ in range(n):
    seq.append(int(sys.stdin.readline()))

answer = []
pointer = 0  # index pointer

while nums:
    if not list:  # empty
        answer.append('+')
        list.append(seq.pop(0))
        continue
    if nums[pointer] == list[0]:
        answer.append('-')
        nums.pop(pointer)
        list.pop(0)
        pointer -= 1
        pointer = max(0, pointer)
    elif nums[pointer] < list[0]:
        answer.append('+')
        list.append(seq.pop(0))
        pointer += 1
    else:
        answer = ["NO"]
        break

for a in answer:
    print(a)
