num = int(input())
dot = 0
for i in range (num+1):
    for j in range(i+1):
        dot += i+j      
print(dot)