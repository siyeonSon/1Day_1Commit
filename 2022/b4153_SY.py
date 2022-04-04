def triangle(arr):
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        return "right"
    else:
        return "wrong"


while True:
    arr = sorted(list(map(int, input().split())))
    if sum(arr) == 0:
        break
    print(triangle(arr))
