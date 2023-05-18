T = int(input())

for i in range(T) :
  arr = list(map(int,input().split()))
  p = int(arr[0] / arr[1])
  m = int(arr[0] % arr[1])
  print("You get",p ,"piece(s) and your dad gets",m,"piece(s).")