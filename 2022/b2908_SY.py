a, b = input().split()
_a = ''.join(reversed(a))
_b = ''.join(reversed(b))

print(max([int(_a), int(_b)]))
