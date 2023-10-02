text=str(input('Ввод:'))
k=0
while ('а' in text):
    text=text.replace('а','о',1)
    k+=1
print(text,'\n', 'Кол-во замен:', k,'\n','Длина строки:', len(text))