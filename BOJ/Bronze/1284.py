while(True):
  n = int(input())
  answer = 2 # 경계판과 숫자 양끝
  if(n==0):
    break
  n = list(map(int, str(n)))
  answer+= (len(n)-1) # 사이 여백
  for i in n:
    if(i ==0):
      answer+=4
    elif(i ==1):
      answer += 2
    else :
      answer += 3
  print(answer)