import sys
input = sys.stdin.readline

answer = ""
for i in range(5):
  li = input()
  if(li.find('FBI') != -1):
    answer+= str(i+1)+ " "
if(answer==""):
  print('HE GOT AWAY!')
else:
  print(answer)