def delete_point(text, text1,k):
    """Удаляет все точки в строке и подсчитывает их кол-во."""
    for x in range(len(text)):
        if text[x]!='.':
            text1+=text[x]
        else:
            k+=1
    return text1, k


text=str(input('Ввод:'))
text1=''
k=0
text1n,kn=delete_point(text, text1,k)
print(text1n,'Кол-во удалённых точек:', kn)