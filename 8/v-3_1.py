def gipoten(k1,k2,gip):
    """Эта функция находит гопотенузу по двум катетам."""
    gip=(k1**2+k2**2)**(1/2)
    return gip

gip=0
gip1=gipoten(int(input('Первый катет:')),int(input('Второй катет:')),gip)
gip2=gipoten(int(input('Первый катет:')),int(input('Второй катет:')),gip)
print('Большая гопотенуза:',max(gip1,gip2),'\nМеньшая гипотенуза:',min(gip1,gip2))