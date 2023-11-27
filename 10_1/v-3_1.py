def enter_matrix():
    """Эта функция производит ввод матрицы."""
    matrica=[]
    for i in range(n):
        b=[]
        for j in range(n):
            b.append(file_vvod.readline())
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
        with open(r'10_1\VialkinaMarinaVladimirovna_Y233_vivod.txt', 'a') as file_vivod:
            file_vivod.write('Матрица симметрична.\n')
    else:
        with open(r'10_1\VialkinaMarinaVladimirovna_Y233_vivod.txt', 'a') as file_vivod:
            file_vivod.write('Матрица несимметрична.\n')


n=int(input('Ввод числа n:'))
k=n**2-n    # Кол-во чисел матрицы, которых не пересекает главная диагональ.
count=0
with open (r'10_1\VialkinaMarinaVladimirovna_Y233_vvod.txt') as file_vvod:
    matrica=enter_matrix()
symmetric(count)
