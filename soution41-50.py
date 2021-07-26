print("문자 1개를 입력받아 다음문자 출력하기")
a = input()
n = ord(a) #ord함수 : 아스키코드 값 반환
b = chr(n+1) #chr함수: 아스키코드 값을 문자로 반환
print(b)

print("정수2개를 입력받아 나눈 몫 출력하기")
a,b =input().split(' ')
a = int(a)
b = int(b)
c = a/b 
print(c)

print("정수 2개를 입력받아 나눈 나머지 출력하기")
a,b = input().split(' ')
a = int(a)
b = int(b)
c = a%b 
print(c)

print("정수 1개를 입력받아 1 더해 출력하기")
a = int(input())
a += 1
print(a)    

print("정수 2개를 입력받아 자동 계산하기")
a,b =input().split(' ')
a = int(a)
b = int(b) 
print(a+b)
print(a-b)
print(a*b)
print("%0.2f"%(a/b))

print("정수 3개를 입력받아 합과 평균 출력하기")
a,b,c =input().split(' ')
a = int(a)
b = int(b) 
c = int(c) 
print(a+b+c)
print("%0.1f"%(a+b+c/3))

print("정수 1개를 입력받아 2배 곱해 출력하기")
a = int(input())
a *=2
print(a)

print("한 번에 2의 거듭제곱 배로 출력하기")
a, b = map(int, input().split())
print(a<<b)

print("두 정수 입력받아 비교하기1")
a, b =map (int, input().split())
if(a>b):
    print(1)
else:
    print(0)

print("두 정수 입력받아 비교하기2")
a,b = map(int, input().split())
if a==b:
    print(1)
else:
    print(0)