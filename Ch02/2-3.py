"""
날짜: 2020/06/20
이름 :강래구
내용 : 리스트 자료형 실습하기 교재 p44
"""

#리스트
ls1 = [1, 2, 3, 4, 5]
print('ls1[0] : ', ls1[0])
print('ls1[1] : ', ls1[1])
print('ls1[2] : ', ls1[2])

ls2 = [1, 3.14, True, '홍길동']
print('ls2[1] : ', ls2[1])
print('ls2[2] : ', ls2[2])
print('ls2[3] : ', ls2[3])

ls3 = [[1,2,3],
       [True,False,True],
       ['Apple','Banana','Grape']]
print('ls3[1] : ',ls3[1])
print('ls3[2] : ',ls3[2])
print('ls3[0][1] : ',ls3[0][1])
print('ls3[2][1] : ',ls3[2][1])

#리스트 더하기
fr1 = ['사과','오렌지']
fr2 = ['바나나','포도','수박']
fr3 = fr1 + fr2
print('fr3 : ', fr3)
print('fr3[3] : ', fr3[3])

#리스트 수정, 변경, 삭제
numbers = [1,2,3,4,5]

numbers[1] = 7
print('numbers : ', numbers)

numbers[2:3] = [8,9]
print('numbers : ', numbers)

numbers[1:3]=[]
print('numbers : ', numbers)

del numbers[1]
print('numbers : ', numbers)

#list 관련 함수 교재p80~84
#list 요소 추가 append
a= [1,2,3]
a.append(4)
print('a = ', a)
a.append([5,6])
print('a = ', a)
#list 정렬 sort
b=[1,4,3,2]
b.sort()
print('b= ', b)
#list 뒤집기 reverse
a=['a','c','d']
a.reverse()
print('a=',a)
#list 위치반환 index
a=[1,2,3]
print('a:' , a.index(3))
#list 요소 삽입 insert
a=[1,2,3]
a.insert(0,4)
print(a)
#list 요소 제거 remove - list에서 첫번째로 나오는 값 제거
a=[1,2,3,3,2,2,2]
a.remove(2)
print(a)
#list

