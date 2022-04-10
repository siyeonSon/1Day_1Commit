n = int(input())
end = 666
plus, count = 1, 1
while n != count:
    end += plus
    if "666" in str(end):
        count += 1
print(end)


'''
# 왜 안되는지 모르겠는 코드
def makingSix(end):
    arr = []
    for e in end:
        for i in range(11):
            arr.append(int(str(i) + str(e)))
            arr.append(int(str(e) + str(i)))
    arr = list(set(arr))
    arr.sort()
    return arr


n = int(input())-1  # 첫번째 영화 == index(0)
end = [666]

while True:
    end = makingSix(end)
    if len(end) >= 10000:
        print(end[n])
        break
'''
