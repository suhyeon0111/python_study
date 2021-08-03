def say_hello1(who):
	print("hello" , who)

say_hello1("suhyeon")

def plus(a,b):
        print(a+b)
plus(2,5)

def minus(a,b):
        print(a-b)

minus(2,5)

def minus2(a, b=0):
    print(a-b)
minus2(2)

def say_hello2(name = "su"):
    print( "hello", name)

say_hello2("suhyeon")

def r_plus(a,b):
    print(a+b)
def p_plus(a,b):
    return a+b

r_result = r_plus(2,3) #none이 나옴
p_result = p_plus(2,3) 

print(r_result,p_result)

def plus2(a,b):
    return a-b
result = plus2(b=30, a=1)
print(result)

def say_hello2(name, age):
    return f"hello {name} you are {age} years old"
    #"hello"+name+"you are"+age+ "years old" 로도 쓸 수 있음
    
hello = say_hello2("suhyeon", "22")
print(hello)

print(3**4)

