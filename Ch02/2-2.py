"""
날짜: 2020/06/20
이름 :강래구
내용 : 문자열 자료형 실습하기 교재 p44
"""
#문자열 더하기
str1 = 'hello'
str2 = 'python'
str3 = str1 + str2
print('str1+str2 :', str3)
#문자열 곱하기
str = "python "
print('str*5 :',str*5)
#문자열 길이
hello = 'hello world'
print('hello : ', len(hello))
#문자열 인덱스
print('hello[6]', hello[6])
print('hello[8]', hello[8])
#문자열 슬라이스
print('hellow[1:7] ', hello[1:7])
print('hellow[3:7] ', hello[3:7])
print('hellow[:7] ', hello[:7])
print('hellow[7:] ', hello[7:])
print('hellow[-2:] ', hello[-2:])
print('hellow[:-1] ', hello[:-1])
#문자열 분리
animal = '사자, 호랑이, 코끼리,기린'
a1,a2,a3,a4 = animal.split(',')
print('a1 :', a1)
print('a2 :', a2)
print('a3 :', a3)
print('a4 :', a4)

#문자열 포멧
fm1 = '오늘은 %d월 입니다.'
fm2 = '오늘은 %d월 %d일 입니다.'
fm3 = '오늘은 %s월 입니다.'
fm4 = '오늘은 %s년 %d월 %d일 %s요일 입니다.'

print(fm1 % 6)
print(fm2 % (6,22))
print(fm3 % '06')
print(fm4 % ('2020', 6,22,'월'))

# 문자열 관련 함수 교재 p67 ~ p71


