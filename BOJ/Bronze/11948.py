import sys
input = sys.stdin.readline

N = []
S = []
for i in range(4):
  N.append(int(input()))
for i in range(2):
  S.append(int(input()))

N = sorted(N)
print(max(S)+N[3]+N[2]+N[1])