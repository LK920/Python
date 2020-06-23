"""
date : 2020/06/23
name :  kang
content : 함수 교재 p150
"""
#함수정의


def f(x):
    y = 2*x+3
    return y

#함수 호출
r1 = f(1)
r2 = f(2)
r3 = f(3)

print('r1:',r1)
print('r2:',r2)
print('r3:',r3)

#함수타입 1 - 매개변수o, 리턴값o

def type1(x,y):
    z = x + y
    return z
#함수타입 2 - 매개변수x, 리턴값o
def type2():
    tot = 0
    for k in range(11):
        tot += k
    return tot
#함수타입 3 - 매개변수o, 리턴값x
def type3(items):
    tot=0
    for i in items:
        tot += i
    print('items 합 :',tot)
#함수타입 4 - 매개변수x, 리턴값x
def type4():
    result = type1(1,2)
    print('result :',result)


res1 = type1(2,2)
print(res1)
res2 = type2()
print(res2)

type3([1,23,4,56])

type4()

