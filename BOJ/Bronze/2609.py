import math

a,b = list(map(int, input().split()))
gcd = math.gcd(a,b)
lcm = int(a*b / gcd)

print(gcd)
print(lcm)