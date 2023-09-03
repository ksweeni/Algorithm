import sys
input=sys.stdin.readline
n = int(input())
li = []
tips = 0
for i in range(n):
  li.append(int(input()))

li = sorted(li, reverse=True)

for idx, v in enumerate(li):
  tip = v-((idx+1)-1)
  if tip < 0 :
    continue
  else: 
    tips+=tip

print(tips)