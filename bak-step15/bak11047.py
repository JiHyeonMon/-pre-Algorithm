#11047
#동전 0

N, price = map(int, input().split())
cnt = 0
i = 0
total_cnt = 0
money = []
for i in range(N):
     money.append(int(input()))

while price>0:
     print(i, money[i], cnt)
     if price > money[i]:
          i+=1
     else:
          if price > money[i-1]*(cnt+1):
               cnt+=1
          else:
               total_cnt += cnt
               price-=money[i-1]*cnt
               cnt = 0
               i = 0

print(total_cnt)
