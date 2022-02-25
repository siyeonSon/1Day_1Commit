def n2dn(n):
    sum = 0
    for i in list(str(n)):
        sum += int(i)
    return sum + n


answer = [i for i in range(1, 10001)]
for i in range(1, 10001):
    dn = n2dn(i)
    if dn in answer:
        answer.remove(dn)

for a in answer:
    print(a)
