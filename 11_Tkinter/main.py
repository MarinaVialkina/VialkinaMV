from tkinter import *
from v3_json import get_json
from PIL import Image, ImageTk

VisualStudioCode = get_json()
k = 0   #Счётчик для заполнения ячеек кнопкой "Ввод" при её нажатии и очищения ячеек при нажатии кнопки "Ещё раз".

def get_txt():
    '''Эта функция выводит JSON при вводе репозитория по имени:VisualStudioCode (если ячйки пустые)'''
    global k
    if k == 0:
        repozitory = txt.get()
        if repozitory == 'VisualStudioCode':
            vivod1=Label(window, text=('company:    ' + str(VisualStudioCode['company'])), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=41, anchor='w').grid(column=0, row=4, columnspan=2)
            vivod2=Label(window, text=('created_at: ' + str(VisualStudioCode['created_at'])), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=41, anchor='w').grid(column=0, row=5, columnspan=2)
            vivod3=Label(window, text=('email:  ' + str(VisualStudioCode['email'])), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=20, anchor='w').grid(column=0, row=6)
            vivod4=Label(window, text=('id: ' + str(VisualStudioCode['id'])), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=20, anchor='w').grid(column=0, row=7)
            vivod5=Label(window, text=('name:   ' + str(VisualStudioCode['name'])), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=20, anchor='w').grid(column=0, row=8)
            vivod6=Label(window, text=('url:    ' + str(VisualStudioCode['url'])), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=41, anchor='w').grid(column=0, row=9, columnspan=2)
            with open('file_vivod.txt', 'w') as file:
                file.write('company:    ' + str(VisualStudioCode['company']))
                file.write('\ncreated_at: ' + str(VisualStudioCode['created_at']))
                file.write('\nemail:  ' + str(VisualStudioCode['email']))
                file.write('\nid: ' + str(VisualStudioCode['id']))
                file.write('\nname:   ' + str(VisualStudioCode['name']))
                file.write('\nurl:    ' + str(VisualStudioCode['url']))
        else:
            vivod1=Label(window, text=('Имя репозитория введено не правильно!'), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=41, anchor='w').grid(column=0, row=4, columnspan=2)
            vivod2=Label(window, text=('(Посмотрите подсказку)'), font=('Comic Sans MS', 20), fg='#ede7df',bg='#705f46', width=41, anchor='w').grid(column=0, row=5, columnspan=2)
        k += 1
def again_enter():
    '''Эта функция очищает содержимое ячеек.'''
    global k
    vivod1=Label(window, text=('company:    ' + str(VisualStudioCode['company'])), font=('Comic Sans MS', 20), fg='#705f46',bg='#705f46', width=41, anchor='w').grid(column=0, row=4, columnspan=2)
    vivod2=Label(window, text=('created_at: ' + str(VisualStudioCode['created_at'])), font=('Comic Sans MS', 20), fg='#705f46',bg='#705f46', width=41, anchor='w').grid(column=0, row=5, columnspan=2)
    vivod3=Label(window, text=('email:  ' + str(VisualStudioCode['email'])), font=('Comic Sans MS', 20), fg='#705f46',bg='#705f46', width=20, anchor='w').grid(column=0, row=6)
    vivod4=Label(window, text=('id: ' + str(VisualStudioCode['id'])), font=('Comic Sans MS', 20), fg='#705f46',bg='#705f46', width=20, anchor='w').grid(column=0, row=7)
    vivod5=Label(window, text=('name:   ' + str(VisualStudioCode['name'])), font=('Comic Sans MS', 20), fg='#705f46',bg='#705f46', width=20, anchor='w').grid(column=0, row=8)
    vivod6=Label(window, text=('url:    ' + str(VisualStudioCode['url'])), font=('Comic Sans MS', 20), fg='#705f46',bg='#705f46', width=41, anchor='w').grid(column=0, row=9, columnspan=2)
    k = 0
def show_hint():
    '''Эта функция выводит и скрывает текст при нажатии на Checkbutton.'''
    value = chk_value.get()
    if value == 'True':
        lbl3 = Label(window, text='VisualStudioCode', font=('Comic Sans MS', 20), fg='#bfad91',bg='#705f46', anchor='w')
        lbl3.grid(column=1, row=2)
    else:
        lbl3 = Label(window, text='VisualStudioCode', font=('Comic Sans MS', 20), fg='#705f46',bg='#705f46', anchor='w')
        lbl3.grid(column=1, row=2)


window = Tk()
window.title('Самые популярные репозитории на GitHub. JSON.')
window.geometry('800x800+450+150')
window.resizable(False, False)
window.config(bg='#705f46')
photo = PhotoImage(file='11_Tkinter\photo1.png')
window.iconphoto(False, photo)

lbl1 = Label(window, text='Получение JSON по имени репозитория:', font=('Comic Sans MS', 22), fg='#705f46',
             bg='#bfad91', width=45)
lbl1.grid(column=0, row=0, columnspan=5)

lbl2 = Label(window, text='Ввод имени репозитория', font=('Comic Sans MS', 20), fg='#c9bda9',bg='#705f46', anchor='w')
lbl2.grid(column=0, row=1)

txt = Entry(window, width=20, font=('Comic Sans MS', 20))
txt.grid(column=1, row=1)

btn = Button(window, text=' Ввод  ', font=('Comic Sans MS', 18), fg='#705f46',bg='#bfad91', command=get_txt)
btn.grid(column=2, row=1)

btn1 = Button(window, text='Ещё раз', font=('Comic Sans MS', 18), fg='#705f46',bg='#bfad91', command=again_enter)
btn1.grid(column=2, row=2)

chk_value = StringVar()
chk = Checkbutton(window, text='Показать имя репозитория', font=('Comic Sans MS', 18), fg='#c9bda9',bg='#805f46', 
                command=show_hint, variable=chk_value, onvalue='True', offvalue='False')
chk.grid(column=0, row=2)

img = ImageTk.PhotoImage(Image.open(r'11_Tkinter\Image2.jpg'))
imag = Label(image=img).place(x=90, y= 450)

window.mainloop()