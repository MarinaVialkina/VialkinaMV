def f(x):
    if (x%4==0 and x%100!=0) or (x%400==0):
        return 'Да'
    else:
        return 'Нет'
x=int(input('Ввод номера года:'))
print(f(x))