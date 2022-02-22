def ten(num):
    return num//10


def one(num):
    return num % 10


answer = 1
n = int(input())
changeN = n
while True:
    changeN = one(changeN)*10 + one(ten(changeN)+one(changeN))
    if changeN != n:
        answer += 1
        continue
    else:
        print(answer)
        break
