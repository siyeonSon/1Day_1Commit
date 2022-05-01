from collections import deque
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
