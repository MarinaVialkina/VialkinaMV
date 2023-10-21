def f(a,b,max,k):
    while a!=0:
        a=int(input('Ввод числа:'))
        if a==b:
            k+=1
            if k>max:
                max=k
        else:
            k=1
        b=a
    return max
a=int(input('Ввод числа:'))
b=a
k=1
max=0
maxn=f(a,b,max,k)
print(maxn)