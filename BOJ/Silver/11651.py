n=int(input())
d=[]
for i in range(n):
  d.append(list(map(int, input().split())))
result = sorted(d, key = lambda x : (x[1], x[0]))

for i in range(n):
  print(result[i][0], result[i][1])