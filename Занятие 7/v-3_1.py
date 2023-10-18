def sum_nechet(n,i,summa):
    while i<=(n-1):
        summa+=D[i]
        i+=2
    return summa


n=int(input('Длина массива:'))
D=[int(input('Элемент массива: ')) for i in range(n)]
summa=0
i=1
summ_itog=sum_nechet(n,i,summa)
print(D, summ_itog)