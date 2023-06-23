n = int(input())
res = []
for i in range(1, n + 1):
    for j in range(i, n // i + 1):
        if (n / i / j).is_integer():
            res.append([i, j, n // i // j])
res = sorted(res, key=lambda x:sum(x))
print(*res[0])