a=int(input('a='))
b=int(input('b='))
if a>b:
    while a>=b:
        print(a)
        a=a-1
else:
    while a<=b:
        print(a)
        a=a+1