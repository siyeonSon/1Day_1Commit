def eratos(m, n):
    nums = [True] * (n+1)
    nums[1] = False
    for i in range(2, n+1):
        if nums[i] == True:
            for j in range(i+i, n+1, i):
                nums[j] = False
    return [k for k in range(m, n+1) if nums[k] == True]


m, n = map(int, input().split())
for e in eratos(m, n):
    print(e)
