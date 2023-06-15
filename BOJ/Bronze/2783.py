import sys
input = sys.stdin.readline

seven = list(map(int, input().split()))
min = seven[0]*1000/seven[1]

for _ in range(int(input())):
  food = list(map(int, input().split()))
  if((food[0]*1000/food[1]) < min):
    min = food[0]*1000/food[1]
print('%.2f' % min)