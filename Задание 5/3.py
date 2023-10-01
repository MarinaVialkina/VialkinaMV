n=int(input('n:'))
stepen=1
while (2**stepen<n):
    stepen+=1
stepen=stepen-1
print('Показатель степень:',stepen,'Степень:',2**stepen)