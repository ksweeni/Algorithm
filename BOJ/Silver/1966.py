t = int(input()) 
printq= []
for _ in range(t):
  n, m = map(int, input().split())
  printq = list(enumerate(list(map(int, input().split()))))
  v = printq[m]
  idx = 0
  
  while len(printq):
    maxv = max([i[1] for i in printq])
    if printq[0][1] == maxv:
      now = printq.pop(0)
      idx += 1
      if now == v:
        print(idx)
        break
    else:
      now = printq.pop(0)
      printq.append(now)