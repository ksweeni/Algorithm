N = int(input())

b=list(map(int, input().split()))
result = sorted(set(b))

for i in result:
  print(i,end=' ')