def pprint(arr):
    for a in arr:
        print(a, end=" ")


answer = [-1 for _ in range(26)]
tmp = []
count = 0
for str in input():
    if not str in tmp:
        tmp.append(str)
        answer[ord(str)-97] = count
    count += 1
pprint(answer)
