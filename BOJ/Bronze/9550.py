t = int(input())
for _ in range(t):
  answer = 0
  n,k = list(map(int,input().split(' ')))
  li = list(map(int,input().split(' ')))
  for i in range(n):
    answer+= li[i]//k
  print(answer)