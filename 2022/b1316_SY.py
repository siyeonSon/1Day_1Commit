def checking(string):
    tmp = string
    sCount = [0 for _ in range(26)]
    for str in string:
        i = ord(str)-97
        if sCount[i] == 0 and tmp == str:  # 단어하나
            return True
        elif sCount[i] == 0 and tmp != str:  # 새로운 문자 초기 등록
            sCount[i] += 1
        elif sCount[i] != 0 and tmp == str:  # 그룹 단어 생성 중
            sCount[i] += 1
        elif sCount[i] != 0 and tmp != str:  # 그룹 단어가 아님
            return False
        tmp = str
    return True


n = int(input())
answer = 0
for _ in range(n):
    s = input()
    if checking(s):
        answer += 1
print(answer)
