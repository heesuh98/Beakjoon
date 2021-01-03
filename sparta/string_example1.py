#문자열 연습하기
"life is too shor, you need Python"

"A"
#백슬래시를 이용하면 작은따옴표가 문자열이 둘러싸는 의미가 아니라 그 자체를 뜻한다.
food = 'hello. I\'m heeseo'

print(food)

#줄을 바꾸기 위해서는 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

print(multiline)

#줄바꿈을 위해 작은따옴표 3개 또는 큰따옴표 3개를 사용한다.
multilie2 = '''
Life is too short
You need python
'''
print(multilie2)

#문자열 연산하기
##문자열 더해서 연결하기(concatenation)

head = "python"
tail = "is fun!"
print(head + tail)

print(head*2)

#문자열 곱하기 응용
print("="*50)
print("My program")
print("=" * 50)

#문자열 길이 구하기
##len함수 사용
a = "Life is too short"
print(len(a))

#문자열 인덱싱: 첫번째 자리는 0, 바로 다음은 1 이렇게 번호 붙인다.
##대괄호를 이용한다.
print(a[3])

#문자열 인덱싱 활용
print(a[0])
print(a[12])
print(a[-1]) #-1의 경우 뒤에서부터 첫번째 문자이다.

#문자열 슬라이싱
b=a[0] +a[1] + a[2]+ a[3]
print(b)

print(a[0:4]) #a[시작번호:끝번호] 이때 끝번호는 포함안함. 바로 그앞까지 나타냄.

print(a[3:6])

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date =a[:8]
weather = a[8:]
print(date)
print(weather)


#숫자 바로 대입 : %d 이용한다. 문자도 대입 가능.
print("I eat %d apples." %3)

#format 함수를 이용한 포매팅
print("I eat {0} apples".format(3))

#2개이상 값 넣기
number = 10
day = "three"
print("I ate {0} apple. so I was sick for {1} days." .format(number, day))

#count 함수:문자 개수 세기
a = "hobby"
print(a.count('b'))
#find 함수: 위치를 알려준다.(맨처음은 0부터 시작)
print(a.find('y'))

#index 함수: 위치 알려주기. 문자열중에 찾는 문자가 맨 처음 나온 위치를 반환
print(a.index('b'))

#join 함수: 문자열 삽입
print(",".join('abcd'))

#upper:소문자를 대문자로 바꾸기
d = 'hi'
print(d.upper())

#lower:대문자를 소문자로 바꾸기
c = 'APPLE'
print(c.lower())

#strip: 양쪽공백 지우기
b = " hi "
print(b.strip())

#replace:문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Yor leg"))

#split:문자열 나누기
print(a.split())
b = "a:b:c:d"
print(b.split(':'))

#리스트 자료형
#리스트를 이용하면 간단히 표현 가능하다.
#리스트를 만들 때는 대괄호로 감싸주고 쉼표로 구분한다.
#리스트명=[요소1,요소2,...]

