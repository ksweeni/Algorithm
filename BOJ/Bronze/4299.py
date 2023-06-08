a,b = map(int,input().split())  

if  a+b < 0 or a-b < 0 or (a + b) % 2:
    print(-1)
else:
  a = (a+b)//2
  b = a-b
  print(a, b)