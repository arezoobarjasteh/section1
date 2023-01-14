a=float(input('vazn'))
b=float(input('ghad'))
bmi=a/(b*b)
if bmi<18.5 :
    print('unde wehight')
if 18.5<=bmi<=24.9:
    print('normal')    
if 25<=bmi<=29.9:
    print('overweitgh')
if 30<=bmi:
    print('obes')
if 35<bmi:
        print ('extremly' 'obes')
