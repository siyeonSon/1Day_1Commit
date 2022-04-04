# 첫번째 방법

x_list, y_list = [], []
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
for x in x_list:
    if x_list.count(x) == 1:
        print(str(x), end=" ")
        break
for y in y_list:
    if y_list.count(y) == 1:
        print(str(y))
        break


# 두번째 방법
def fsn(x, y, z):
    if y == z:
        return x
    elif x == z:
        return y
    else:
        return z


a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
print(fsn(a, c, e), fsn(b, d, f))
