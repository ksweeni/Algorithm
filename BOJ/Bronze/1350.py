import math

n = int(input())
answer = 0
num = list(map(int,input().split(' ')))
size = int(input())
while(len(num)!=0):
  answer+=math.ceil(num.pop(0)/size)*size
print(answer)