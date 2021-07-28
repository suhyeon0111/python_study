print("수 나열하기3")
a,m,d,n = map(int, input().split())
k = a
for i in range(0, n-1):
    k *= m
    k+=d

print(k)

print("함께 문제 푸는 날")
a,b,c = map(int, input().split())
day=1
while day%a!=0 or day%b!=0 or day%c!=0 :
    day+=1
print(day)

print("이상한 출석 번호 부르기1")
a = int(input())
b = map(int, input().split())
b_list = list(b)
arr = []
#모든 배열에 0을 넣어주기
for i in range(24):
    arr.append(0)
#이름 불린 횟수 기록
for i in range(b):
    arr[b_list[i]] +=1
#결과 출력
for i in range(1,24):
    print(arr[i], end='')

print("이상한 출석 번호 부르기2")
a = int(input())
b = list(map(int, input().split()))
b.reverse()
for i in range(a):
    print(b[i], end = ' ')
  
print("이상한 출석 번호 부르기3")
a = int(input())
b = list(map(int, input().split()))
b.sort()
print(b[0])


#리스트 공부한 후에 도전

print("바둑판에 흰 돌 놓기")

print("바둑알 십자 뒤집기")

print("설탕과자뽑기")

print("성실한 개미")
