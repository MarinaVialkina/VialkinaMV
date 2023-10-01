a=int(input('Ввод числа:'))
k=1
s=a
while a!=0:
    a=int(input('Ввод числа:'))
    if a!=0:
        k+=1
        s=s+a
print('Среднее арифметическое',s/k)