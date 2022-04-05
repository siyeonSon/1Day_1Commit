n = int(input())
answer = 0
start = max(0, n - len(str(n))*9)  # 이게 어려웠음
end = max(0, n)  # 이게 어려웠음
for num in range(start, end):
    if sum([int(n) for n in list(str(num))])+num == n:
        answer = num
        break
print(answer)
