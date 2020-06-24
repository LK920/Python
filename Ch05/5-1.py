"""
날짜: 2020/06/24
이름 :강래구
내용 : 클래스  교재 p183
"""


#객체생성
from Ch05.sub1.Account import Account
from Ch05.sub2.Smartphone import Smartphone

kb = Account('국민은행','101-11-1153-1532','김유신',10000)
wb = Account('우리은행','101-1153-1532-01','김춘추',20000)

kb.deposit(30000)
kb.withdraw(15000)
kb.show()

wb.deposit(10000)
wb.withdraw(5000)
wb.show()

#클래스 상속
iphone = Smartphone('A7','4GB','128GB','아이폰7','010-2688-8888')
iphone.call()
iphone.calc()
iphone.internet()
iphone.show()

