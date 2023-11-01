def enter_matrix():
    matrica=[]
    for i in range(n):
        b=[]
        for j in range(m):
            print('Введите [',i,',',j,'] элемент:')
            b.append(float(input()))
        matrica.append(b)
    return matrica
def max_element():
    maximum=0
    index_maximum=0
    index_stroki_maximum=0
    for i in range(n):
        if max(matrica[i])>maximum:
            maximum=max(matrica[i])
            index_maximum=matrica[i].index(max(matrica[i]))
            index_stroki_maximum=i
    #print(index_stroki_maximum)
    #print(index_maximum)
    return [index_stroki_maximum, index_maximum]



n=int(input('Ввод числа n(кол-ва строк):'))
m=int(input('Ввод числа m(кол-ва столбцов):'))
matrica=enter_matrix()
print('\n'.join('\t'.join(map(str, row))for row in matrica),'\n')
maximum=max_element()
matrica[0], matrica[maximum[0]] = matrica[maximum[0]], matrica[0]
for j in range(n):
    matrica[j][0],matrica[j][maximum[1]]=matrica[j][maximum[1]],matrica[j][0]
print('\n'.join('\t'.join(map(str, row))for row in matrica))
