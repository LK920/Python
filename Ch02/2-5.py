"""
날짜: 2020/06/20
이름 :강래구
내용 : dictionary 자료형 실습하기 교재 p88
"""
#dictionary는 자바스크립트에 json이다//자바에선 map
dic1 = {1: 'python', 2:'Java', 3:'C', 4:'C++'}
dic2 ={
    'kor': '대한민국',
    'usa': '미국',
    'chi': '중국',
    'jpn': '일본',
    'spn': '스페인',
    'tai': '대만'
}
dic3 = {
    101:[1,2,3,4,5], #리스트
    102:('서울','대전','대구','부산','광주'), #튜플
    103:{'p1':'김유신','p2':'강감찬','p3':'이순신'}, #dictionary
}
#dictionary 출력
print('dic1 :', dic1)
print('dic2 :', dic2)
print('dic3 :', dic3)

print('dic1[1] :', dic1[1])
print("dic2['kor'] :", dic2['kor'])
print("dic3[102] :", dic3[102])
print("dic3[102][1] :", dic3[102][1])
print("dic3[103] :", dic3[103])
print("dic3[103]['p3'] :", dic3[103]['p3'])

#dictionary 값 추가
dic1[5] = 'R'
print('dic1 :', dic1)

dic2['aus'] = '호주'
print('dic2 :', dic2)

#dcitionary 값 제거
del dic1[3]
print('dic1: ', dic1)

#dictionary 관련 함수 교재 p93 - 96