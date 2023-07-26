li = list(map(int, input().split(' ')))
for i in range(1,max(li)+1):
  if int(li[0]%i) == 0 and int(li[1]%i)== 0:
    print(i, li[0]//i, li[1]//i)