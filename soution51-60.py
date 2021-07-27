print("두 정수 입력받아 비교하기3")
a, b = map(int, input().split())
if a<b:
    print(1)    
else:
    print(0)    
print("두 정수 입력받아 비교하기4")
a,b = map(int, input().split())
if a != b:
    print(1)    
else:
    print(0)    

print("참 거짓 바꾸기")
a = int(input())
if a==1:
    print(0)    
else:
    print(1)    

print("둘 다 참일 경우만 참 출력하기")
a, b = map(int, input().split())
if a==1 and b==1:
    print(1)    
else:
    print(0)    
    
print("하나라도 참이면 참 출력하기")
a,b = map(int, input().split())
if a==1 or b ==1:
    print(1)    
else:
    print(0)

print("참/거짓이 서로 다를 때에만 참 출력하기")
a,b = map(int, input().split())
print(a^b)

print("참/거짓이 서로 같을 때에만 참 출력하기")
a,b = map(int, input().split())
print(a&b)

print("둘 다 거짓일 경우만 참 출력하기")
a, b = map(int, input().split())
print(not a and not b)  

print("비트단위로 NOT하여 출력하기")
a = int(input())
print(~a)

print("비트단위로 AND하여 출력하기")
a,b = map(int, input().split())
print(a&b)  
