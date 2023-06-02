N = list(map(int, input().split())) 

if(N.count(N[0])==3):
  print((N[0]*1000)+10000)
elif(N.count(N[0])==1 and N.count(N[1])==1):
  print(max(N)*100)
else:
  for i in N:
    if(N.count(i)==2):
      print((i*100)+1000)
      break