def enter_matrix():
    """Эта функция производит ввод матрицы.
    Возвращает: матрица"""
    matrica=[]
    for i in range(n):
        b=[]
        for j in range(m):
            print('Введите [',i,',',j,'] элемент:')
            b.append(float(input()))
        matrica.append(b)
    return matrica
def max_element():
    """Эта функция находит максимальный элемент матрицы.
    Возвращает: индекс максимального числа по строке и столбцу."""
    maximum=0
    index_maximum=0
    index_stroki_maximum=0
    for i in range(n):
        if max(matrica[i])>maximum:
            maximum=max(matrica[i])
            index_maximum=matrica[i].index(max(matrica[i]))
            index_stroki_maximum=i
    return [index_stroki_maximum, index_maximum]


n=int(input('Ввод числа n(кол-ва строк):'))
m=int(input('Ввод числа m(кол-ва столбцов):'))
matrica=enter_matrix()
print('\n'.join('\t'.join(map(str, row))for row in matrica),'\n')
maximum=max_element()
matrica[0], matrica[maximum[0]] = matrica[maximum[0]], matrica[0]   #Меняет местами строки
for j in range(n):  #Меняет местами столбцы
    matrica[j][0],matrica[j][maximum[1]]=matrica[j][maximum[1]],matrica[j][0]
print('\n'.join('\t'.join(map(str, row))for row in matrica))
