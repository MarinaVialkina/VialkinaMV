n=int(input('n='))
n1=1
n2=1
k=3
s=2
while k<=n:
    s=s+n1+n2
    xranit=n1
    n1=n2
    n2=xranit+n1
    k+=1
print(s)
