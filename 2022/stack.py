global stack
stack = []


def push(x):
    stack.append(x)


def pop():
    if stack:
        return stack.pop(-1)
    return -1


def size():
    return len(stack)


def empty():
    if stack:  # not empty
        return 0
    return 1


def top():
    if stack:
        return stack[-1]
    return -1
