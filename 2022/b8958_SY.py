n = int(input())
for _ in range(n):
    problem = list(input())
    score = []
    sequence = 0
    for pro in problem:
        if pro == "O":
            sequence += 1
            score.append(sequence)
        else:
            sequence = 0

    print(sum(score))
