# print("단어 1개 입력받아 그대로 출력하기")
# a = input()
# print(a)

# print("실수 1개 입력받아 부분별로 출력하기")
# a, b = map(str, input().split('.'))
# print('%s%s'%a%b)

# print("문장 1개를 입력받아 그대로 출력하기")
# a = str(input())
# print(a)

# print("정수 1개를 입력받아 나누어 출력하기")
# a = input()
# count = len(a)
# for i in a :
#     count -= 1
#     print([int(i+'0'*count)])

# print("시분초 입력받아 분만 출력하기")
# h, m,s = input().split(':')
# print(int(m))

print("년월일 입력받아 형식 바꿔 출력하기")
y, m, d =str(input().split('.'))
print(d, m, y, sep="-")

print("정수1개를 입력받아 그대로 출력하기2")
a = int(input())
print(a)

print("실수 1개를 입력받아 그대로 출력하기2")
a = float(input())
print("%11f"%a)
