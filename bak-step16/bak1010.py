#3036
#링
def gcd(a, b):
     if a%b == 0:
          return b
     else:
          return gcd(a, a%b)

n = int(input())
num = list(map(int, input().split()))
a = num[0]

for i in range(1, n):
     k = gcd(a, num[i])
     print(str(a//k)+"/"+str(num[i]//k))
