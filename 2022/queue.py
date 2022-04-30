global queue
queue = []


def push(x):
    queue.append(x)


def pop():
    if queue:
        return queue.pop(0)
    return -1


def size():
    return len(queue)


def empty():
    if queue:
        return 0
    return 1


def front():
    if queue:
        return queue[0]
    return -1


def back():
    if queue:
        return queue[-1]
    return -1
