import sys
input = sys.stdin.readline
fa, fb = list(map(int,input().split(' ')))
max = fa + fb
sub = fa + fb

for i in range(9):
  a, b = list(map(int,input().split(' ')))
  sub = b - a + sub
  if max < sub:
    max = sub

print(max)