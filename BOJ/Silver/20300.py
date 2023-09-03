import sys
input=sys.stdin.readline

n = int(input())
kg = list(map(int, input().split(' ')))
kg = sorted(kg, reverse=True)
temp = []
if(n%2==1):
  temp.append(kg.pop(0))
for i in range(n//2):
  temp.append(kg[i]+kg[len(kg)-1-i])
print(max(temp))