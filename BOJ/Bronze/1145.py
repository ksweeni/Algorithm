n = list(map(int, input().split()))
min_num = min(n)
cnt = 0
while True:
    cnt = 0
    for i in range(len(n)):
        if min_num % n[i] == 0 :
            cnt += 1
    if cnt >= 3:
        print(min_num)
        break
    min_num += 1