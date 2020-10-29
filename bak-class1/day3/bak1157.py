#1157
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

a = input()
a = a.lower()

cnt = []
for i in range(0, len(a)):
    if a[i] not in cnt:
        cnt.append(a[i])
    else:
        a.index(a[i])


'''
모든 문자를 대문자든 소문자든 변환하여 같은 문자 찾는 방법으로 구함.
'''

