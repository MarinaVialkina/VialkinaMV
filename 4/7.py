n=int(input('n='))
k=1
s=0
pred=1
while k<=n:
    s=s+pred*k
    pred=pred*k
    k+=1
print(s)
