while(True):
  str = input()
  low_str = str.lower()
  if(str=='#'):
    break
  count =0
  count += low_str.count('a') + low_str.count('e') + low_str.count('i') + low_str.count('o')+ low_str.count('u')
  print(count)