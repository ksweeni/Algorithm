N = int(input())
arr = list(map(int,input().split()))
total= 0
score =0
for i in arr :
  if (i ==0) :
    score =0
  else :
    score +=1
    total += score

print(total)