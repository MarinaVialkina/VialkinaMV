n=int(input('Кол-во чисел из ряда Фибоначи:'))
k=int(input('Порядковый номер вряду, с которого нужно начинать:'))
stat=3
pr1=1
pr2=1

if (k>2) or (k==0):
    s=0
elif (k==1):
    s=2
else:
    s=1
while stat<=(k+n-1):
    if stat<k:
        stat+=1
        xranit=pr1
        pr1=pr2
        pr2=xranit+pr1

    else:                  ##s>=k
        s=s+pr1+pr2
        stat+=1
        xranit=pr1
        pr1=pr2
        pr2=xranit+pr1 

print(s)
