#1339
#단어 수학

word = []
alpha = {}
k = 9
answer =[]
for i in range(int(input())):
     word.append(list(input()))

word.sort(key=len, reverse=True)

for i in range(len(word)):
     for j in range(len(word[i])):
          if word[i][j] not in alpha:
               alpha[word[i][j]] = k
               k-=1
               
for i in range(len(word)):
     tmp=0
     for j in range(len(word[i])):
          tmp += alpha[word[i][j]] * 10**(len(word[i])-j-1)
     answer.append(tmp)
     
print(alpha)
print(sum(answer))
