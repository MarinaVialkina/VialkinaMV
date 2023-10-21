def f(massiv):
    """Эта фукция заменяет все числа в масиве меньше 15 на из удвоенные значения."""
    for i in range(len(massiv)):
        if massiv[i]<15:
            massiv[i]=massiv[i]*2
    return massiv


massiv=[int(input('Элемент массива:'))for i in range(8)]
massiv_new=f(massiv)
print(massiv_new)