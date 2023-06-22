import sys
input = sys.stdin.readline

while(True):
  num = int(input())
  if(num==0):
    break
  answer = 0
  for i in range(num+1):
    answer+=i**2
    
  print(answer)