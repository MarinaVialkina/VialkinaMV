def enter_matrix():
    """Эта функция производит ввод матрицы."""
    matrica=[]
    for i in range(n):
        b=[]
        for j in range(n):
            print('Введите [',i,',',j,'] элемент:')
            b.append(int(input()))
        matrica.append(b)
    return matrica
def symmetric(count):
    """Эта функция определяет симметричность матрицы."""
    for stolb in range(n):
        for strok in range(n):
            if stolb==strok:
                continue
            if matrica[stolb][strok]==matrica[strok][stolb]:
                count+=1
    if count==k:
        print('Матрица симметрична.')
    else:
        print('Матрица несимметрична.')


n=int(input('Ввод числа n:'))
k=n**2-n    # Кол-во чисел матрицы, которых не пересекает главная диагональ.
count=0
matrica=enter_matrix()
symmetric(count)