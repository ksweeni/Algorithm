T = int(input())

def cal(num) :
  if num == 1 :
    return 1
  elif num ==2 :
    return 2
  elif num == 3 :
    return 4
  else :
    return cal(num-1) + cal(num-2) + cal(num-3)

for i in range(T) :
  test = int(input())
  print(cal(test))