s=str(input('Ввод:'))
s1=''
while s!='':
    s1=s[:s.find(' ')]
    if s1[0]=='а' or s1[0]=='А':
        print(s1)
        s1=''
        s=s[s.find(' ')+1:]
        print(s)
    else:
        s=s[s.find(' ')+1:]