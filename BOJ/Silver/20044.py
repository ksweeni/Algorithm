n = int(input())
li = list(map(int, input().split(' ')))
li.sort()
res=[]

while(len(li)!=0):
  res.append(li.pop(0)+li.pop())
print(min(res), end="")