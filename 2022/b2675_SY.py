for _ in range(int(input())):
    r, s = input().split()
    for str in s:
        print("".join(str*int(r)), end="")
    print()
