n = int(input())
answer = []
for i in range(n):
  N = list(map(int, input().split()))
  if(N.count(N[0])==3):
    answer.append(10000+(N[0]*1000))
  elif(N.count(N[0])==1 and N.count(N[1])==1):
    answer.append(max(N)*100)
  else:
    for j in N:
      if(N.count(j)==2):
        answer.append((j*100)+1000)
        break
  
print(max(answer))