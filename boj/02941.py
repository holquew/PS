cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for c in cro:
    word = word.replace(c, "?")

print(len(word))
