import sys
input=sys.stdin.readline

n,k = map(int,input().split(' '))
li = []
for i in range(n):
  li.append(int(input()))
  
li = sorted(li,reverse=True)
count = 0
for l in li:
  if l <= k:
    count += (k//l)
    k = k % l
print(count)