for _ in range(int(input())):
  n = int(input())
  li = sorted((map(int, input().split(' '))))
  print((li[-1]-li[0])*2)