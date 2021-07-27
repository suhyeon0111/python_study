# print("0입력될 때까지 무한 출력하기")
# a = 1
# while a!=0:
#     a = int(input())
#     print(a)

# print("정수 1개 입력받아 카운트다운 출력하기1")
# a = int(input())
# while a != 0:
#     print(a)
#     a-=1

# print("정수 1개 입력받아 카운트다운 출력하기2")
# a =int(input()) 
# while a !=0:
#     a-=1
#     print(a)

# print("문자1개 입력받아 알파벳 출력하기")
# a = ord(input())
# t = ord('a')
# while t<=a:
#     print(chr(t),end=' ')
#     t +=1

# print("정수 1개 입력받아 그 수까지 출력하기1")
# a = int(input())
# i =0
# while i<=a:
#     print(i)
#     i+=1
# print("정수 1개 입력받아 그 수까지 출력하기2")
# a = int(input())
# for i in range(0,a+1):
#     print(i)    

# print("짝수 합 구하기")
# a = int(input())
# i =0
# sum=0
# while i<=a:
#     if(i%2==0):
#         sum += i
#     i+=1
# print(sum)

# print("원하는 문자가 입력될 때까지 반복 출력하기")
# a=0
# while a != 'q':
#     a = input() 
#     print(a)

# print("언제까지 더해야할까")
# a = int(input())
# sum=0
# i = 1
# while a>sum:
#     i+=1
#     sum+=i
# print(i-1)

print("주사위 2개 던지기")
a ,b=map(int, input().split())

for i in range(1,a+1):
    for j in range(1,b+1):
        print(i, j)





