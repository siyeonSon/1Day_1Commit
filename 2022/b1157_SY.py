string = input()
ABC = [0 for i in range(26)]
for str in string:
    num = ord(str)
    # A-Z 65-90  a-z 97-122
    if 65 <= num <= 90:
        ABC[num-65] += 1
    elif 97 <= num <= 122:
        ABC[num-97] += 1
max = max(ABC)
if ABC.count(max) != 1:
    print("?")
else:
    print(chr(ABC.index(max)+65))
