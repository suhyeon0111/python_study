print("비트단위로 OR하여 출력하기")
a,b = map(int, input().split()) 
print(a|b)

print("비트단위 XOR하여 출력하기")  
a,b = map(int, input().split()  )
print(a^b)

print("두 정수 입력받아 큰 수 출력하기")
a,b = map(int, input().split())
if a>b:
    print(a)
else:
    print(b)

print("정수 3개 입력받아 가장 작은 수 출력하기")
a,b,c = map(int, input().split())
if(a<b):
    if a<c:
        print(a)
    else:
        print(c)
if a>b:
    if b<c:
        print(b)
    else:
        print(c)

print("정수 3개 입력받아 짝수만 출력하기")
a,b,c = map(int, input().split())
if a %2==0:
    print(a)
if b%2==0:
    print(b)    
if c%2==0:
    print(c)

print("정수 3개 입력받아 짝/홀 출력하기")
a,b,c = map(int, input().split())
if(a%2==0):
    print("even")
else:
    print("odd")
if(b%2==0):
    print("even")
else:
    print("odd")
if(c%2==0):
    print("even")
else:
    print("odd")
print("정수1개 입력받아 분류하기")
a = int(input())
if a<0 :
    if a%2==0:
        print("A")
    else:
        print("B")
else:
    if a%2==0:
        print("C")
    else:
        print("D")


print("정수 1개 입력받아 평가출력하기")
a = int(input())

if 89<a:
    print("A")
else:
    if 69<a:
        print("B")
    else:
        if 39<a:
            print("C")
        else:
            print("D")
            
print("평가 입력받아 다르게 출력하기")
a = input()
if a == 'A':
    print("best!!!")
elif a == 'B':
    print("good!!!")
elif a =='C':
    print("run!")
elif a=='D':
    print("slowly~")
else:
    print("what?")

print("월 입력받아 계절 출력하기")
a = int(input())
if a//3==0:
    print("spring")
if a//3==1:
    print("summer")
if a//3==2:
    print("fall")
else:
    print("winter")


