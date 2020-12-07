#1003
#피보나치 함수

def fibonacci(n) :
     num = []
     if n == 0 :
          num.append(0)
     elif n == 1:
          num.append(1)
     else:
          return fibonacci(n-1) + fibonacci(n-2)
     return num

for i in range(int(input())):
     num = fibonacci(int(input()))
     print("{} {}".format(num.count(0), num.count(1)))
