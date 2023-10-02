s=str(input('Ввод:'))
if '  ' in s:
    print('Допущена пунктуационная ошибка!')
else:
    print('Кол-во слов:',s.count(' ')+s.count('.'))