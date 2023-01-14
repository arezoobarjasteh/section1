n=input('enter your name:')
f=input('eter your family:')
a=float(input("enter your 1 lesson"))
b=float(input("enter your 2 lesson"))
c=float(input("enter your 3 lesson"))
sum=a+b+c
ave=sum/3
if ave>=17:
    print (n , f , "great")


elif 17> ave and ave>=12:
    print (n , f, "normal")


elif ave < 12:
    print(n , f , "fail")