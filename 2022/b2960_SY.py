'''
# 에라토스테네스의 체
def eratos(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    nums = [True] * (n+1)
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m):
        if nums[i] == True:  # i가 소수인 경우
            for j in range(i+i, n+1, i):  # i이후 i의 배수들을 False 판정
                nums[j] = False
    return [i for i in range(2, n+1) if nums[i] == True]
'''
n, k = map(int, input().split())
count = 0
nums = [True] * (n+1)
for i in range(2, n+1):
    if nums[i] == True:
        for j in range(i, n+1, i):
            if nums[j] == True:
                nums[j] = False
                count += 1
            if count == k:
                print(j)
                break
