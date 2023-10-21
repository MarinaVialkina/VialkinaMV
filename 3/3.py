n=int(input('n='))
if n>1440:
    n=n%1440
print(n//60,':',n%60)