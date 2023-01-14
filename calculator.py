import math 
op=input("enter math perations:")
if op=='sin' or op=='cos' or op=='sqr' or  op=='tan':
    a=float(input("enter number:"))
else:
    a=float(input("enter first number:"))
    b=float(input("enter second number:"))
if op=="+":
    result=(a+b)
elif op=="-":
    result=(a-b)
elif op=="*":
    result=(a*b)
elif op=="/":
    if b==0:
        result("you can not divide by zero")
    else:
        result=(a/b)
elif op=="sin":
    x=(a/180)*3.14
    result=math.sin(x)
elif op=="cos":
    result=math.cos(a)
elif op=="sqrt":
    result=math.sqrt(a)
elif op=="tan":
    x=(a/180)*3.14
    result=math.tan(x)
print(result)