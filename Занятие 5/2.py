def f(n,d):
    while (n%d!=0):
        d+=1

n=int(input('Ввод n>=2:'))
d=2
f(n,d)
print(d)