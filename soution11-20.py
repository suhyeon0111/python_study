a = str(input())
print(a)

b = float(input())
print(b)

print("정수2개를 입력하라")
c, d= map(int, input().split())
print(c,d)

print("문자2개를 입력하라")
a, b= map(str, input().split())
print(a, b)
 
print("정수 1개를 입력받아 공백을 사이에 두고 3번 출력")
a = input()
print(a,a,a)

print("float 1개를 입력받아 둘째자리까지 출력하기")
a = float(input())
print("%0.2f" %a)

print("시간 입력받아 그대로 출력하기")
h, m = input().split(':')
print(int(h), int (m), sep = ':')

print("주민번호 입력받아 형태 바꿔 출력하기")
a, b = map (str, input().split('-'))
print('%s%s'%a%b)

