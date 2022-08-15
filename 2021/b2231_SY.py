# b2231_SY1
n = input()
same = []
for i in range(int(n)):
    sum = 0
    sum += i
    for j in str(i):
        sum += int(j)
    if sum == int(n):
        same.append(i)
if len(same) == 0:
    print(0)
else:
    print(min(same))


# b2231_SY2
def plus(num):
    num_len = len(str(num))
    sum = 0
    sum += num
    for _ in range(num_len):
        sum += num % 10
        num = int(num / 10)
    return sum


n = int(input())
n_len = len(str(n))
same = []
for i in range(n):
    result = plus(i)
    if result == n:
        same.append(i)
if len(same) == 0:
    print(0)
else:
    print(min(same))
