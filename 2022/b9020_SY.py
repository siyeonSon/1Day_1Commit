def eratos(n):
    nums = [True] * (n+1)
    for i in range(2, n+1):
        if nums[i] == True:
            for j in range(i+i, n+1, i):
                nums[j] = False
    return [k for k in range(2, n+1) if nums[k] == True]


t = int(input())
for _ in range(t):
    n = int(input())
    prime_numbers = eratos(n)
    tmp = n // 2
    for i in range(tmp):
        if tmp-i in prime_numbers and tmp+i in prime_numbers:
            print(tmp-i, tmp+i)
            break
