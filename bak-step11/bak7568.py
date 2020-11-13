#7568
#덩치

n = int(input())
dungchi = []
answer = [0 for i in range(n)]
cnt = 1

for i in range(n):
     w, h = map(int, input().split())
     dungchi.append([w,h])

while n>0:
     for i in range(len(dungchi)):
          if dungchi[i][0] == max(dungchi)[0]:
               if dungchi[i][1] == max(dungchi, key=lambda x: x[1])[1]:
                    print(i)
                    answer[i] = cnt
                    cnt+=1
                    dungchi[i] = [0,0]
               else:
                    answer[i] = cnt
                    dungchi[i][0] = 0
               continue
               
     n-=1

print(answer)
