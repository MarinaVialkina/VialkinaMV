text=str(input('Ввод:'))
text1=''
k=0
for x in range(len(text)):
    if text[x]==':':
        text1=text1+'%'
        k+=1
    else:
        text1=text1+text[x]
print(text1, k)