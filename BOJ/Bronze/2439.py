n = int(input())
for i in range(1,n+1):
  star = "*" * i
  print(star.rjust(n)) # 오른쪽 정렬