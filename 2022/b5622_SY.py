# 첫번째 풀이
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str = input()
answer = 0
for s in str:
    if s in abc[0:3]:
        answer += 3
    elif s in abc[3:6]:
        answer += 4
    elif s in abc[6:9]:
        answer += 5
    elif s in abc[9:12]:
        answer += 6
    elif s in abc[12:15]:
        answer += 7
    elif s in abc[15:19]:
        answer += 8
    elif s in abc[19:22]:
        answer += 9
    elif s in abc[22:]:
        answer += 10
print(answer)


# 두번째 풀이
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
str = input()
answer = 0
for s in str:
    for d in dial:
        if s in d:
            answer += dial.index(d)+3
print(answer)
