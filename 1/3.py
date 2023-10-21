age=int(input('Возраст:'))
name=input('Имя:')
if age>0 and age<75 and name!='Иван':
    if age>=16:
        print('Поздравляем, вы поступили во ВГУИТ!')
    else:
         print('Сначала нужно окончить школу.')
         print('Сколько лет осталось учиться в школе?',16-age)
else:
    print('Ошибка.')