text=str(input('Ввод:'))
k=0
for x in range(len(text)+1):
    if x==0:
        if text[x]=='Е':
            k+=1
    else:
        if ((text[x]=='е' or text[x]=='Е') and text[x-1]==' '):
            k+=1
print(k)