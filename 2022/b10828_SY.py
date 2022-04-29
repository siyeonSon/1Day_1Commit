import sys
stack = []
n = int(input())
for _ in range(n):
    command = sys.stdin.readline()
    if 'push' in command:
        stack.append(int(command.split()[1]))

    elif 'pop' in command:
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)

    elif 'size' in command:
        print(len(stack))

    elif 'empty' in command:
        if stack:
            print(0)
        else:
            print(1)

    elif 'top' in command:
        if stack:
            print(stack[-1])
        else:
            print(-1)
