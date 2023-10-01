a=int(input('Ввод числа:'))
pr=a
k=0
while a!=0:
    a=int(input('Ввод числа:'))
    if a>pr:
        k+=1
    pr=a
print(k)