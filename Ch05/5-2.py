"""
날짜: 2020/06/24
이름 :강래구
내용 : 모듈  교재 p207
"""
#모듈은 from없이 import만 클래스는 from하고 import 두개다 사용
import Ch05.sub1.calc as Calc
if __name__=="__main__": #파이썬의 엔트리 포인트
    #모듈(파이썬 패키지에 있는 소스파일) 함수 호출
    rs1 = Calc.plus(1, 2)
    rs2 = Calc.minus(1, 2)
    rs3 = Calc.multi(2, 3)
    rs4 = Calc.div(4, 2)

    print('rs1 :',rs1)
    print('rs2 :',rs2)
    print('rs3 :',rs3)
    print('rs4 :',rs4)

#