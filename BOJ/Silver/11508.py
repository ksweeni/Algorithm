import sys
input=sys.stdin.readline
n = int(input())
li = []
for i in range(n):
  li.append(int(input()))

li = sorted(li,reverse=True)
sum = 0
count = 0

for l in li:
  if count == 2:
    count=0
  else : 
    sum+=l
    count+=1
print(sum)