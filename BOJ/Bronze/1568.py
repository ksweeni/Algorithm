n = int(input())
cnt = 1
ans = 0
while(n>0):
  if(n<cnt):
    cnt = 1
  n -= cnt
  cnt +=1
  ans +=1
print(ans)