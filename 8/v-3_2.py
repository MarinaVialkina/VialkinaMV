def sort_slov(kolvo_slov, index_probela, stroka, stroka_new):
    """Функция сортрует каждое слово строки отдельно по алфавиту """
    for i in range (kolvo_slov):
        index_probela=stroka.find(' ')
        slovo=''.join(sorted(stroka[:index_probela]))
        stroka_new=stroka_new+str(slovo)+' '
        stroka=stroka[(index_probela+1):]
    return(stroka_new)


stroka=str(input('Ввод строки:'))+' '
stroka_new=''
kolvo_slov=stroka.count(' ')+1
slovo=''
index_probela=stroka.find(' ')
stroka_new=sort_slov(kolvo_slov, index_probela, stroka, stroka_new)
print(stroka_new)


