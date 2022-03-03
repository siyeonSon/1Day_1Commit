# b2178
import sys
def pprint(arr) :
    for line in arr :
        print(line)

n, m = map(int, sys.stdin.readline().split())
maze = []
for _ in range(n) :
    maze.append(list(map(int, input())))

def BFS():
    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]
    q = deque()





