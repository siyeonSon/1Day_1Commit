two_word = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
three_word = 'dz='
str = 'c=c='
answer = len(str)
for tw in two_word:
    if tw in str:
        answer -= 1
if three_word in str:
    answer -= 2
print(answer)
