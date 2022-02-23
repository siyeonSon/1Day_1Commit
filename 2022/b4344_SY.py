c = int(input())
for _ in range(c):
    students = list(map(int, input().split()))
    n = students.pop(0)
    mean = sum(students) / n
    smart = [student for student in students if student > mean]
    print("{:.3f}%".format(len(smart)/n*100))

# 소수점 : https://blockdmask.tistory.com/534
