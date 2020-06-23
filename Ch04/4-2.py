"""
date : 2020/06/23
name :  kang
content : 함수 입출력 교재 p168
"""
#입력함수
num = input("숫자입력:")

#출력함수
print('입력한 숫자:',num)

#함수정의
def grade(score):
    if 90< score <=100:
        print('A입니다.')
    elif  80< score <=90:
        print('B입니다.')
    elif 70< score <=80:
        print('C입니다.')
    elif 60< score <=70:
        print('D입니다.')
    else:
        print('F입니다.')

#함수호출
while True:
    score = input('숫자 입력(종료는 0) : ')
    #여기서 입력 받는 숫자는 문자열이기에 숫자로 바꿔줘야한다.
    sc = int(score)
    if sc == 0:
        break
    grade(sc)
print('프로그램이 종료되었습니다.')