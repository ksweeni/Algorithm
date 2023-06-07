import sys
n = int(sys.stdin.readline())
plug = 0
for i in range(n):
    plug += int(sys.stdin.readline())
print(plug - (n - 1))