import sys  
read = sys.stdin.readline  

s = read().rstrip()  
p = read().rstrip()  

answer = 0
index = 0

while(index < len(p)):
  str = ''
  if s.find(p[index:])!= -1:
    answer+=1
    break
    
  for i in range(index, len(p)):
    str+=p[i]
    if s.find(str) == -1 :
      index = i
      answer+=1
      break
    
print(answer)