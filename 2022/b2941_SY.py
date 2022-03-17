string = input()
alphbet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alp in alphbet:
    if alp in string:
        string = string.replace(alp, "_")
print(len(string))
