def pprint(stack):
    if stack:  # not empty
        print("NO")
    else:
        print("YES")


def vps(array):
    stack = []
    while array:
        ps = array.pop(0)
        if stack:  # not empty
            if (stack[-1] == ps) or (stack[-1] == ')' and ps == '('):
                stack.append(ps)
            else:
                stack.pop(-1)
        else:
            stack.append(ps)
    pprint(stack)


n = int(input())
for _ in range(n):
    vps(list(input()))
