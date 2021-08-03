def plus(a,b):
    return  int(a)+int(b)

def minus(a,b):
    return int(a)- int(b)

def mult(a,b):
    return int(a)*int(b)

def div(a,b):
    return int(a)/int(b)

def remain(a,b):
    return int(a)%int(b)    

def negated(a):
    return -int(a)  

def unchange(a):
    return int(a)

def power(a,b):
    return int(a)**int(b)

result = plus("2",3)
print(result)
result = minus("2","10")
print(result)
result = mult("2",3)
print(result)
result = div("2",3)
print(result)
result = negated("5")
print(result)
result = unchange("5")
print(result)
result = power("2",3)
print(result)



