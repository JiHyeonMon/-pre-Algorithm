#1011
#Fly me to the Alpha Centauri

for i in range(int(input())):
     s, e =map(int, input().split())
     end= e-s
     print(end)
     go = 1
     answer=0
     while end>0:
          if end-go*2<0:
               if end-go<0:
                    break
               else:
                    answer+=1
                    break
          else:
               end-=go*2
               go+=1
               answer+=2

     print(answer)
