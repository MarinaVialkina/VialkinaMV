def f(a,pr,k):
    while a!=0:
        a=int(input('Ввод числа:'))
        if a>pr:
            k+=1
        pr=a
    return k
a=int(input('Ввод числа:'))
pr=a
k=0
k1=f(a,pr,k)
print(k1)