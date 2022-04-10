def eratos(n):
    nums = [True] * (n+1)
    for i in range(2, n+1):
        if nums[i] == True:
            for j in range(i+i, n+1, i):
                nums[j] = False
    return [k for k in range(2, n+1) if nums[k] == True]


answer = 0
n = int(input())
numbers = list(map(int, input().split()))
prime_numbers = eratos(max(numbers))
for n in numbers:
    if n in prime_numbers:
        answer += 1
print(answer)
