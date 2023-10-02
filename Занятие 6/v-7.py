s=str(input('Ввод:'))
s1=''
for x in range(len(s)//2):
    if s[x]=='п':
        s=s.replace('п','*',1)
print(s)

