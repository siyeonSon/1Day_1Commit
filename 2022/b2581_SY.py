def eratos(m, n):
    nums = [True] * (n+1)
    nums[1] = False
    for i in range(2, n+1):
        if nums[i] == True:
            for j in range(i+i, n+1, i):
                nums[j] = False
    return [i for i in range(m, n+1) if nums[i] == True]


m = int(input())
n = int(input())
prime_numbers = eratos(m, n)
if prime_numbers:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)
