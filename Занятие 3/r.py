def f(x,y):
    if x%2==y%2:
        return 'ч'
    else:
        return 'б'
if f(int(input('Номер столбца(1-8):')),int(input('Номер строки(1-8):')))==f(int(input('Номер столбца(1-8):')),int(input('Номер строки(1-8):'))):
    print('Да')
else:
    print('Нет')