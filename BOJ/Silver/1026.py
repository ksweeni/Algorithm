n=int(input())
a=[]
b=[]
answer = 0 
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = sorted(b)
a = sorted(a, reverse=True)


for i in range(n):
  answer += a[i]*b[i]

print(answer)