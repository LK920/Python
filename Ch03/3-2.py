"""
date : 2020/06/23
name :  kang
content : while문 교재 p136
"""
#while
num = 1
while num < 5:
    print('num이 5보다 크다.')
    num = num + 1
#1부터 10까지 합
tot = 0
start = 1
while start <= 10:
    tot += start
    start = start + 1
print('1부터 10까지의 합:',tot)

#리스트 합
scores = [80,90,92,78,62]
tot = i = 0
while i < len(scores) :
    tot += scores[i]
    i += 1
print('리스트 scores 전체합', tot)

#break

num = 1
while True:
    if num % 5 == 0 and num % 7 == 0 :
        break
    num += 1
print('5와 7의 최소공배수', num)

#continue
sum = 0
k = 0
while k <= 10:

    k += 1
    if k%2 == 1:
        continue
    sum += k
print('1부터 10까지 짝수합 :',sum)