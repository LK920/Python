class Account:
    #멤버 변수 init(생성자)
    def __init__(self,bank,id,name,money):
        self.bank = bank
        self.id =id
        self.name =name
        self.money =money

    #멤버 변수
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money
    def show(self):
        print('---------------')
        print('은행명 :', self.bank)
        print('계좌번호:',self.id)
        print('입금주:',self.name)
        print('현재잔액:',self.money)
        print('---------------')
