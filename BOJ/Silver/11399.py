import sys
input=sys.stdin.readline
n = int(input())
li = list(map(int, input().split(' ')))

li = sorted(li)
times = 0
time = []
for l in li:
  times+=l
  time.append(times)
print(sum(time))