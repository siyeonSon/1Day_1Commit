def eratos(n):
    nums = [True] * (2*n + 1)
    nums[0], nums[1] = False, False
    for i in range(2, len(nums)):
        if nums[i] == True:
            for j in range(i+i, len(nums), i):
                nums[j] = False
    return [k for k in range(n+1, 2*n+1) if nums[k] == True]


while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(len(eratos(n)))
