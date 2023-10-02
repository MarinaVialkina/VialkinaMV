text=str(input('Ввод:'))
text1=''
k=0
for x in range(len(text)):
    if text[x]!='а':
        text1+=text[x]
    else:
        k+=1
print(text1, k)