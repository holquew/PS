n = int(input())
c = 0 

if (n % 5 < 3):
    if (n % 3 == 0):   
        c = n // 3 
    else:
        c = -1
elif (n % 5 >= 3):
    c += n // 5
    n = n % 5 
    c += n // 3
else: 
    c = -1

print(c)
