from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    num = [int(stdin.readline()) for i in range(N)]
    if sum(num) == 0:
        print("0")
    elif sum(num) > 0:
        print("+")
    else:
        print("-")