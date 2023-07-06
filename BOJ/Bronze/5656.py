i = 0
while True:
  n = input().split()
  if n[1] == 'E': break
  if n[1] == '>': result = int(n[0]) > int(n[2])
  elif n[1] == '>=': result = int(n[0]) >= int(n[2])
  elif n[1] == '<': result = int(n[0]) < int(n[2])
  elif n[1] == '<=': result = int(n[0]) <= int(n[2])
  elif n[1] == '==': result = int(n[0]) == int(n[2])
  elif n[1] == '!=': result = int(n[0]) != int(n[2])
  i += 1
  print(f"Case {i}:",str(result).lower())