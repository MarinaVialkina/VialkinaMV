def f(n,stepen):
    while ((2**stepen)<=n):
        stepen=stepen+1
    return stepen
    


n=int(input('n:'))
stepen=1
stepenn=f(n,stepen)
stepenn=stepenn-1
print('Показатель степень:',stepenn,'Степень:',2**stepenn)