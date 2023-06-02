n = int(input())
arr = list(map(int, input().split())) 

ys = 0
ms = 0
for i in arr:
  ys += ((int(i)//30)+1)*10
  ms += ((int(i)//60)+1)*15
if ys> ms :
  print("M", ms)
elif ys<ms :
  print("Y", ys)
elif ys==ms:
  print("Y M",ys)