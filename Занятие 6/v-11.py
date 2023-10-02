s=str(input('Ввод:'))
sum=0
max=0
for x in range(len(s)):
    if s[x]=='!':
        s=s.replace('!','.', 1)
    elif s[x]=='н':
        sum+=1
        if sum>max:
            max=sum
    else:
        sum=0
print(s, max)