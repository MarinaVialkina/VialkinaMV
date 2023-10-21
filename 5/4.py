def f(x,y,dni):
    """Функция определяет номер дня, в который пробег спортсмена составит не менее y километров."""
    while (x<y):
        x=x*1.1
        dni+=1
    return dni


x=float(input('Сколько пробежал за 1 день?'))
y=float(input('y='))
dni=1
dnin=f(x,y,dni)
print(dnin)