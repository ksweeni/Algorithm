from sys import stdin

n = int(stdin.readline())
cost = 0

for i in range(n):
  time,d = stdin.readline().rstrip().split(' ')
  d = int(d)
  h,m = map(int, time.split(':'))
  endhour=h
  endmin=m+d
  if endmin >=60:
    endhour+= endmin//60
    endmin-=60
  if endhour >=24:
    endhour-=24
  if 7<=h<=18 and 7<=endhour<=18:
    cost+=d*10
  elif (0<=h<=6 or 19<=h<=23) and (0<=endhour<=6 or 19<=endhour<=23):
    cost+=d*5
  elif h==18 and endhour==19:
    cost+=10*(60-m)+(5*endmin)
  elif h == 6 and endhour==7:
    cost+=5*(60-m)+(10*endmin)
print(cost)