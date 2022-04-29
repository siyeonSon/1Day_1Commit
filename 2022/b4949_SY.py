import sys


# logic1 : 괄호 문자를 찾는 함수
def logic(string):
    ps = ['(', ')', '[', ']']
    ps_array = []
    for str in string:
        if str in ps:
            ps_array.append(str)
    stable(ps_array)


# logic2 : 균형을 이루는가?
def stable(array):
    stack = []
    while array:
        tmp = array.pop(0)
        if stack:
            if (stack[-1] == '(' and tmp == ')') or (stack[-1] == '[' and tmp == ']'):
                stack.pop(-1)
                continue
        stack.append(tmp)
    pprint(stack)


# logic3 : 출력
def pprint(stack):
    if stack:  # not empty
        print("no")
    else:
        print("yes")


str = sys.stdin.readline()
while str[0] != ".":
    logic(str)
    str = sys.stdin.readline()
