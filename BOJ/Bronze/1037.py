N = int(input())
b = list(map(int, input().split()))
b = sorted(b)

answer =0
if(N % 2 == 0):
  answer= b[0] * b[len(b)-1]
  
else :
    answer= pow(b[int(len(b)/2)],2)
print(answer)