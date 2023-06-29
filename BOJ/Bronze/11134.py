import math
t = int(input())
for _ in range(t):
  n,k = list(map(int,input().split(' ')))
  print(math.ceil(n/k))