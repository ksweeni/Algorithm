n = int(input())
for _ in range(n):
  s = int(input())
  op = int(input())
  for _ in range(op):
    q,p=list(map(int,input().split(' ')))
    s+= q*p
  print(s)