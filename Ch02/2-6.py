"""
날짜: 2020/06/20
이름 :강래구
내용 : 집합 자료형 실습하기 교재 p97
"""

#집합 생성하기
set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7,8])

#집합 출력하기 - 리스트,튜플로 변환후에 출력
ls1 = list(set1)
ls2 = tuple(set2)

print('set1 :', ls1)
print('set2 :', ls2)

#교집합
print('set1과 set2 교집합 :', set1 & set2)
#합집합
print('set1과 set2 합집합 :', set1 | set2)
#차집합
print('set1과 set2 차집합 :', set1 - set2)