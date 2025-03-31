age=18
if age<20:
    print('청소년 할인')
print('입장을 환영합니다')


age=24
if age<20:
    print('청소년 할인')
print('입장을 환영합니다')

age=18
if age<20:
    print('나이',age)
    print('청소년 확인')
    print('청소년 할인')

age=24
if age<20:
    print('나이',age)
    print('청소년 확인')
    print('청소년 할인')

num=100

if num<0:
    print(num,'은(는) 음수입니다')
else:
    print(num,'은(는) 음수가 아닙니다')

    if num%2==0:
        print(num,'은(는) 짝수입니다')
    else:
        print(num,'은(는) 홀수입니다')

for i in range(2,10):
    for j in range(1,10):
        print('%d*%d=%d'%(i,j,i*j),end=' ')
    print()

n=-1
while n<=0:
    n=int(input('합계를 구할 양의 정수를 입력하세요: '))

s=0
for i in range(1,n+1):
    s=s+i

print('1부터 %d까지의 합은 %d' %(n,s))

st='Programming'

for ch in st:
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)

print('The end')

st='Programming'

for ch in st:
    if ch in ['a','e','i','o','u']:
        break
    print(ch)

print('The end')