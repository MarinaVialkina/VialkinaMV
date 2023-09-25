def f (a,b,c):
    if a!=b and a!=c and b!=c:
        return '0'
    elif a==b and a==c and b==c:
        return '3'
    else:
        return '2'
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(f(a,b,c))        