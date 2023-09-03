import sys
input=sys.stdin.readline

n = int(input())
distance = list(map(int, input().split(' ')))
literPrice = list(map(int, input().split(' ')))

minPrice = literPrice[0]
total = 0
for i in range(n-1):
  if minPrice > literPrice[i]:
    minPrice = literPrice[i]
  total += minPrice*distance[i]
print(total)