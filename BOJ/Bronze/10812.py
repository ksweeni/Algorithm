n,m = map(int,input().split(' '))
num = [i for i in range(1,n+1)]

for _ in range(m):
  begin, end, mid = map(int,input().split(' '))
  begin -= 1; end -= 1; mid -= 1
  num[begin : end+1] = num[mid : end+1] + num[begin : mid]
print(*num)