"""
날짜: 2020/06/24
이름 :강래구
내용 : 외장함수  교재 p262
"""
import time
import calendar as cal
import math
import random as rand

#time
r1 = time.time()
print('r1:',r1)

r2 = time.ctime()
print('r2',r2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
print('%s년 %s월 %s일' % (year, month, date))

for i in range(2):
    print('i :', i)
    time.sleep(1) #스레드를 1초 동안 sleep

#calendar
r3 = cal.calendar(2020)
print('r3:', r3)
r4 = cal.weekday(2020,7,16)
print('r4:', r4)

#math
r5 = math.ceil(1.2)
r6 = math.floor(1.8)
r7 = math.sqrt(9)
r8 = math.factorial(5)
r9 = round(1.6)
print('r5:',r5)
print('r6:',r6)
print('r7:',r7)
print('r8:',r8)
print('r9:',r9)

#random()
rs1 = rand.random() #0-1사이 실수
print('rs1:', rs1)
rs2 = rs1*10 #0-10사이의 실수
print('rs2:', rs2)

rs3 = math.ceil(rs2)#1에서 10사이의 정수
print('rs3:', rs3)
