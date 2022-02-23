num = 1
for _ in range(3):
    num *= int(input())
array = list(str(num))
for i in range(10):
    print(array.count(str(i)))
