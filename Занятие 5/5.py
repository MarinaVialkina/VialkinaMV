def f(chislo,s):
    while chislo!=0:
        chislo=int(input('Ввод числа:'))
        s+=1
    return s


chislo=int(input('Ввод числа:'))
s=0
s1=f(chislo,s)
print(s1)