def jinsu(n, m):
    s = 0
    while True:
        if n // m == 0:
            s += n
            break
        s += n%m
        n = n // m
    return s

for i in range(2992,10000):
    ten=jinsu(i,10)
    twe = jinsu(i, 12)
    six = jinsu(i, 16)
    if ten==twe and twe==six : 
        print(i)