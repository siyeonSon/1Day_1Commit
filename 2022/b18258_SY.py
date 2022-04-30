from collections import deque
deq = deque()

n = int(input())
for _ in range(n):
    command = input()
    if 'push' in command:
        deq.append(command.split()[1])

    elif 'pop' in command:
        if deq:
            print(deq.popleft())
        else:
            print(-1)

    elif 'size' in command:
        print(len(deq))

    elif 'empty' in command:
        if deq:
            print(0)
        else:
            print(1)
    elif 'front' in command:
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif 'back' in command:
        if deq:
            print(deq[-1])
        else:
            print(-1)
