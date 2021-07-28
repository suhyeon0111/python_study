print("16진수 구구단 출력하기")
n = int(input(), 16)
for i in range(1,16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

print("3 6 9 게임의 왕이 되자")
a= int(input())
for i in range(1, a+1):
    if i%3==0:
        print("X", end=' ')
    else:
        print(i, end = ' ')

print("빛 섞어 색 만들기")
a,b,c = map(int, input().split())
for i in range(0,a):
    for j in range(0,b):
        for k in range(b,c):
            print(i, j, k)

print("소리파일 저장용량 계산하기")
h,b,c,s = map(int , input().split())
print('%1f MB' % (h*b*c*s/8/1024/1024))

print("그림파일 저장용량 계산하기")
w,h,b = map(int, input().split())
print('%.2f MB'%(w*h*b/8/1024/1024))

print("거기까지! 이제 그만~")
a = int(input())
i = 1
sum =0
while True :
    sum += i
    i+=1
    if sum>=a:
        print(sum)
        break

print("3의 배수는 통과")
a = int(input())    
for i in range(1,a+1):
    if i%3==0:
        continue
    print(i)

print("수 나열하기1")
a,d,n = map(int, input().split())
for i in range(0,n):
    k = (i*d)+a
print(k)

print("수 나열하기2")
a,r,n = map(int, input().split())
k = a
for i in range(0,n-1):
    k *= r
print(k)

print("수 나열하기3")
a,m,d,n = map(int, input().split())
k = a
for i in range(0, n-1):
    k *= m
    k+=d

print(k)