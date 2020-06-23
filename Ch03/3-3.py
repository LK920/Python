"""
date : 2020/06/23
name :  kang
content : for문 교재 p138
"""
#for
#리스트를 이용한 for
nums = [1,2,3,4,5]
for n in nums:
    print("n :",n)

for a in ['tiger','lion','eagle','bear']:
    print("a :" ,a)

#튜플을 이용한 for
for n in (4,2,1.23,4,5,12,3):
    print("n :", n)

#range 함수를 이용한 for
for num in range(5):
    print("num :", num)

for num in range(1,10):
    print("num :", num)

for v in range(1,10):
    print("v :", v)
#1부터 10까지 합
som = 0
for k in range(1,11):
    som += k
print("1부터 10까지의 합" ,som)
#1부터 10까지 짝수합
tot = 0
for k in range(1,11):
    if k %2 == 0:
        tot += k
print("1부터 10까지의 짝수합 :", tot)
#이중 for
for a in range(0,3):
    print("a:",a)
    for b in range(0,5):
        print('b :',b)
#구구단
for k in range(2,11):
    print(k,"단 출력")
    for a in range(1,10):
        print("%d x %d = %d" %(k,a,k*a))

#별삼각형
for a in range(0,10):
    for b in range(0,a+1):
        print('☆', end='')
    print()

for n in range(1,11):
    print('★'*n)

for c in range(10,0,-1):
    print('☆'*c)
