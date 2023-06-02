while(True) :
  str = input()
  if(str=='# 0 0'):
    break
  n, a, w = str.split(' ')
  if int(a) > 17 or int(w) >= 80:
    print(n, 'Senior')
  else :
    print(n, 'Junior')