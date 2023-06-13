import sys
input = sys.stdin.readline
for _ in range(int(input())):
  money = int(input())
  a = money//25
  money %= 25
  b = money//10
  money %= 10
  c = money//5
  money %= 5
  print(a,b,c,money)