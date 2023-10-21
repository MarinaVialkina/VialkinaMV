def f(a,k,s):
    while a!=0:
        a=int(input('Ввод числа:'))
        if a!=0:
            k+=1
            s=s+a
    return s, k


a=int(input('Ввод числа:'))
k=1
s=a
s1,k1=f(a,k,s)
print('Среднее арифметическое',s1/k1)