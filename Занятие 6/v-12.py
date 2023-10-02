s=str(input('Ввод:'))
s1=''
for x in range(len(s)):
    if s[x]!=' ':
        s1+=s[x]
    else:
        if s1[-1]=='я':
            print(s1)
            s1=''
        else:
            s1=''