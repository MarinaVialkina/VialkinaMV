def f(a,b,n,l):
    return a+(2*b+2*a)*(n-1)+2*l
a=int(input('Расстояние между рядами:'))
b=int(input('Расстояние между дырочками:'))
n=int(input('Количество дырочек в ряду:'))
l=int(input('Длина свободного конца:'))
print('Длина шнурка',f(a,b,n,l))