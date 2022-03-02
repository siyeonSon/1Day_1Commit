string = input()
str = string.split(" ")
answer = len(str)
for s in str:
    if s == '':
        answer -= 1
print(answer)
