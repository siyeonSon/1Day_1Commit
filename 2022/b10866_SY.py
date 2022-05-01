from collections import deque
import sys

input = sys.stdin.readline
deq = deque()


def push_front(x):
    deq.appendleft(x)


def push_back(x):
    deq.append(x)


def pop_front():
    if deq:
        return deq.popleft()
    return -1


def pop_back():
    if deq:
        return deq.pop()
    return -1


def size():
    return len(deq)


def empty():
    if deq:
        return 0
    return 1


def front():
    if deq:
        return deq[0]
    return -1


def back():
    if deq:
        return deq[-1]
    return -1


n = int(input())
for _ in range(n):
    command = input()
    if 'push_front' in command:
        push_front(command.split()[1])
    elif 'push_back' in command:
        push_back(command.split()[1])
    elif 'pop_front' in command:
        print(pop_front())
    elif 'pop_back' in command:
        print(pop_back())
    elif 'size' in command:
        print(size())
    elif 'empty' in command:
        print(empty())
    elif 'front' in command:
        print(front())
    elif 'back' in command:
        print(back())
