answer = 0
max = answer

for i in range(4):
  N = list(map(int, input().split())) 
  answer += N[1] - N[0]
  if(max < answer):
    max = answer

print(max)