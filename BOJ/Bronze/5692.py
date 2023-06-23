import sys

def fact(n):
  return n*fact(n-1) if n > 0 else 1

while(True):
  num = sys.stdin.readline().rstrip() # '/'제거
  if num == '0':
    break

  result = 0

  for i in range(1,len(num)+1):
    result += int(num[len(num)-i])*fact(i)
    
  print(result)