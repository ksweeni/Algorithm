import sys
input=sys.stdin.readline
n = int(input())
li = list(map(int, input().split(' ')))

li = sorted(li)


while(len(li) > 1):
  if li[0] > li[len(li)-1]:
    li[0], li[n-1] = li[n-1], li[0]
    
  li[len(li)-1] += li[0]/2
  li.pop(0)
print(*li)