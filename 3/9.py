def f(k,m,n):
    if k%n!=0 and k%m!=0:
        return 'Нет'
    else:
        if k<=(m*n):
            return 'Да' 
        else:
            return 'Нет'
n=int(input('Размер шоколадки:'))
m=int(input('Размер шоколадки:'))
k=int(input('Необходимо отломить:'))
print(f(k,m,n))