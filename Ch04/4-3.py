"""
date : 2020/06/23
name :  kang
content : 파일 읽고 쓰기 교재 p171
"""
#파일 읽기 - 역슬러시 슬러시로 바꿔줘야함
file = open('C:/Users/bigdata/Desktop/testtest.txt')
line = file.readline()

print('line',line)

file.close() #파일닫기

#여러줄 파일 읽기
file = open('C:/Users/bigdata/Desktop/testtest.txt', 'r')

while True:
	line = file.read()

	if not line : #라인이 없으면
		break

	print('line :',line)
file.close()

#파일쓰기
sample = open('C:/Users/bigdata/Desktop/sample.txt', 'w')
sample.write('안녕하세요.\n')
sample.write('반갑습니다.\n')
sample.write('안녕히가세요.\n')
sample.close()

#구구단 파일 생성하기
gugudan = open('C:/Users/bigdata/Desktop/gugudan.txt', 'w')
for a in range(2,10):
	gugudan.write('%d단\n' %a)
	for b in range(1,10):
		gugudan.write('%d x %d = %d\n' %(a,b,a*b))
gugudan.close()

#with문(자동으로 파일을 close실행)을 이용한 파일 입출력
with open('C:/Users/bigdata/Desktop/star.txt', 'w') as star:
	for i in range(1,11):
		star.write('☆'*1)
		star.write('\n')