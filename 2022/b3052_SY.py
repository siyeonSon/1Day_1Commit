array = []
for _ in range(10):
    tmp = int(input()) % 42
    if not(tmp in array):
        array.append(tmp)
print(len(array))
