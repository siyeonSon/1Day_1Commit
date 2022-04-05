def move(start, end):
    print(start, end)  # 이동좌표 출력


def hanoi(n, first, second, third):
    if(n == 1):
        move(first, third)
    else:
        hanoi(n-1, first, third, second)  # 1 ~ n-1 원반들을 두번째 장대로 이동
        move(first, third)  # n 원반 이동
        hanoi(n-1, second, first, third)  # 1 ~ n-1 원반들을 세번째 장대로 이동


n = int(input())
count = 2**n - 1  # 원반 이동 횟수
print(count)
hanoi(n, 1, 2, 3)
