import sys
input = sys.stdin.readline
sec = 0
first = int(input())
end = int(input())
c = int(input())
d = int(input())
e = int(input())
if(first <= 0):
  sec += (abs(first)*c) + d + (end*e)
elif(first > 0):
  sec += (end-first)*e
print(sec)