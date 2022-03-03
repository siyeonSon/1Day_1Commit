# b2578_SY
    
def sayBingo(bingo) :
    check = diag = diagR = 0
    for i in range(5):
        if sum(bingo[i]) == 0 : check+=1
        if sum([k[i] for k in bingo]) == 0 : check+=1
        diag += bingo[i][i]
        diagR += bingo[i][4-i]
    if diag == 0 : check+=1
    if diagR == 0 : check+=1
    return check

bingo = []
for _ in range(5) :
    b = list(map(int,input().split()))
    bingo.append(b)

count = 1
A = True
while(A) :
    nums = list(map(int,input().split()))
    for n in nums :
        for i in range(5) :
            for j in range(5) :
                if bingo[i][j] == n : bingo[i][j] = 0
        if(sayBingo(bingo) == 3) :
            print(count)
            A = False
        count += 1
        
