n = int(input())
front = (n%10)*10
back = (n//10)+(n%10)
newnum = front+(back%10)
cnt = 1;

while(newnum != n):
  front = (newnum%10)*10
  back = ((newnum//10)+(newnum%10))
  newnum = front+(back%10)
  cnt+=1

print(cnt)