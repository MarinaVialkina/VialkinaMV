s=str(input('Ввод:'))
s1=''
skob=0
for x in range(len(s)):
    if s[x-1]=='(':
        skob=1
    elif s[x]==')':
        skob=0
    if skob==1:
        s1+=s[x]
print(s1)